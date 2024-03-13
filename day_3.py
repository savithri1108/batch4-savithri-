### DAY-3:
'''
# EXAMPLE :3
# take values of length and breadth of a from user and check if it is square or not

len=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
if len==breadth:
   print("its a square")
else:
    print("its not a square")
'''
'''
# EXAMPLE : 4
# Python program to check whether the given integer is a multiple of both 5 and 7

num=int(input("enter the number:"))
if num%5==0 and num%7==0:
    print("yes")
else:
    print("no")
'''
'''
# EXAMPLE : 5
# write a program to accept the cost price of a bike and display the road tax to be paid
# according to the following criteria :
# cost price (in Rs)                 Tax
# > 100000                           15 % + discount 6%
# <= 100000                           5%

price = int(input("enter the price:"))
total = 0
if price>=100000:
    discount = price*(6/100)
    value = price-discount
    tax = value*(15/100)
    total = value+tax
else:
    tax = price*(5/100)
    total = price+tax
print("the on road cost of bike is :",total)
 '''
'''
# ! ---> if elif else
#EX:1
a=7
b=9
c=30
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
elif c>a and c>b:
    print("C is greater")
'''
'''
# A school has following rules for grading system:
# a. BELOW 25 - F
# b. 25 TO 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade

marks=int(input("enter marks:"))
if marks < 25:
    print("F")
elif marks >= 25 and marks < 45:
    print("E")
elif marks >= 45 and marks < 50:
    print("D")
elif marks >= 50 and marks < 60:
    print("C")
elif marks >= 60 and marks < 80:
    print("B")
else:
    print("A")
'''
'''
# ! ---> short hand if else
#EX-1
a = 9
b = 6
if a>b:
  print("A")
else:
   print("B")

# ! ---> using short hand if else
#rules
# 1.)statement inside the if condition have to be present at first
# 2.)elif cannot be used in short hand if else
# 3.)always it have to end with else

print("A") if a>b else print("B")                
'''
'''
# code to check the given char is vowel or consonent

char = input("enter the char:")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
    print("is a vowel")
else:
    print("it is consonent")

## OR
    str1 = "aeiouAEIOU"
    if char in str1:
        print("vowel")
    else:
        print("consonent")


# ! using shorthand if else
char = input("enter the char:")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")
'''
'''
# ! ---> elif ladder using shorthand if else 
# EXAMPLE :1
# ! find greatest among 3 variables using shorthand if else
a=8
b=5
c=9
print("A is greater") if a>b and a>c else print("B is greater") if b>a and b>c else print("c is greater")
'''
'''
# ! ---> LOOPING

# looping can be implimented using
# for loop
# while loop

# ! ---> for loop
# for loop is used for iteration, if we know the number of times the loop have to run.It is used to iterables eg(string, list, tuple, etc...)

# to do ---> syntax for loop

# ! for syntax in c
# for(i=0;i<10;i++)
  {
     printf("hello");
   }  

# ! for syntax in python
# for userdefined_variable in range(start,end,step): default step value is 1
 statement
 statement
 statement
 '''
'''
# EXAMPLE:1
# to  print the value from 1 to 10 using for loop
for i in range (0,10): #(n,n-1)
    print(i)
'''
'''
# EXAMPLE:2
for val in range(1,15,2):
    print(val)
    
for val in range(1,15,3):
    print(val)
for val in range(23,50,4):
    print(val)    
'''
'''
# EXAMPLE :3
# to decrement value
for val in range(10,0,-1):
    print(val)
for val in range(10,0,-4):
    print(val)
'''

# EXAMPLE : 4
# ! print the output of 7 th multiplication table from 21 to 43
'''
# METHOD-1
for val in range(3,10-3):
    print('7','x',val,'=',val*7)
    
# METHOD-2    
for val in range(3,10-3):    
    ans="7 x {} = {}"
    print(ans.format(val,val*7))
    
# METHOD-3   
for val in range(3,10-3):
    print(f"7 x {val} = {val*7}")
 '''
'''
# EXAMPLE : 5
# break ---> used to terminate the loop

for val in range(1,10):
    if val == 6:
        break
    print(val)

# EXAMPLE : 6    
for val in range(1,10):
    print(val)
    if val == 6:
        break
   
# EXAMPLE : 7
for val in range(1,10):
    if val == 6:
        print(val)
        break
'''
'''
# ! CONTINUE
# EXAMPLE:1
for val in range (1,10):
    if val == 6:
        continue
    print(val)
    
# METHOD-2
for val in range(1,30):
    if val == 6 or val == 8 or val == 21:
        continue
    print(val)
'''
'''
# ! PRACTISE PROBLEMS
# ! ---> even numbers from 20 to 40
for val in range (20,41):
    if val % 2 == 0:
       print(val)
'''
'''
# ! ---> WHILE LOOP
# while is used when we do not know the number of times the loop have to run to iterate the non iterate the non iterable elements while loop is used

# to do syntax

# initialisation
# ! --> while condition:
#       statement
#       incre or decre
'''

# ! EXAMPLE :1
# to iterate number from 1 to 10

i=0
while i<11:
    print(i)
    i+=1 # OR I+=1
'''
# ---> Assesment
 1.) cats and mouse:Hacker rank
 2.) Print the factorla of 8 using for loop
 3.) Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

 4.) Write code to print the sum of number using while loop n1 = 123 --> 1+2+3 = 6
 5.) Prine th reverse of given number --> n1= 234 o/p --> 432
'''























    
