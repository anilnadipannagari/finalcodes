from abc import ABC,abstractmethod
class car(ABC):
    def __init__(self,name,colore,amount):
        self.name=name
        self.colore=colore
        self.amount=amount
        self.speed=0
    @abstractmethod
    def stop():
        pass
    @abstractmethod
    def speed_up():
        pass
    @abstractmethod
    def speed_down():
        pass    
class bmw(car):
    def speed_down(self):
        self.speed-=5
    def spe
    
    ed_up(self):
        self.speed+=5
    def stop(self):
        self.stop=0
class bently(car):
    def speed_down(self):
        self.speed-=50
    def spped_up(self):
        self.speed+=50
    def stop(self):
        self.stop=0
car1=bmw('Bently Bentega','Blue',21000000)
car2=bently('Bentega','orange',8000000)
print(bently.amount)
print(bently.name)
