xann: int = 0
def unp(t):
    a,b,*c = t
    [m,n] = t
    return a,b,c,m,n
def slic(a): return a[1:2:3], a[::2]
def strs(a): return f"{a!r:>{10}.{3}f}", f"{a=}"
def cmps(a,b): return a<b<=b!=a, a is b, a in b, a not in b
def colls(a,k): return [*a],{*a},{**k},(*a,),[i for i in a],{i for i in a},{i:i for i in a}
def callex(f,a,k): return f(*a,**k), f(1,x=2)
def gen(it):
    yield 1; z=yield 2; yield from it
async def ag(ait,cm,g):
    async with cm() as c:
        async for i in ait: await g(i)
    return [j async for j in ait]
def exc1():
    try: raise ValueError("x")
    except ValueError as e: raise
    finally: pass
def excstar(g):
    try: pass
    except* (TypeError,KeyError) as eg: pass
def mt(o):
    match o:
        case [a,b,*r]: return r
        case {"k": v, **rest}: return v,rest
        case str() | bytes(): return 1
        case C(x=1,y=px): return px
        case _ if o: return 9
class C:
    __match_args__=("x","y"); x=1; y=2
    def mk(s):
        s.x=1
        def inner(): return s.x
        return inner
def loops(n):
    t=0
    for i in range(n):
        if i: continue
        while t<n: t+=1; break
    else: t=-1
    return t
def raises(): raise RuntimeError from None
