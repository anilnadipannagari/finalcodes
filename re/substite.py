import re
file=open(r"C:\Users\administrator.MCA\Desktop\re\random.txt",'r')
data=file.read()
file.close()
data1=re.sub('a','God Father',data)
print(data1)