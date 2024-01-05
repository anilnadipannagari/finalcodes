#programme to add the integer present in a heterogenouus list data items
def hetlist(a):
    sum=0
    for i in a:
        if type(i)==int:
                sum+=i
    print(sum,' is the sum of the all Number ')
hetlist([10,'a','b',10,7,4,'hi'])