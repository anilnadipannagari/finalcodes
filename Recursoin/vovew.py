def rng(a):
    for j in range(0,len(a)):
        if a[j] in 'aeiouAEIOU':
            yield a[j]
            yield j
b='god father anil'
c=rng(b)
print(list(c))
