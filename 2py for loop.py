"""a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(1, 20, 2):
    print(i)
print("odd number")
for i in range(0, 20, 2):
    print(i)
else:
    print("even number")"""

#prime number
"""num= int(input("enter the prime number:"))
count=0
for i in range (1,num+1):
    if num % i == 0:
        count=count+1
if count==2:
    print("prime number")
else:
    print("not prime number")"""

#muliplication table

"""num = int(input("enter the number:"))
for i in range(1,10):
    print(num,"x",i, "=",i*num )"""

#factorial

"""fact=5
for i in range (1,5):
    fact = fact*i
print(fact)"""

#natural number

"""num=int(input("enter the number:"))
for i in range (1,100):
    print(i)"""

# count vowels in string

"""string=input("enter the string:")
for i in string:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        print(i, "=", string.count(i))"""

#print
"""for i in range(0,100):
    print(i, " ",i+1)"""

#print number
"""n= 1
for i in range(1,2):
    print(i, " ", n)
    print(i, " ", n,n+1)
    print(i, " ", n,n+1,n+2)
    print(i, " ", n,n+1,n+2,n+3)"""

#count digit

"""num=int(input("enter the number:"))
count=0
while  num!=0:
    num = num//10
    count=count+1
    print(num," ",count)"""

#reverse number

"""num =int(input("enter the number:"))
rev = 0
while num>0:
    digit = num % 10
    rev = rev*10+digit
    num = num // 10
print("reverse",rev)"""

# factorial

"""i=1
fact=1
while (i<=6):
    fact=fact*i
    print(fact)
    i=i+1"""


#uncondition statement

"""for i in range(1,10):
    pass
print("hello world")
print(i)"""


#prime number

"""num=int(input("enter the number:"))
for i in range(2,num):
    if num % i ==0:
        print("not prime")
        break
else:
    print("prime")"""

#continue
#odd number
"""i=1
while i<50:
    if i%2==0:
        print("odd number")
        i=i+1
        continue
    print(i)
    i=i+1
print("loop exit")"""

#skip vowels


"""a="python programming"
vowels="aeiouAEIOU"
for i in a:
    if i =="a" or i =="e" or i =="i" or i =="o" or i =="u":
        continue
    print(i)"""

# skip negative number

"""a=[2,3,-4,-5,6,-7]
for i in a:
    if i<=0:
        continue
    print(i)"""

#divisible
"""for i in range(0,51):
    if (i % 5 == 0):
        print("divisible by 5")
        continue
    print(i)"""


