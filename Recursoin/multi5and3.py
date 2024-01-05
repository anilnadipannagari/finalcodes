def fname(a):
    if a%3==0 and a%5==0:
        return True
    else:
        return False
out=filter(fname,range(1,200))
print(list(out))
