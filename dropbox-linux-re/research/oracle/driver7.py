import os,zipfile,marshal,ctypes
ZIP=os.environ["ORACLE_ZIP"]
def emit(m): os.write(2,(m+"\n").encode())
for mod in ["apex/dbxconn.pyc","abc.pyc"]:
    body=zipfile.ZipFile(ZIP).read(mod)[16:]
    before=bytes(body[:40])              # copy of raw/ciphertext
    c=marshal.loads(body)                # decrypt+parse
    after=bytes(body[:40])               # same buffer, read again
    emit("%s: inplace_changed=%s"%(mod, before!=after))
    emit("  before=%s"%before.hex())
    emit("  after =%s"%after.hex())
    if before!=after:
        ks=bytes(before[i]^after[i] for i in range(40))
        emit("  XORks =%s"%ks.hex())
