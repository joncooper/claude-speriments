import os, sys, json
OUT = os.environ["ORACLE_OUT"]; SRC = os.environ["ORACLE_SRC"]
def emit(m): os.write(2, (m + "\n").encode())
src = open(SRC, "r", encoding="utf-8", errors="replace").read()
try:
    top = compile(src, "corpus", "exec")
except SyntaxError as e:
    emit("[py] compile failed: %r" % e); raise
# preorder traversal of all nested code objects, deterministic
CT = type(top)
seq = []
def walk(c):
    seq.append(c.co_code.hex())
    for k in c.co_consts:
        if isinstance(k, CT): walk(k)
walk(top)
json.dump(seq, open(os.path.join(OUT, "their_corpus_codes.json"), "w"))
emit("[py] their corpus: %d code objects" % len(seq))
