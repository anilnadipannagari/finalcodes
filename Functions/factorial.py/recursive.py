def sumn(st,ev):
    if st==ev:
        return st
    return st+sum(st+1,ev)
d=sumn(1,10)
print(d)