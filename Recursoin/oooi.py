a=input('which colour you need ')
#input('enter the seat type u need'))
match a:
    case 'red':
        print("stop")
       
    case 'yellow':
        print('START')
       
    case 'green':
        print('GO')
       
    case _:
        print('not valid')
    