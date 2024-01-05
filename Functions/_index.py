def index_vowel(a):
    out=[]
    i=0
    while i<len(a):
        if a[i] in 'aeiouAEIOU':
            out=out+[i]
        i+=1
    return out
a='my name id anil'
c=index_vowel(a)
print(c)