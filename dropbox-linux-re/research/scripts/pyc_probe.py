import sys,math,collections
def ent(b):
    if not b: return 0.0
    c=collections.Counter(b); n=len(b)
    return -sum(v/n*math.log2(v/n) for v in c.values())
for p in sys.argv[1:]:
    d=open(p,'rb').read()
    hdr=d[:16]; body=d[16:]
    print(f"{p.split('/')[-1]:28s} len={len(d):7d} hdr={hdr.hex()} body_entropy={ent(body):.3f} bits/byte")
