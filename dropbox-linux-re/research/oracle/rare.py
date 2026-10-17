async def af(cm,ait,g):
    async with cm() as x:
        async for i in ait(): await g(i)
    return [j async for j in ait()]
def gen(it):
    yield 1
    x = yield 2
    yield from it
def mt(o):
    match o:
        case [a,b,*r]: return a
        case {"k":v}: return v
        case str() | bytes(): return 1
        case object(x=1): return 2
        case _: return 0
def misc(a,*args,**kw):
    global G
    del a
    assert args,"m"
    try: pass
    except* ValueError: pass
    with open("x") as f, open("y") as h: pass
    return {**kw,'a':1},{*args},[*args],f"{a!r:>{10}}",a[1:2:3]
class C:
    __slots__=('a',)
    def __init__(self): self.a=1
    @property
    def p(self): return self.a
