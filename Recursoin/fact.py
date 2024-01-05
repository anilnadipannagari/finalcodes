def facto(a,n=1):
    if n==a:
        return a
    return a*facto(a,n+1)
d=facto(5)
print('the factorial of the n',d)