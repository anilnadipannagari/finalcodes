def fname(a):
    if a%2:
        return a**2
    else:
        return a**3
out=map(fname,[1,4,9,16])
print(list(out))
