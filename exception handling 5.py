#exception handling

#index error

"""try:
    number=[10,30,40]
    print(number[5])
except IndexError:
    print("IndexError")
else:
    print("NoError")
finally:
    print("Executed")"""

#key error

"""try:
    data={"name":"varshini","age":20,"department":"eee"}
    print(data["address"])
except KeyError:
    print("KeyError")
else:
    print("NoError")
finally:
    print("Executed")"""

"""try:
    print(a)
except Exception as e:
    print(e)"""

#type error

"""try:
    int=(23,49,"varshini")
except TypeError:
    print("TypeError")
else:
    print("NoError")
finally:
    print("Executed")"""

#value error

"""try:
    a=int(input("enter the number:"))
    b=int(input("enter the string:"))
except ValueError:
    print("ValueError")
else:
    print("NoError")
finally:
    print("Executed")"""

#zero division error

"""try:
    a=20
    b=0
    c=a/b
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print("NoError")
finally:
    print("Executed")"""

"""try:
    a=int(input("enter the number:"))
    b=int(input("enter the string:"))
    result=a/b
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("InValid input")
else:
    print(result)
finally:
    print("Executed")"""

"""try:
   print(a)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("InValid input")
else:
    print(result)
finally:
    print("Executed")"""

#raise exception

"""num=-5
if num<0:
    raise Exception("negative num not allowed")
print(num)"""

"""try:
    num=int(input("enter the number:"))
    if num<0:
        raise ValueError("negative num not allowed")
    print(num)
except ValueError as e:
    print(e)"""

"""try:
    num=int(input("enter the number:"))
    if num<18:
        raise KeyError("before 18 not eligible")
    print(num)
except KeyError as e:
    print(e)
else:
    print("eligible")
finally:
    print("completed")"""

"""class AgeError(Exception):
    pass
try:
    age=int(input("enter the age:"))
    if age<18:
        raise AgeError("not eligible")
    print("eligible")
except AgeError as e:
    print(e)"""

"""class BalError(Exception):
    pass
try:
    pin=int(input("enter the pin:"))

    p=1212
    if p==pin:
        print("check balance")
        Bal = int(input("enter the Bal:"))
        if Bal<500:
            raise BalError("in sufficient balance")
        print("withdraw successful")
    else:
        print("wrong pin ")

except BalError as e:
    print(e)"""
