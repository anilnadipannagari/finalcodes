class Model:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def add(a,b,c):
        return a+b+c
obj=Model(add)
obj.add(2,3)
'''method & operatore overloading
method over loading is not possible for methods 
but we can overload operators'''