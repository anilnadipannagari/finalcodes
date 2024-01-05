'''a='my name is anil kumar da'
dec=''
def index(a):
    for i in a:
        if i in 'aeiouAEIOU':
                inde=[i]
                dec+=inde
    return inde,i
b=index(a)
print('index of string a is: ',d)
'''
'''b='my name is anil kumar da'
str1=[]
i=0
while i<len(b):
    if i== 'a' or i== 'e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        str1=str1+[i]
    i+=1
    return str1
print(str1)'''