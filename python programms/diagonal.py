#print only in border with diagonal
rows=int(input('enter the number of rows:- ')) 
col=int(input('enter the number of rows:- ')) 
for i in range(rows):
    for j in range(col):
        if i==0 or i==rows-1 or i==j or rows-i-1==j:
            print('+',end=' ')
        elif j==0 or j==col-1:
            print('+',end=' ')
        else:
            print(' ',end=' ')
    print()