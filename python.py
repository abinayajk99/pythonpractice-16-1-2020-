#Lambda functions

#from fuctools import reduce
nums=[1,2,3,4,5,6,7,8,9]
evens=list(filter(lambda n:n%2==0,nums))
print(evens)
doubles=list(map(lambda n:n+2,evens))
print(doubles)
#su=reduce(lambda a,b:a+b,doubles)
#print(su)
=========================================================================================================================
#class:
#class
class book:
    def config(self):
        print("i5,10gb,iTb")
com=book()
com2=book()
com.config()
com2.config()
========================================================================================================================
#class
class book:
    def __init__(self,name,price):
        self.name=name;
        self.price=price;
        
    def config(self):
        
        print("name=%s,price=%s"%(self.name,self.price))
print("Books:")
com=book("abi",1000)
com2=book("gan",20)
com.config()
com2.config()
================================================Classes and Methods==================================================

>>>class Dog:
...    def __init__(self, name):
...        self.name = name
...        self.tricks = []
...    def add_trick(self, trick):
...        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
>>>def scope_test():
...    def do_local():
...        spam = "local spam"
...    def do_nonlocal():
...        nonlocal spam
...        spam = "nonlocal spam"
...    def do_global():
...        global spam
...        spam = "global spam"
>>>spam = "test spam"
>>>do_local()
>>>print("After local assignment:", spam)
After local assignment: test spam
>>>do_nonlocal()
>>>print("After nonlocal assignment:", spam)
After nonlocal assignment: nonlocal spam
>>>do_global()
>>>print("After global assignment:", spam)
After global assignment: nonlocal spam
>>>scope_test()
>>>print("In global scope:", spam)
In global scope: global spam


>>>class Reverse:
...	def __init__(self, data):
...        self.data = data
...        self.index = len(data)
...    def __iter__(self):
...        return self
...    def next(self):
...        if self.index == 0:
...            raise StopIteration
...        self.index = self.index - 1
...        return self.data[self.index]

>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print char
...
m
a
p
s

==============================================Inheritance==========================

>>>class Polygon:
...    def __init__(self, no_of_sides):
...        self.n = no_of_sides
...        self.sides = [0 for i in range(no_of_sides)]
...    def inputSides(self):
...        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]
...    def dispSides(self):
...        for i in range(self.n):
...            print("Side",i+1,"is",self.sides[i])

>>>class Triangle(Polygon):
...    def __init__(self):
...        Polygon.__init__(self,3)
...    def findArea(self):
...        a, b, c = self.sides
...        s = (a + b + c) / 2
...        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
...        print('The area of the triangle is %0.2f' %area)

>>> t = Triangle()
>>> t.inputSides()
Enter side 1 : 3
Enter side 2 : 5
Enter side 3 : 4
>>> t.dispSides()
Side 1 is 3.0
Side 2 is 5.0
Side 3 is 4.0
>>> t.findArea()
The area of the triangle is 6.00

>>> isinstance(t,Triangle)
True
>>> isinstance(t,Polygon)
True
>>> isinstance(t,int)
False
>>> isinstance(t,object)
True
>>> issubclass(Polygon,Triangle)
False
>>> issubclass(Triangle,Polygon)
True
>>> issubclass(bool,int)
True
