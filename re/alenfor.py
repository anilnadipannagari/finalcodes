import re
file=open(r"C:\Users\administrator.MCA\Desktop\re\random.txt",'r')
data=file.read()
data1=re.split('',data)
file.close()
cout=0
words=[]
for i in data1:
    out=re.match('^a',i)
    if out:
        words+=[i]
        cout+=1
print(cout)
print(words)
b=re.sub('a' )