a=45
b=43
c=a+b
print(c)

#check odd even

"""number = int(input("enter the number:"))
if number % 2 == 0:
    print( number,"is even")
else:
    print( number,"is odd")"""

#divisible by3and5

"""number = int(input("enter the number:"))
if number % 3 == 0:
    print(" it is divisible by 3")
    number = int(input("enter the number:"))
    if number % 5 == 0:
        print(" it is divisible by 5")
    else:
        print(" it is not divisible by 5")
else:
    print(" it is not divisible by 3")"""

#username login

"""username = input("enter your username:")
if username == "varshini":
    print(username ,"is valid")
else:
    print(username ,"is invalid")"""

#check speed

"""a=50
b=80
speed = int(input("enter the speed"))
if speed>b:
    print("high speed")
else:
    print("medium speed")"""

#pass character

"""password = input("enter your password:")
if len (password) <= 8:
    print("password is registered")
else:
    print("set minimum 8 character")"""

#day find

"""day=int(input("enter your day:"))
if day == 1:
  print("the day is monday")
elif day == 2:
  print("the day is tuesday")
elif day == 3:
    print("the day is wednesday")
elif day == 4:
    print("the day is thursday")
elif day == 5:
    print("the day is friday")
elif day == 6:
    print("the day is saturday")
elif day == 7:
    print("the day is sunday")
else:
  print("the day is invalid")"""

#simple calculator

"""a=input("enter first number:")
b=input("enter second number:")
operator = input("enter operator (+,-,*,/):")
 if operator == " + ":
     print("addition:", a + b)
 elif operator == " _ ":
     print("subtraction:", a - b)
 elif operator == " * ":
     print("multiplication:", a * b)
 elif operator == " / ":
     if b == 0:
         print("division:", a / b)
     else:
         print("cannot divide by 0")
else:
     print("data exit")"""

#traffic signal

"""colour = input("enter the colour:")
if colour == "green":
    print("go")
elif colour == "yello":
    print("get ready")
elif colour == "red":
    print("stop")
else:
    print("invalid colour")"""

#season

"""season=int(input("enter the season:"))
if season == 1:
    print("winter season")
elif season == 2:
    print("summer season")
elif season ==3:
    print("rainy season")
else:
    print("invalid season")"""

#ATM withdrawal check

"""bal=5000
pin=2282
p=int(input("enter the pin number:"))
if p == pin:
    amount = int(input("enter the amount:"))
    if amount <= bal:
        print(amount,"withdrawal successful")
    else:
        print(amount,"insufficient balance")
else:
    print("invalid pin number")"""

#job eligibility check

"""age=int(input("enter the age:"))
degree=input("enter the degree:")
if age >= 18:
    print("eligible ")
    if degree == "Engineering":
        print("degree is eligible")
    else:
        print("not eligible")
else:
    print("not eligible")"""
