'''out=[]
i=1
while i<=10:
    out=out+[i]
    i+=1
print(out)'''
def str(a,b):
    if a==b:
        return[a]
    return [a]+str(a+1,b)
out=str(1,19)