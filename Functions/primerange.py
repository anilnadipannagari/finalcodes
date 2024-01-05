out=[]
def primerange(a,b):
    for i in range(a,b):
        out=[]
        cout=0
        for j in range(1,i+1):
            if i%j==0:
                cout+=1
        if cout==2:
            out=out+[i]
    #return out
d=primerange(1,100)
print('output of the following range',d)
                