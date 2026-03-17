#iteration

"""a=[10,20,30]
it=iter(a)
print(next(it))
print(next(it))
print(next(it))"""

"""class count:
    def __iter__(self):
        self.num=1
        return self
    def __next__(self):
        if self.num<=3:
            value=self.num
            self.num+=1
            return value
        else:
            raise StopIteration
obj=count()
for i in obj:
    print(i)"""

#generator
#ex
"""def demo():
    for i in range(3):
        return i
obj=demo()
print(obj)"""

"""def demo():
    for i in range(3):
        yield i
g=demo()
print(next(g))"""

"""def demo():
    for i in range(3):
        yield i
g=demo()
print(next(g))
print(next(g))
print(next(g))"""

"""def demo():
    for i in range(3):
        yield i
g=demo()
for n in g:
    print(n)"""


#decorator

def my_decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
@my_decorator
def display():
        print("hello")
display()