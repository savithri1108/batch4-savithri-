# DAY-8

# 1.) Write a Python script to generate and print a dictionary that  contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

n=int(input("enter the number"))
d=dict()
for x in range(1,n+1):
    d[x] = x * x
print(d)

# 2.)Find the uncommon words from 2 strings
# s1 = "Hello how are you"
# s2 = "Hello how is"

s1="Hello how are you"
s2="hello how is"
def uncommonwords(s1,s2):
    s1=s1.split()
    s2=s2.split()
    x=[]
    for i in s1:
        if i not in s2:
            x.append(i)
    for i in s2:
        if i not in s1:
            x.append(i)
    x=list(set(x))
    return x
print(uncommonwords(s1,s2))

# ! EXAMPLE:3
def profile(name, age, place):
    txt="My name is {}. I am {} years old. I am from {}."
    print(txt.format(name, age, place))
profile("savithri",21, "kadapa")    


# ! ---> return
# ! return
#1.) A variable declared inside the function can be accessed outside the function using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement

# EXAMPLE:4
def f1():
    z=8
f1()
print(z) # error ---> cannot use outside the function

def f1(a,b):
    c=a*b
    return c
print(f1(6,8))
obj=f1(6,8)
obj1=f1(4,6)
def gracemark(object):
    print(object+4)
gracemark(obj)
gracemark(obj1)

# 123
def palindrome(s):
    return s == s[::-1]
s="123"
ans=palindrome(s)
if ans:
    print("palindrome")
else:
    print("not palindrome")
    
# ! PROBLEM:1
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n,"palindrome")
    else:
        print("not palindrome")
a=int(input("enter the value: "))
palindrome(a)

# !---> Based on the declaration of parameter and args functions are divided into 5 categories
# positional args
# keyword args
# default args
# variable length args
# keyword variable length args

# * positional args
# ? the position of parameter have to be same as position or arguments
# ! EXAMPLE :1
def profile(name,phone,mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name, phone, mark))
profile(8065429107,"savithri",95) # unexpected output

# * keyword args
# ! EXAMPLE:1
# ? to overcome the disadvantages of position args, we use keyword args
# ? It is the process of intialising the parameter with the args while calling the function

# funtions
def profile(name,phone,mark):
    txt="My name is {}. My phone number {}. I got {} marks."
    print(txt.format(name, phone, mark))
profile(name="savithri", mark=95, phone=5672389021)

# todo ---> Exception of  keyword args function
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name, phone, mark))
#profile(name="savithri", 5672389021 ,mark=95) # error ---> positional args follow keyword arg
#profile(5672389021, name="savithri", mark=95) # error ---> names has multiple values
profile("savithri", mark=95, phone=5672389021)

# * Default args
# ? the method of assigning the argument to the parameter while declaring the function
# ! EXAMPLE :1
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
    if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
         txt="My name is {}. My phone number {}. I am from {} ."
         print(txt.format(name,phone,place))
    else:
         print("You are not eligible to Signup")
profile("Savithri",9876543210)

# * variable length params
# ! EXAMPLE:1
# ? To pass more then 1 arg to a parameter means we use variable length args
# To convert parameter to variable length param, add * to their prefix of parameter

#name="savithri", "pavithra ", 'name3'
def profile(*name):
    for val in name:
        print(" My name is",val)
profile("savithri", 'pavithra', 'name3')

# ! EXAMPLE:2
def profile(*name, age):
    for val in name:
        print("My name is",val, "may age is", age)
#profile("savithri", 'name2', 'name3', 20) # error ---> age has no args
def profile(age, *name):
    for val in name:
        print("My name is",val, "may age is", age)
profile(20, "savithri",'name2', 'name3')


# * keyword variable length args
# kwargs ---> which is used to provide the args in the form of key value pair
# ! EXAMPLE:1
def price(**price_list):
    print(price_list)
price(shirt=1000, iphone=80000)


d1={"a":100, "b":200, "c":300}
d1=dict(a=100, b=200, c=300)
print(d1)


n=int(input("enter the number"))
d1={}
for val in range(1,n+1):
    d1[val] = val**2
print(d1)
    
def dict(n):
    d1={}
    for val in range(1,n+1):
        d1[val]=val**2
    print(d1)    
dict(5)    


# ! ----> object oriented programming
# The panadigms of objects oriented progarmming are

# class
# objects
# inheritance
# polymorphism
# abstraction
# encapsulation

# ! EXAMPLE:1
class c1:
    name1 = "savithri"
    print(name1)
    
# ! EXAMPLE:2
class person:
    name = "savithri"
c = person() # c as object
# the process of creation of an object is called as Instantiation
print(c.name)

# ! EXAMPLE:3
# create of a method
# when the function is created with a class is called as method
class person:
    def display(person): # It is a method
        print("hello welcome to classes")
p=person()
p.display()

# ! EXAMPLE:4
# ? method with parameter
class person:
    def display(person, name, age):
        print(name, age)
p=person()
p.display("savithri",20)

# ! EXAMPLE:5
class person:
    name = "savithri" # attribute or static variable
    def display(person):
        print(person.name)
p=person()        
p.display()    

# ! EXAMPLE:6
class person1:
    fname = "savithri" # attribute or static variable
    lname = "p"
    def first_name(self):
        print(self.fname)
    def full_name(self):
        print(self.fname+" "+self.lname)
p=person1()
p.first_name()
p.full_name()

# ! EXAMPLE:7
# constructors ---> __init__()
# This is a special method which has the ability to execute itself without
#calling it manullay through the process of instantiation

class profile:
#    def_init_(self): # constructor method
        print("hello")
p=profile() # execution of constructor throught this process        
