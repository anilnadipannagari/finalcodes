a=int(input('number'))
# for i in range(a):
#     for j in range(i):
#         print('*',end='')
#     print()
#for j in range(1,i+1):
#print('*'*i)
for i in range(a):
    for j in range(i-1,i-1):
        print('*',end=' ')
    print()