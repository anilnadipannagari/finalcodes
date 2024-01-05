'''controller autometically calls the function no need to 
magic method called when we call the object '''
class Base:
    a=10
    b=20
    def __init__(self,c):
        self.c=c
class child(Base):
    def __init__(self,c,e,d):
        super().__init__(c)
        '''Base.__inint__(self,c)#also been used insted of super'''
        self.property3=e
        self.property4=d
obj=child(20,50,60)
print(obj.property3)
