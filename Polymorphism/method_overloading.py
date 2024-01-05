class Method:
    def __init__(self,a,b):
        return a+b
    def __add__(self,other):
        return self.a+other.add
    def __sub__(self,other):
        return self.a-other.add
    def __mul__(self,other):
        return self.a*other.add
    def __div__(self,other):
        return self.a/other.add

x=Method(10)
y=Method(20)
print(x+y)