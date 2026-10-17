import os, sys, json, io, zipimport, opcode, dis, pickle
OUT = os.environ.get("ORACLE_OUT")
ZIP = os.environ.get("ORACLE_ZIP")

def emit(msg):
    os.write(2, (msg + "\n").encode())

emit("[py] driver live; version=%s" % sys.version.split()[0])

# 1) dump their opcode tables
with open(os.path.join(OUT, "their_opcode.json"), "w") as f:
    json.dump({
        "version": sys.version,
        "hexversion": sys.hexversion,
        "opmap": opcode.opmap,
        "opname": list(opcode.opname),
        "HAVE_ARGUMENT": opcode.HAVE_ARGUMENT,
        "EXTENDED_ARG": opcode.EXTENDED_ARG,
        "cmp_op": list(opcode.cmp_op),
        "hasconst": opcode.hasconst, "hasname": opcode.hasname,
        "hasjrel": opcode.hasjrel, "hasjabs": opcode.hasjabs,
        "haslocal": opcode.haslocal, "hasfree": opcode.hasfree,
    }, f)
emit("[py] wrote their_opcode.json (%d opcodes mapped)" % len(opcode.opmap))

z = zipimport.zipimporter(ZIP)

def code_to_tree(c):
    # capture every 3.11 co_* field; recurse into nested code objects in consts
    def conv(x):
        if isinstance(x, type(c)):
            return {"__code__": True, **code_to_tree(x)}
        if isinstance(x, tuple):
            return {"__tuple__": [conv(i) for i in x]}
        if isinstance(x, frozenset):
            return {"__frozenset__": [conv(i) for i in x]}
        return x  # int/str/bytes/float/complex/bool/None are picklable
    return {
        "argcount": c.co_argcount, "posonlyargcount": c.co_posonlyargcount,
        "kwonlyargcount": c.co_kwonlyargcount, "nlocals": c.co_nlocals,
        "stacksize": c.co_stacksize, "flags": c.co_flags,
        "code": c.co_code, "consts": [conv(k) for k in c.co_consts],
        "names": list(c.co_names), "varnames": list(c.co_varnames),
        "freevars": list(c.co_freevars), "cellvars": list(c.co_cellvars),
        "filename": c.co_filename, "name": c.co_name, "qualname": c.co_qualname,
        "firstlineno": c.co_firstlineno, "linetable": c.co_linetable,
        "exceptiontable": c.co_exceptiontable,
    }

targets = ["abc", "apex.auth", "apex.dbxconn", "dropbox.client.__init__"]
loaded = {}
for name in targets:
    try:
        c = z.get_code(name)              # decrypt + unmarshal, NO execution
    except Exception as e:
        emit("[py] get_code(%s) FAILED: %r" % (name, e))
        continue
    loaded[name] = code_to_tree(c)
    emit("[py] %-24s name=%s consts=%d names=%d codelen=%d"
         % (name, c.co_name, len(c.co_consts), len(c.co_names), len(c.co_code)))
    # their dis (uses their opmap) -> correct mnemonics
    buf = io.StringIO()
    try:
        dis.dis(c, file=buf)
        open(os.path.join(OUT, "dis_%s.txt" % name.replace(".", "_")), "w").write(buf.getvalue())
    except Exception as e:
        emit("[py] dis(%s) failed: %r" % (name, e))

with open(os.path.join(OUT, "code_trees.pkl"), "wb") as f:
    pickle.dump(loaded, f, protocol=4)
emit("[py] wrote code_trees.pkl (%d modules)" % len(loaded))
