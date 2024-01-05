#frequcy of a charecter without using input
def ferq(a,b):
    cout=0
    for i in a:
        if i==b:
            cout+=1
    print(cout,' Number repeted')
ferq([10,2,3,4,56,2,4,2],2)