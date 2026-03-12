#function

"""def student(name,age,*args,**kwargs):
    print("name",age,"*args","**kwargs")
student("varshini",20,"python","sql","excel",**kwargs:name="varshini",age=20,class="a",dep="EEE")"""

#position argument

"""def student(department,section):
    print(department,section)
student("EEE","A")"""

#keyword argument

"""def student(name,department):
    print(name,department)
student(name="varshini",department="EEE")"""

#default argument

"""def greet(name="student"):
    print("hello","varshini",name)
    print(name,"good morning","varshini")
greet()"""

#variable length argument

"""def student(degree):
    print(degree)
student("bca","BE","cse")"""

#function
#positional argument

"""def student (name,age):
    print(name,age)
student("varshini",20)"""

#keyword argument

"""def student (name,age):
    print(name,age)
student(age=20,name="varshini")"""

#default argument

"""def greet(name="student"):
    print("hello",name)
greet()"""

#variable length argument
#args
"""def demo (*degree):
    print(*degree)
demo("bsc","b.com","be")"""

#kwargs

"""def student (**kwargs):
    print(kwargs)
student(name="varshini",age=20,course="engineering",section="a")"""

#allfunction

"""def student (name,age,*args,**kwargs):
    print(name,age,*args,kwargs)
student(age=20,name="varshini",course="engineering",section="a",city="kancheepuram")"""

#variable
#local variable

"""def demo():
    x=10
    print(x)
demo()"""

#globalvariable
"""x=50
def show():
    print(x)
show()"""

#nonlocal variable

"""def outer ():
    x=20
    def inner():
        print(x)
    inner()
outer()"""

#global keyword

"""x=5
def change():
    global x
    x=10
change()
print(x)"""

#nonlocal keyword

"""def outer():
    x=5
    def inner():
        nonlocal x
        x=10
    inner()
    print(x)
outer()"""

"""def check(number):
    if number % 2 == 0:
        print("even number")
    else:
        print("odd number")
#getting input from user
number=int(input("enter the number:"))

check(number)"""

#reverse string

"""a="varshini"
rev=" "
for i in a:
    rev=i+rev   
    print(rev)"""

# reverse the word
"""a="i"
b="love"
c="python"

for j in a,b,c:
    print(c,b,a)"""


#lambda function

"""add=lambda x,y:x+y
print(add(2,4))"""

"""odd_even=lambda x:x%2==0
print(odd_even(5))"""

"""import math
print(dir(math))"""

"""import math
print(math.sqrt(25))"""

"""help()
import math
help(math.sqrt)"""

#filtering greater than 10

"""numbers=[5,12,7,18,3,20]
x=list(filter(lambda a:a>10,numbers))
print("number greater than 10",x)"""

#reverse the string

"""name="varshini"
reverse_string=lambda s: s[::-1]
print("reverse string:",reverse_string(name))"""

#filtering odd even

"""number=[2,3,6,4,90,34,98,5,65,54]
odd_number=list(filter(lambda a:a%2!=0,number))
even_number=list(filter(lambda a:a%2==0,number))
print("odd number",odd_number)
print("even number",even_number)"""
