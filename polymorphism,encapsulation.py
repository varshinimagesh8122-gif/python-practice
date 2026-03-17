#polymorphism
"""class demo:
    def display(a,b):
        print(a)
    def display(a,b,c):
        print(b)
obj=demo()
obj.display(2,3)"""

"""class animal:
    def sound(self):
        print("sound the animal")
class dog:
    def sound(self):
        print("sound the dog")
obj=dog()
obj.sound()"""

#super method
"""class display:
    def show(self):
        print("this is parent class")
class demo(display):
    def show(self):
        super().show()
        print("this is child class")
obj=demo()
obj.show()"""

#encapsulation

"""class student:
    def __init__(self):
        self.__marks=0 #private variable
    def show_marks(self):
        print(self.__marks)
obj=student()
obj.show_marks()"""

#getter,setter
"""class student:
    def __init__(self):
        self.__marks=0
    def set_marks(self,m):
        self.__marks=m
    def get_marks(self):
        return self.__marks
obj=student()
obj.set_marks(90)
print(obj.get_marks())"""
