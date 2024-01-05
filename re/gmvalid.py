gmail=input('Enter an gmail.')
for i in gmail:
    if i in '@gmail.com':
        print(gmail,' is a valid mail id')
        break
    else:
        print('Enter a valid mail id')