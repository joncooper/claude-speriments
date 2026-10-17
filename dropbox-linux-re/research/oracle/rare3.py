G=0
def dg():
    global G
    del G
def outer():
    c=1
    def inner():
        nonlocal c
        del c
    class K:
        y=c
    return inner,K
