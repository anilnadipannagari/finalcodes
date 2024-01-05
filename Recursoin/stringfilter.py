def rangeodd(a):
    if 'a'<= a<='z':
        return a
def mapp(args):
    return ord(args)
z='a1b2c3Def12@#9z'
out=map(mapp,filter(rangeodd,z))
print(list(out))