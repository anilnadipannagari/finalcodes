def bookmyShow(x,y,z):
    print('Welcome to Book MyShow \n')
    print('Please enter your name : \n',end='')
    a=input()
    print('Select number of Seats you wish to book:\n',end='')
    b=int(input())
    print('Select Class you wish to Watch From:\n')
    print('select 1 for Dimond \n')
    print('select 2 for Gold \n')
    print('select 3 for Silver \n')
    print('Enter Your cofortable Option Class: ',end='')
    c=int(input())
    if c==1:
        bill=(b*200)
        print(f'\n Hi {a} and your are selected {b} seats for Dimond Class and your bill is {bill} \n ')
    elif c==2:
        bill=(b*150)
        print(f'Hi {a} and your are selected {b} seats for Dimond Class and your bill is {bill} \n')
    elif c==3:
        bill=(b*100)
        print(f'Hi {a} and your are selected {b} seats for Dimond Class and your bill is {bill} \n')
    else:
        print('Please Select Valid Class \n')
    return 'Thank you For Using Book my Sow My DEAR BOY \n'
print('')
dd=(bookmyShow('Anil',4,1))
print(dd)
print('')