def fname(a):
    if 'A'<=a<='Z':
        return True
    else:
        return False
out=filter(fname,'aBc@15$67DEfgh')
print(list(out))
