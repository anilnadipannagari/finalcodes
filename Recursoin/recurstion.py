#programme to add all value in given homogenoues list collection by using recurstion
'''i=0    
whil i<len(a):
    sum=sum+a[i]
    i+=1
print(sum)'''
def recur(var,i=0):
    if i==len(var)-1:
        if var[i]%2==0:
            return var[i]
        else:
            return 0
    if var[i]%2==0:
            return var[i]+recur(var,i+1)
    else:
        return recur(var,i+1)
a=[1,2,3,4,5,6,7]
d=recur(a)
print('the recursive code oth the input',d)