import os, sys, json, zipimport, zipfile, marshal, pickle
OUT = os.environ["ORACLE_OUT"]; ZIP = os.environ["ORACLE_ZIP"]
def emit(m): os.write(2, (m + "\n").encode())
emit("[py] driver4 live %s" % sys.version.split()[0])

zf = zipfile.ZipFile(ZIP)
pycs = [n for n in zf.namelist() if n.endswith(".pyc")]
emit("[py] %d pyc entries in zip" % len(pycs))

# Q1: does THEIR marshal.loads decrypt a raw pyc body directly?
sample = zf.read("abc.pyc")
for strip in (16,):
    try:
        obj = marshal.loads(sample[strip:]); emit("[py] marshal.loads(abc body[%d:]) -> %r" % (strip, type(obj)))
    except Exception as e:
        emit("[py] marshal.loads(abc body[%d:]) FAILED: %r" % (strip, e))

CT = type(compile("0","<s>","eval"))
def code_to_tree(c):
    def conv(x):
        if isinstance(x, CT): return {"__code__": True, **code_to_tree(x)}
        if isinstance(x, tuple): return {"__t__": [conv(i) for i in x]}
        if isinstance(x, frozenset): return {"__fs__": [conv(i) for i in x]}
        return x
    return {"argcount":c.co_argcount,"posonlyargcount":c.co_posonlyargcount,
            "kwonlyargcount":c.co_kwonlyargcount,"nlocals":c.co_nlocals,
            "stacksize":c.co_stacksize,"flags":c.co_flags,"code":c.co_code,
            "consts":[conv(k) for k in c.co_consts],"names":list(c.co_names),
            "varnames":list(c.co_varnames),"freevars":list(c.co_freevars),
            "cellvars":list(c.co_cellvars),"filename":c.co_filename,"name":c.co_name,
            "qualname":c.co_qualname,"firstlineno":c.co_firstlineno,
            "linetable":c.co_linetable,"exceptiontable":c.co_exceptiontable}

# Decrypt EVERY module by reading raw bytes and unmarshalling via their marshal.
# (Decryption is applied by their marshal/loader; we never execute module code.)
ok = 0; fails = []
out = open(os.path.join(OUT, "all_trees.pkl"), "wb")
pk = pickle.Pickler(out, protocol=4)
for n in pycs:
    body = zf.read(n)[16:]
    try:
        code = marshal.loads(body)
        pk.dump((n, code_to_tree(code)))
        ok += 1
    except Exception as e:
        fails.append((n, repr(e)))
out.close()
emit("[py] decrypted+exported %d/%d modules; %d failed" % (ok, len(pycs), len(fails)))
json.dump(fails[:50], open(os.path.join(OUT,"export_fails.json"),"w"))
