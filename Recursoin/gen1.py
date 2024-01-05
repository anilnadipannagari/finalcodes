#wap programe to get square of a number and twice of a number in the range 5 to 15 by using generatore
def rng(a,b):
    for j in range(a,b+1):
        yield j**2
        yield j*2
b=rng(1,15)
print(list(b))