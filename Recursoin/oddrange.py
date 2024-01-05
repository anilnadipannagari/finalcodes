def rangeodd(a):
    if not a%2==0:
        return a
def mapp(b):
    return b*b
out=map(mapp,filter(rangeodd,range(1,100)))
print(list(out))