import marshal, dis, sys
p = sys.argv[1]
data = open(p,'rb').read()
# strip 16-byte pyc header (magic4 + bitfield4 + mtime/size 8)
body = data[16:]
try:
    code = marshal.loads(body)
except Exception as e:
    print("MARSHAL FAIL:", type(e).__name__, e); sys.exit(2)
print("MARSHAL OK:", code)
print("co_names:", code.co_names[:15])
print("co_consts head:", [c for c in code.co_consts[:8]])
print("---- dis (first 40 lines) ----")
import io
buf=io.StringIO()
try:
    dis.dis(code, file=buf)
    print("\n".join(buf.getvalue().splitlines()[:40]))
except Exception as e:
    print("DIS FAIL:", type(e).__name__, e)
