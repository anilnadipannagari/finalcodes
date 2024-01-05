def freq(a,b):
    cout=0
    for i in a:
      if i==b:
        cout+=1
    return cout
a='my a name is anil kumar da'
b='a'
c=freq(a,b)
print('the frequency of a number :',c)