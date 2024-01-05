def index_vowel(a):
    out=[]
    i=0
    for i in range(0,len(a)):
        if a[i] in 'aeiouAEIOU':
            out=out+[i]
    return out
a="my name id anil"
c=index_vowel(a)
print(c)