from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def nooftyre(self,tyre):
        pass
class activa(vehicle):
    def nooftyre(self,tyre):
        self.tyre=tyre
        print("activa has ",self.tyre,"tyres")

class auto(vehicle):
    def nooftyre(self,tyre):
        self.tyre=tyre
        print("auto has ",self.tyre,"tyres")
class car(vehicle):
    def nooftyre(self,tyre):
        self.tyre=tyre
        print("car has ",self.tyre,"tyres")

a1=activa()
a1.nooftyre(2)

at=auto()
at.nooftyre(3)

c1=car()
c1.nooftyre(4)
