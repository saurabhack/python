from abc import ABC

class car(ABC):
    def mileage(self):
        pass

class tesla(car):
    def mileage(self):
        print("the mileage is 30 kmph\n")

class suzuki(car):
    def mileage(self):
        print("the mileage is 40 kmph")

class duster(car):
    def mileage(self):
        print("the mileage is 50 kmph")


t=tesla()
s=suzuki()
d=duster()

for d in (t,s,d):
    d.mileage()
