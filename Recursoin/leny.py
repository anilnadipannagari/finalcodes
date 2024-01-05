b=[1,[4,5,6],{7,8},'e',{'a':1},9.5,12]
def factd(a):
    for i in a:
        if type(i) in [list,tuple,str,dict,set]:
            yield len(i)
        else:
            yield i
c=factd(b)
print(list(c))


