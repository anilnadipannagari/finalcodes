class Car:
    name='cars'

    def __init__(self,name,milage,price,color):
        self.name=name
        self.milage=milage
        self.price=price
        self.color=color

class Supre(Car):
    pass
class Benz(Car):
    pass
car1=Supre('suprea red',10,50000,'white')
car2=Benz('glx',8,20000,'blue')