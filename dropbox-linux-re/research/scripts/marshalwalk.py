import sys,math,collections
TYPES={0x30:'NULL',0x4e:'None',0x46:'False',0x54:'True',0x53:'StopIter',0x2e:'Ellipsis',
0x69:'int32',0x49:'int64',0x6c:'long',0x67:'float_bin',0x79:'complex_bin',
0x73:'string/bytes',0x74:'interned',0x72:'ref',0x52:'shortref',
0x28:'tuple',0x29:'smalltuple',0x5b:'list',0x7b:'dict',0x3c:'frozenset',0x3e:'set',
0x63:'CODE',0x75:'unicode',0x7a:'short_ascii',0x5a:'short_ascii_interned',
0x61:'ascii',0x41:'ascii_interned',0xe3:'CODE+ref'}
def ent(b):
    if not b: return 0.0
    c=collections.Counter(b); n=len(b); return -sum(v/n*math.log2(v/n) for v in c.values())
def walk(body, maxn=40):
    i=0; out=[]
    import struct
    for _ in range(maxn):
        if i>=len(body): break
        t=body[i]; base=t&0x7f; ref=t&0x80
        name=TYPES.get(base, f'?0x{base:02x}')
        out.append((i,hex(t),name+('+ref' if ref else '')))
        i+=1
        if base in (0x30,0x4e,0x46,0x54,0x53,0x2e): continue
        if base==0x69: i+=4; continue
        if base==0x67: 
            if i<len(body): ln=body[i]; i+=1+ln
            continue
        if base in (0x73,0x75,0x74,0x61,0x41): # string-ish: 4-byte len + data
            if i+4<=len(body):
                ln=struct.unpack('<I',body[i:i+4])[0]; out.append(('  len',ln,'')); i+=4+ (ln if ln<10_000_000 else 0)
            continue
        if base in (0x7a,0x5a): # short ascii: 1-byte len
            if i<len(body): ln=body[i]; i+=1+ln
            continue
        if base in (0x29,): # small tuple: 1-byte count, then items (we don't recurse deeply)
            if i<len(body): n=body[i]; out.append(('  n',n,'')); i+=1
            continue
        if base==0x63 or base==0xe3-0x80:
            # code object: argcount,posonly,kwonly,stacksize,flags = 5x int32
            vals=struct.unpack('<5i', body[i:i+20]) if i+20<=len(body) else None
            out.append(('  code hdr(argc,posonly,kwonly,stack,flags)',vals,'')); i+=20
            continue
        # unknown -> stop
        out.append(('  STOP unknown type',hex(t),'')); break
    return out,i
for p in sys.argv[1:]:
    d=open(p,'rb').read(); body=d[16:]
    print(f"\n==== {p.split('/')[-1]} bodylen={len(body)} ent(all)={ent(body):.2f} ent(first64)={ent(body[:64]):.2f} ent(tail)={ent(body[-64:]):.2f}")
    print("  first48:", body[:48].hex())
    for row in walk(body)[0][:14]: print("   ",row)
