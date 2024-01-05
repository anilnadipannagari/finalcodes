#length of i is even then print average of two els eprint the middle value.
#//--> called floor devesion it will remove decimal point.
z=[(1,2),[4,5,3],(11,12,13),[9,8,7,6]]
def ran(a):
    for i in a:
        if len(i)%2==0:
            yield (i[0]+i[-1])/2
        else:
            yield[len(i)//2]
b=ran(z)
print('hello',list(b))
        