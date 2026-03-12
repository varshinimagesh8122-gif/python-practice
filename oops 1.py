#abstraction
"""from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car start")
c=car()
c.start()"""

"""from abc import ABC, abstractmethod
class pay(ABC):
    @abstractmethod
    def pay(self):
        pass
class card(pay):
    def pay(self):
        print("card payment")
class upi(pay):
    def pay(self):
        print("upi payment")

c = card()5
c.pay()
u = upi()
u.pay()"""

#constructor
"""class student:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
s1=student("arun",35)
print(s1.name)"""

#inheritance

"""class parent:
    def __init__(self):
        self._age=34
class child(parent):
    def show(self):
        print(self._age)
obj=child()
obj.show()
print(obj._age)"""

#practice

#single inheritance
"""class manager:
    def __init__(self):
        self._name="varshini"
        self._salary=25000
class employee(manager):
    def show(self):
        print(self._name)
        print(self._salary)
obj=employee()
obj.show()
print(obj._name)
print(obj._salary)"""

#multiple inheritance
"""class camera_phone:
    def __init__(self):
        self._model="apple"
        self._cost=45000
class smart_phone1(camera_phone):
    def show(self):
        print(self._model)
class smart_phone2(camera_phone):
    def show(self):
        print(self._cost)

obj=smart_phone1()
obj.show()
obj=smart_phone2()
obj.show()"""


"""class camera:
    def open_camera(self):
        print("click the camera")
class phone:
    def using_smart(self):
        print("check the photo")
class smart_phone (camera,phone):
    def edit(self):
        print("camera quality well")
s=smart_phone()
s.open_camera()
s.using_smart()
s.edit()"""

#multilevel inheritance
"""class vehicle:
    def start(self):
        print("vehicle start")
class car(vehicle):
    def drive(self):
        print("drive the car")
class electric_car(car):
    def charge(self):
        print("charge the electric car")
c=car()
e=electric_car()
c.start()
c.drive()
e.drive()

e.charge()"""
