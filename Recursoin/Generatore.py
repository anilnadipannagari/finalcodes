def gen(a,b):
    yield a+b
    yield a-b
    yield a*b
    yield a/b
b=gen(5,9)
print('hi',b)
for i in b:
    print(i)