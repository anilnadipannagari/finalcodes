def leng(a):
    if type(a) in [str,list,set,dict,tuple]:
        return len(a)
    else:
        return a
v=[1,(4,5),(7,9),{1:2}]
out=map(leng,v)
i=0
while i<1000:
    print(list(out))
    
