# DAY:7

# # ----> Assesment
'''
# 1.) d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Merge two python dictionary
# o/p --> {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


d1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
d2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
d1.update(d2)
print(d1)
'''
'''
# 2.)Python Program to determine if 
# the given Sets Are Disjoint 
# or Not without Using Inbuilt-in Functions

# set1 = {'Python', 'Java', 'Data Science'}
# set2 = {'ML', 'AI', 'R Language', 'Python'}
# set3 = {'Data Analytics', 'Robotics', 'Deep Learning'}

s1 = {'Python', 'Java', 'Data Science'}
s2 = {'ML', 'AI', 'R Language','Python'}
s3 = {'Data Analytics', 'Robotics', 'Deep Learning'}
c=0
flag = 0
for val in range(3):
    c=c+1
    if c==1:
        for val in s1:
            if val in s2 or val in s3:
                flag=1
                break
    if c==2:
        for val in s2:
            if val in s1 or val in s3:
                flag=1
                break

    if c==3:
        for val in s3:
            if val in s1 or val in s2:
                flag=1
                break
if flag==0:
    print("Disjoint")
else:
    print("joint")            
'''
'''
# 3.)list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]

# O/P --> ['My', 'name', 'is', 'Kelly']

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result=[list1[i]+list2[i]
for i in range(len(list1))]
print(result)
# OR
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3 = []
for val in range(len(list1)):
    result=list1[val]+list2[val]
    l3.append(result)
print(l3)
#OR
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
l3=[]
i=0
while i<len(list1):
    l3.append(list1[i]+list2[i])
    i+=1
print(l3)    
'''
# ! ---> functions
# ! ---> DEF
# Function is a block of code which is used to perform a specific functionality
# Function can be created using def keyword

# ! ---> Function has 3 parts
# Function declaration
# Function defination
# Function call

# EXAMPLE:1
def greet():
    print("greetings user !!")
greet() 
greet()    
greet()    
greet() 
greet() 

def greeting(name):
    print("Welcome", name)
for val in range(3):
    username = input("Enter the name: ")
    greeting(username)

# ! EXAMPLE:2
# ! Function with parameter
def greeting(name):
    print("welcome",name)
    for val in range(1):
        username=input("Enter the name:")
        greeting(username)




























































































































































































































            
