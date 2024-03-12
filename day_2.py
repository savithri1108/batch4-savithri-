

#***DAY-2:
  
# -----> SWAPPING OF VARIABLES
#EX:1
a=7
b=5
temp=a #temp=7
a=b #a=5
b=temp #b=7
#print(a,b)

#EX:2
a=a+b #a=5+7=12
b=a-b #b=12-7=5
a=a-b #a=12-5=7
#print(a,b) 

#EX:3 
a=a*b #a=35
b=a/b #b=35/7=5.0
a=a/b #a=35/5=7.0
#print(int(a),int(b))


#id() --> used to find the memory address of the variable
a=7
b=8
#print(id(a))
#print(id(b))

#----> KEYWORDS
# keywords are reserved words which provides special meaning to compiler or interpretor
import keyword
#print(keyword.kwlist)
#print(len(keyword.kwlist))
#print(type(keyword.kwlist))

# to check if the string is keyword or not
#print(keyword.iskeyword("sid")) #false

# ! ----> LITERALS
# Literal is the constant value assigned to a variable
# A Variable is considers to be constant when it is defines in caps
a=78 # a is variable
A=78 # A is constant

# hash() --> it creates a hash value for constant datatypes and provides error for non constant datatypes
n1=89+7j
#print(hash(n1))
#f1=[7,8,9]
#print(hash(f1))
a=9
b=9
b=90
#print(id(a))
#print(id(b))

# ! ---> operators
# operators are symbols which is used to perform various operations between 2 or more operands
# arithmatic
# assignment
# logical
# relational or comparision
# bitwise
# identity
# membership

# to do ---> arithmatic --> =,-,*,?,%,//,**
#EX:1
a=8
b=6
c=9
#print(a+b+c)

# input() ---> used to get the runtime input
#eval() ---> used to get the runtime values of all data type
#n1=eval(input("enter the value: "))
#print(type(n1))

a=4
b=2
#print(a/b) # is used to get the quotient
#print(a%b) # is used to get the remainder

# ! // ---> floor division
a=765433
b=19
#print(a//b) # -> the output will be inn integer & the output will be based on floor value

# ! ** ---> used for power of a number
#print(2**4)

# ! assignment ---> =,+=,-=,/=,*=,//=,**=,&=,|=
a=8
a+=2
#print(a)
a=30
a-=5
#print(a)

# ! comparision ---> ==,>,<,!=,<=,>=
a=8
b=7
#print(a>b)
a=9
b=5
#print(a==b)

# ! bitwise operator ---> &,|,^,~,<<,>>
a=7
b=6
#print(a|b)

# 2^4 2^3 2^2 2^1 2^0
#  8   4   2    1   0
#  0    1   1   1   # ---> 7
#  0   1    1   0   # ---> 6 &
#  ----------------
#  0    1    1  1   # ---> 7


# ! logical
# and, or, not
a=6
#print(a>3 and a<10)
#print(a>7 or a<30)
#print(not(a>8 and a<10))

# ! identity operator ---> is,is not
# it is used to compare the memory location that the values are stored
a=8
b=8
#print(a is not b)
#print(a==b)

a=[1,2,3]
b=[1,2,3]
#print(a is not b)

# ! membership operator ---> in,not in
l1=[7,8,9,0,6,5]
num=55
#print(num in l1)
#print(num not in l1)
num=678
# print(8 in num) # error

# ! CONDITIONAL STATEMENT
# if, elif,else

# EXAMPLE
# ---> C SYNTAX
# if (condition){
#    statement;
#    statement;
#    statement;
 #  }
# ---> PYTHON SYNTAX
# if condition :
 #    statement
#    statement
#    statement

# EX:1
a=6
if a:
#    print("hello")
# EX:2
a=6
if a>3:
#    print("yes")
else:
#    print("no")
    
# EX:3
if 7>8:
 #   print("hello")
else:
#   print("no")

# EX:4
a=0
a=None
a=False
a=""
if a:
 #   print("yes")
else:
 #   print("no")

# EX:5

# a number is even or odd
num = int(input("enter a number"))
if num%2==0:
    print(num,"even")
else:
    print(num,"odd")
    


























































































































