# DAY-10

#) Tasks
# Write the code for the belwo tasks using function
# 1.) d1 = {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
#a.) Find the min ans max priced product
# b.) Find the product starts with 's' and 'S'

# 2.) Find the n = 67, is strong number or not

# 3.) l1 = [1,2,3,4,5,6] 
# n=2 --> [5, 6, 1,2,3,4]
# n=3--> [4,5,6, 1,2,3]

d1 = {"shirt": 1000, "pant": 1500, "Shoes": "900", "handkey": 30}
for val in d1:
    if d1[val] == min(d1.values()):
        print(val)
for val in d1:
    if d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
        print(val)

# * polymorphisms
# 1)
# 2) method overriding

# $ method overloading
# * polymorphism in classes using Inheritance
# ! EXAMPLE:1
class bank:
    def ratio(self):
        print("All banks has repo rate")
class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")
class IOB(bank):
    def ratio(self):
        print("IOB rate is 7.5%")
i = IOB()
i.ratio()
s = SBI()
s.ratio()

# ! EXAMPLE:2
class USA:
    def language(self):
        print("English")
    def capital(self):
        print("Washington DC")
class India(USA):
    def language(self):
        print("None")
    def capital(self):
        print("New Delhi")
I = India()
I.language()
I.capital()

# ! EXAMPLE:3
# polymorphism using objects
# c1,c2 ---> c1=print(c1),print(c2)
# f1,f2

class c1:
    def f1(self):
        print("class 1")
class c2:
    def f1(self):
        print("class 2")
obj1 = c2()
obj1.f1()
obj2 = c1()
obj2.f1()

# & OR
def display(a):
    a.f1()
display(obj1)
display(obj2)
  
# * changing the functionality of builtin functions
a = 9
b = 6
print(a+b)
print(a.__add__(b)) # ---> dunder method or mafic method
int()
print(a.__sub__(b))
print(a.__mul__(b))

class shoping:
    def __init__(self, l1):
        self.items = l1
    def __len__(self):
        length = len(self.items)
        return length
s = shoping([1,2,3,4,5,8])
print(len(s))

# ! ---> method overloading
# ! EXAMPlE:1
class suming:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)
s = suming()
#s.add(4,3) # ! ---> error
s.add(4,5,1)

# ! EXAMPLE:2
class suming:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
obj=suming()
obj.add(2)
obj.add(3,4)
obj.add(1,2,3)

# ! ---> Abstraction
# The process of hiding the implimentation details is abstraction
# ! EXAMPLE:1
from abc import ABC,abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")
class triangle(shapes):
    def triangle_sides(self):
        print("3 sides")
    def name(self):
        print("I am triangle")
    def sides(self):
        pass
class square(shapes):
    def square(self):
        print(" 4 sides")
    def sides(self):
        pass
tr = triangle()
tr.triangle_sides()
tr.name()

# ! Rules to define abstract class 1
# 1) Abstract class cannot be instantiated
# 2) from abc import ABC, abstractmethod
# 3) subclass the normal class with ABC
# 4) convert the normal method inside the abstract class to abstract method
# 5) All the child classes have to be subclassed with abstract class
# 6) The abstract method should be present in the child class

# ! EXAMPLE:2
# * super() ---> used to access the parent class method from child class method
from abc import ABC, abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")

class c2(c1):
    def m2(self):
        super().m1()
        print("Iam child 1")

    def m1(self):
        pass
class2 = c2()
class2.m2()

# ! EXAMPLE:3
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pswd = "savithri@1108"
        return pswd
class login(password):
    def validate(self, name, password):
        if super().pwd() == password:
            print("welcome", name,'!!')
            print("Login Sucessful")
        else:
            print("Please check the password")

    def pwd(self):
        pass

Login = login()
name = input("Enter the name: ")
pwd = input("enter the password: ")
Login.validate(name, pwd)

# ! Encapsuiation
# ! EXAMPLE:1
class car:
    __name = "BMW" # private variable
    print(__name)
c1 = car()
print(c1.name) # error
c1.name = "Audi"
print(c1.name) # error

# ! ---> EXAMPLE:2
# * Accessing private date outside the class
class c1:
    __phone = '2547896317'
    def display(self):
        print(self.__phone)
c = c1()
c.display()

# ! EXAMPLE:3
# ? declare private method
class class1:
    def __m1(self):  # private method
        print("I am private method")
    def __init__(self):
        self.__m1()
c = class1()
c.__m1() # error

# * nested class
class class1:
    class class2:
        name = "savithri"
        def display(self):
            print(self.name)
    obj1 = class2()
obj = class1()
obj.obj1.display()


