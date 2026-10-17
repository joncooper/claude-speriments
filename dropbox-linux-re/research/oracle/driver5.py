import os, sys, json
OUT = os.environ["ORACLE_OUT"]; LIST = os.environ["ORACLE_LIST"]; RARE = os.environ["ORACLE_RARE"]
def emit(m): os.write(2, (m + "\n").encode())
files = [l.strip() for l in open(LIST) if l.strip()] + [RARE]
CT = type(compile("0","<s>","eval"))
seq = []
def walk(c):
    seq.append(c.co_code.hex())
    for k in c.co_consts:
        if isinstance(k, CT): walk(k)
nf = 0
for path in files:
    try:
        src = open(path, "r", encoding="utf-8", errors="replace").read()
        c = compile(src, os.path.basename(path), "exec")
    except Exception as e:
        continue
    nf += 1
    walk(c)
json.dump(seq, open(os.path.join(OUT, "their_corpus_codes.json"), "w"))
emit("[py] compiled %d files -> %d code objects" % (nf, len(seq)))
