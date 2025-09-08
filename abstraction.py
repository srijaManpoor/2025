from abc import ABC , abstractmethod
#hiding unnecessary data and showing the required data is known as abstraction
#if we have one or more abstract method in a class then it is known as abstract class

class car(ABC):
    @abstractmethod
    def mileage(self):
        pass
class BMW(car):
    def mileage(self):
        print("i go 25 kmpk")
class TESLA(car):
    def mileage(self):
        print("i go 40 kmph")
class Nano(car):
    def mileage(self):
        print("i go 45 kmph")
ob=Nano()
ob.mileage()
