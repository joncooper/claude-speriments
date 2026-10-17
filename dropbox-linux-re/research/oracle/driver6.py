import os, sys, zipfile, marshal, math, collections
OUT=os.environ["ORACLE_OUT"]; ZIP=os.environ["ORACLE_ZIP"]
def emit(m): os.write(2,(m+"\n").encode())
def ent(b):
    if not b: return 0.0
    c=collections.Counter(b); n=len(b); return -sum(v/n*math.log2(v/n) for v in c.values())
zf=zipfile.ZipFile(ZIP)
mods=["abc.pyc","_weakrefset.pyc","apex/dbxconn.pyc","apex/auth.pyc"]
kss={}
for m in mods:
    body=zf.read(m)[16:]
    code=marshal.loads(body)          # their loads (decrypts)
    p=marshal.dumps(code)             # does their dumps re-encrypt?
    emit("%-20s len(body)=%d len(dumps)=%d ent(body)=%.2f ent(dumps)=%.2f eq=%s"
         %(m,len(body),len(p),ent(body),ent(p),body==p))
    emit("   body[:24]=%s"%body[:24].hex())
    emit("   dump[:24]=%s"%p[:24].hex())
    n=min(len(body),len(p)); ks=bytes(body[i]^p[i] for i in range(n)); kss[m]=ks
    emit("   xor [:24]=%s  (ks zero-bytes %d/%d)"%(ks[:24].hex(),ks.count(0),n))
# are keystreams identical across modules (fixed keystream)?
ks0=kss[mods[0]]
for m in mods[1:]:
    k=kss[m]; n=min(len(ks0),len(k)); same=sum(1 for i in range(n) if ks0[i]==k[i])
    emit("ks match %s vs %s: %d/%d"%(mods[0],m,same,n))
