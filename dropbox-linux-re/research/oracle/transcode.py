#!/usr/bin/env python3.11
"""Dropbox pyc transcoder. Reads all_trees.pkl (decrypted code objects exported
from Dropbox's own interpreter) and rebuilds STOCK CPython 3.11 .pyc files by
remapping Dropbox's permuted opcode numbering back to canonical 3.11 opcodes.
Output .pyc are readable by any stock 3.11 tool (dis, decompilers)."""
import json, pickle, marshal, types, importlib.util, io, dis, os, sys

OUT = os.path.join(os.path.dirname(__file__), "out")
PYC = os.path.join(OUT, "stockpyc")
M = json.load(open(os.path.join(os.path.dirname(__file__), "opcode_map.json")))
T2S = {int(k): int(v) for k, v in M["their_to_stock"].items()}; T2S[0] = 0

def remap(co):
    b = bytearray(co)
    for i in range(0, len(b), 2):
        b[i] = T2S.get(b[i], b[i])
    return bytes(b)

def rebuild(x):
    if isinstance(x, dict):
        if x.get("__code__"): return build(x)
        if "__t__" in x: return tuple(rebuild(i) for i in x["__t__"])
        if "__fs__" in x: return frozenset(rebuild(i) for i in x["__fs__"])
    return x

def build(d):
    return types.CodeType(
        d["argcount"], d["posonlyargcount"], d["kwonlyargcount"], d["nlocals"],
        d["stacksize"], d["flags"], remap(bytes(d["code"])),
        tuple(rebuild(k) for k in d["consts"]), tuple(d["names"]), tuple(d["varnames"]),
        d["filename"], d["name"], d["qualname"], d["firstlineno"],
        bytes(d["linetable"]), bytes(d["exceptiontable"]),
        tuple(d["freevars"]), tuple(d["cellvars"]))

def pyc_bytes(code):
    return (importlib.util.MAGIC_NUMBER + (0).to_bytes(4,"little")*3 + marshal.dumps(code))

def disasm(code):
    buf = io.StringIO(); dis.dis(code, file=buf); return buf.getvalue()

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    up = pickle.Unpickler(open(os.path.join(OUT, "all_trees.pkl"), "rb"))
    n = ok = 0; errs = []
    while True:
        try: name, tree = up.load()
        except EOFError: break
        n += 1
        if only and only not in name: continue
        try:
            code = build(tree)
            dst = os.path.join(PYC, name)              # name == zip path e.g. dropbox/x.pyc
            os.makedirs(os.path.dirname(dst) or PYC, exist_ok=True)
            open(dst, "wb").write(pyc_bytes(code))
            ok += 1
        except Exception as e:
            errs.append((name, repr(e)))
    print("transcoded %d/%d modules; %d errors" % (ok, n, len(errs)))
    for nm, e in errs[:15]: print("  ERR", nm, e)
