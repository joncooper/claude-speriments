import os, sys, json, zipimport, pickle
OUT = os.environ["ORACLE_OUT"]; ZIP = os.environ["ORACLE_ZIP"]
def emit(m): os.write(2, (m + "\n").encode())
emit("[py] driver2 live; version=%s" % sys.version.split()[0])

# 1) compile canonical snippets on THEIR interpreter -> detect opcode renumber
snips = {
 "pass": ("pass", "exec"), "load_a": ("a", "eval"), "add": ("a+b", "eval"),
 "call": ("f(x)", "eval"), "assign": ("a=1", "exec"),
 "ret1": ("def g():\n return 1", "exec"), "attr": ("a.b", "eval"),
 "import": ("import os", "exec"),
}
theirs = {}
for k,(src,mode) in snips.items():
    c = compile(src, "<s>", mode)
    theirs[k] = {"code": c.co_code.hex(), "names": list(c.co_names),
                 "consts": [repr(x) for x in c.co_consts]}
json.dump(theirs, open(os.path.join(OUT,"their_snips.json"),"w"), indent=0)
emit("[py] wrote their_snips.json")

# 2) export module code objects (decrypt+unmarshal via their loader; NO exec)
def code_to_tree(c):
    CT = type(c)
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
            "cellvars":list(c.co_cellvars),"filename":c.co_filename,
            "name":c.co_name,"qualname":c.co_qualname,"firstlineno":c.co_firstlineno,
            "linetable":c.co_linetable,"exceptiontable":c.co_exceptiontable}

z = zipimport.zipimporter(ZIP)
targets = ["abc","apex.auth","apex.dbxconn","dropbox.client.__init__",
           "dropbox.sync_engine.nucleus.__init__"]
loaded = {}
for name in targets:
    try:
        c = z.get_code(name)
    except Exception as e:
        emit("[py] get_code(%s) FAILED: %r" % (name,e)); continue
    loaded[name] = code_to_tree(c)
    emit("[py] %-34s co_name=%s consts=%d names=%d codelen=%d firstline=%d"
         % (name, c.co_name, len(c.co_consts), len(c.co_names), len(c.co_code), c.co_firstlineno))
pickle.dump(loaded, open(os.path.join(OUT,"code_trees.pkl"),"wb"), protocol=4)
emit("[py] wrote code_trees.pkl (%d modules)" % len(loaded))
