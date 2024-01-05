a=int(input('Enter a number'))
b=a
sum=0
for i in range(a):
    if i%2==0:
        sum=sum+i
    else:
        pass
if sum==b:
    print('Palindrom number')
else:
    print('Not a palindrom number')