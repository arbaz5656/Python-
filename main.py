'''
x=int(input("Enter your first no: "))
print("1st no: ",x)
y=int(input("Enter your second no:"))
print("2st no: ",y)
print("Total no.: ",x+y)
'''
from abc import abstractmethod, ABCMeta

"""String"""
"""
x=("Helloworld!")
print(len(x))
print(x[0:6])
print(x[0:12:2])
print(x.isprintable())
print(type(x))
"""

"""LIST"""
"""
list=["Shaikh","Arbaz","Ahmed"]
print(len(list))
list1=["Shaikh",98,True]
print(list1)
print(list1[0])
print(type(list1))
"""

"""tuple"""
"""
x=("arbaz","asdf","ksjks")
print(x)
y=x.index("asdf")
print(y)
f=()
print(type(f))
"""

"""Exercise:1 Apni dictionery"""
"""
dict={"name":"earaf","roll":78,"class":"commerce","college":"ambedkar"}
print(dict)
x=input("enter the key: ")
print(x)
print("Result: ",dict[x])
print("Result: ",dict.get(x))
"""
"""MOdules oprator (%)"""
"""
print(19%10)
print(22%2)
print(5%3)
"""
"""Exponentition (**)"""
"""
print(3**4)
print(5**3)
print(2**5)"""

"""Floor division(//)"""
"""
print(3//2)
print(21//2)
print(35//3)
"""





"""
x=int(input("Enter your age: "))
if x in range(7,100) and 18<x:
    print("yes,you can drive the car")
elif 18==x:
    print("Oops, i can't deside. sorry")
elif 100<x:
    print("invalid age")
else:
    print("No, you can't drive the car")
"""


"""Exercise:2 Faulty calculater"""
"""
x=input("Enter the oparetar:'+','*','/','-' :")
print("OPERATAR",x)
y=int(input("Enter 1st no."))
z=int(input("Enter 2nd no."))
if x=="+":
    if y==56 and z==9:
        print("77")
    else:
        print(y+z)
if x=="*":
    if y==43 and z==3:
        print("555")
    else:
        print(y*z)
if x=="/":
    if y==56 and z==6:
        print("4")
    else:
        print(y/z)
if x=="-":
    print(y-z)
"""
"""
x=input("Enter the oparetar:'+','*','/','-' :")
print("OPERATAR",x)
y=int(input("Enter 1st no."))
z=int(input("Enter 2nd no."))
if x=="+":
    print(y+z)
elif x=="*":
    print(y*z)
elif x=="/":
    print(y/z)
elif x=="-":
    print(y-z)
else:
    print("invalid,Pleace try again use correct operater")
"""

"""Odd numer Using for Loop"""
"""
for i in range(1,10,2):
    print(i)
"""

"""Even numer Using for Loop"""
"""
for i in range(0,10,2):
    print(i)
"""




"""
demo=["arbaz","shaikh",12,45,6,5,3,21,3,"ahmed"]
for x in demo:
    if str(x).isnumeric() and x>=6:
        print(x)
"""



"""EVEN WHILW USING """
"""i=2
while i<20:
    print(i)
    i=i+2
"""
"""oDD WHILE USING"""
"""
i=1
while i<20:
    print(i)
    i=i+2
"""

"""
i=0
while True:
    print(i,end=" ")
    if i==10:
        break
    i =i+2
"""
"""
num=int(input("Enter the numbers: "))
while num>=100:
    print("congretulation")
    break
else:
    print("enter the 100 above no.")

while(True):
    x=int(input("Enter the no."))
    if x>100:
        print("congratuletion")
        break
    else:
        print("Re-try")
        continue
"""
# SHOrt Hand if else
"""
i1=int(input("Enter the 1st numer:"))
i2=int(input("Enter the 2nd numer:"))
# if i1>i2: print("1st number is greter then 2nd number")
print("1st number is greter then 2nd number") if i1>i2 else print("1st number is less then 2nd number")
"""
"""Exercise:3 Guess the number"""
"""
Number=96
i=1
while(i<=5):
    user = int(input("Guess the no. between 90 to 99:"))
    if user==96:
        print("woo hoo!,congrates you have win")
        break
    elif user<=96:
        print("no you have close, try again")
    elif user>=96:
        print("no,You have moved on.try again")
    else:
        print("Game Over")
        print(i, "no.of guesses you finish.")
        break
    print(5-i, "no. of guesses left")
    i=i+1

if (i>5):
    print("Game over")
"""
"""
# Using Random
import random
Number=random.randint(90,99)
i=1
while(i<=5):
    user = int(input("Guess the no. between 90 to 99:"))
    if user==Number:
        print("woo hoo!,congrates you have win")
        break
    elif user<=Number:
        print("no you have close, try again")
    elif user>=Number:
        print("no,You have moved on.try again")
    else:
        # print("Game Over")
        # print(i, "no.of guesses you finish.")
        break
    print(5-i, "no. of guesses left")
    i=i+1

if (i>5):
    print("Game over")
"""
'''lambda'''
"""
# lambda
x=lambda a:a*5
print(x(5))
# function
def lambd(a):
    print(a*5)
lambd(5)"""


'''
def my_function(a,b):
    print("My first function\n", a+b)
my_function(9,6)

def second(x,y):
    """The average calculation"""
    avrg=(x+y)/2
    return avrg
d=second(7,9)
print(d)
print(second.__doc__) #doc string


def func(a,b):
    print("add",a+b)
    print("minus",a-b)
    print("mul",a*b)
    print("div",a/b)
a1=int(input("Enter 1st "))
b1=int(input("Enter 2nd "))
func(a1,b1)


def my_self(fname,lname):
    print("Full name:",fname,lname)
my_self("Shaikh","Arbaz")
'''
'''
x=input("entre the no1.")
y=input("entre the no2.")

try:
    print("Sum of number",int(x)+int(y))
except Exception as e:
    print(e)
print("asdf")
'''
# Doc String

# def func1():
#     '''Question of the day'''
#     print("My name is Arbaz")
# func1()
# print(func1.__doc__)
"""Exercise:4 Astrologers stars"""
"""
No=int(input("Enter the number how many star line you want to print: "))
b=int(input("Enter 0 or 1 no.:"))
x=(bool(b))
print(x)
i=0
if x==True:
    while i<No:
        print("*"*(i+1))
        i=i+1
elif x==False:
    while i<No:
        print("*"*(No))
        No=No-1
"""
"""
a=96 #Global variable
def func1(x):
    # a=95 #local variable
    b=100
    global a #Global keyword
    a=a+2
    print(a,b)
    print(x,"My age is 19:")
func1("my name is Arbaz,")
print(a)
"""
# try me
"""
z=96
def func2():
    z=12
    def func
    3():
        # global z
        z=24
    # print(z)
    func3()
    print(z)
func2()
print(z)
"""
# Factorial no
# Recursion
"""
def facto(n):
    if n==1:
        return 1
    else:
        return n *facto(n-1)
def facto1(n):
    fac=1
    for x in range(n):
        fac=fac*(x+1)
    return fac
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
num=int(input("Enter the number: "))
print("Recuarsive:")
print(facto(num))
print("Iterative:")
print(facto1(num))
print("Fibonacci No:")
print(fibonacci(num))
"""
#Harry code:
"""# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
def factorial_iterative(n):
    '''
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    '''
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    '''
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    '''
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120

# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


number = int(input("Enter then number"))
# print("Factorial Using Iterative Method", factorial_iterative(number))
# print("Factorial Using Recursive Method", factorial_recursive(number))
print(fibonacci(number))
  
"""
# def minus(x,y):
    # return x-y
# minus=lambda x,y:x-y
# print(minus(11,3))
# def a_first(a):
#     return a[1]
# a=[[1,7],[4,1],[54,98]]
# a.sort(key=lambda x:x[1])
# a.sort(key=a_first)
# print(a)

"""-"""
# import random
# x=random.random()
# x=random.randint(1,10)
# list=["shaikh","Arbaz","Ahmed","Akhlaque","AHMED"]
# x=random.choice(list)
# random.seed(10)
# print(random.random())
# x=random.randrange(1,23)
# print(x)
#Current time
"""
import time
x=time.asctime(time.localtime(time.time()))
print(x)
#calender 2020
import calendar
y=calendar.month(2020,11)
print(y)
import datetime
z=datetime.datetime.now()
print(z)
"""
"""
you=" bahot"
me=" hard"
a=" hai"
d= 96

x="Arbaz%s%s%s"%(you,me,a)
print(x)
import time
value = time.process_time()
a=f"{x} {value}"
print(a)
# y="bao%d"% d
# print(y)
"""
#41
# *args
"""Arbitrary Arguments"""
"""
def four(*all):
    # print(type(all))
    print(all)
    # for x in all:
        # print(x)
list=("bahot","hard","arbaz")
(four(*list))
"""
"""
def bout(*name):
    print(f"MY name is {name[0]}:")
bout("Arbaz","shaikh")
"""
"""
#**kwargs
def my_func(**byy):
    for key,value in byy.items():
        print(f"{key} {value}")
kw={"Engineer":"Arbaz","Arman":"student"}
my_func(**kw)
"""
"""
def func(**bhai):
    print("My brothers is "+bhai["first"])
# func(first="shahnwaz",second="shahbaz")
a={"first":"shahnwaz","second":"shahbaz"}
func(**a)
"""
# 42
import time
# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)
print(time.asctime(time.localtime(time.time())))
p=9
if __name__ == '__main__':
    vars=time.asctime(time.localtime(time.time()))
"""import calendar
var=calendar.month(1920,8)
var1=calendar.month(2021,8)
print(var)
print(var1)
"""
"""
cal=time.time()
i=0
while i<10:
    print("Arbaz")
    time.sleep(2)
    i=i+1
print("ran time",time.time() - cal,"second")
cal2=time.time()
for x in range(10):
    print("Shaikh")
print("ran time",time.time() - cal2,"second")
"""

# list=["pani","puri","plate","katori"]
# i=1
# for x in list:
#     if i%2!=0:
#         print(f"buy {x}")
#     i=i+1
# for index,x in enumerate(list):
#     if index%2==0:
#         print(f"buy {x}")
# y=enumerate(list)
# print(tuple(y))

# 45
"""
# How to import works in python

import sys
print(sys.path)
import new
print(new.a)
"""
# 46
# if__name==main__usage
"""
def main1(par):
    return f"{par} is very claver boy."
def cal(no1,no2):
    return no1+no2+7
print("The name is ", __name__)
if __name__ == '__main__':
    print(main1("Arbaz"))
    x=cal(9,9)
    print(x)
"""
# 47
# join Function
"""
list=["king xi punjab","Shami","rahul","gayle","mayank","jordan"]
x= " ,legend ".join(list)
print("yesterday match Heroes:",x)
"""
# 48
# map,filter,reduse
# number=["1","78","64","95"]
# for i in range(len(number)):
    # number[i]=int(number[i])
# number=list(map(int,number)) #map function
# print(number)
# number[3]=number[3]+1
# print(number[3])
"""
op=[3,5,6,3,6,7,8,89]
def squre(x):
    return x*x
def cube(x):
    return x*x*x
y=list(map(squre,op))
k=list(map(cube,op))
y=list(map(lambda x:x*x,op))#using lambda
print(y)
"""
"""
def squre(x):
    return x*x
def cube(x):
    return x*x*x
func=[squre,cube]
for i in range(5):
    k=list(map(lambda x:x(i),func))
    print(k)
"""
"""
# filter
list_1=[2,45,6,6,7,4,4,81,5]
x=list(filter(lambda a:a>6,list_1))
print(x)
"""
"""
# Reduce
from functools import reduce
l=[2,4,6,1]
# num=0
# for x in l:
#     num=num+x
# print(num)
num=reduce(lambda x,y:x+y,l) #Reduse function
print(num)
"""
# 51
"""
# decorators
def func1(arg):
    def func2():
        print("print1")
        arg()
        print("print2")
    return func2
@func1
def func3():
    print("new print3")
# func3=func1(func3)
func3()
"""
# 53

"""Class"""
"""
class classname:
    var=100
    pass
first=classname()
second=classname()
first.name="Arbaz"
first.enroll=96
first.p=78
second.name="saif"
second.enroll=95
second.p=71
print(first.name,second.enroll)
"""
"""
# 54
print(classname.var)
print(first.var)
classname.var=102
print(classname.var)
second.var=103
print(second.var)
print(second.__dict__)
print(first.__dict__)
"""
# 55
"""Self"""
"""
class classname:
    var=100
    def wtf(self):
        return f"This is my name {self.name}.Enrollment is {self.enroll} and Percentage is {self.p}."
first=classname()
second=classname()
first.name="Arbaz"
first.enroll=96
first.p=78
second.name="saif"
second.enroll=95
second.p=71
print(first.name,second.enroll)
print(first.wtf())
print(second.wtf())
"""

"""__init__(Constroctor)"""

"""class student():
    def __init__(self,fname,froll,fp):
        self.name=fname
        self.roll=froll
        self.p=fp
first=student("Arbaz",96,78)
second=student("Saif",95,82.54)
print(second.p)
"""
# 56
"""Class method"""
"""
class Employee:
    no_of_leaves=96
    @classmethod
    def hard(cls,leaves):
        cls.no_of_leaves=leaves
first=Employee()
second=Employee()
second.hard(78)
# Employee.no_of_leaves=78
print(Employee.no_of_leaves)
"""
# 57
"""Alternative constructor"""
"""
class student():
    def __init__(self,fname,froll,fp):
        self.name=fname
        self.roll=froll
        self.p=fp
    @classmethod
    def alter(cls,string):
        # third=string.split("-")
        # print(third)
        # return cls(third[0],third[1],third[2])
        return cls(*string.split("-"))  #alternative class method
first=student("Arbaz",96,78)
third=student.alter("Arbaz-69-64")
print(third.roll)
"""
"""Harry code"""
"""
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_dash(cls,string):
          return cls(*string.split("-"))

date1=Date.from_dash("2008-12-5")
print(date1.year)
#Output: 2008
"""
"""
def func():
    print("Shaikh")
print(func())
"""
# 58
"""Static Method"""
"""
class Teacher:
    # def __init__(self,name):
        # self.oname=name
    @staticmethod
    def sub(String):
        print("Teaching the subject"+String)
object=Teacher()
Teacher.sub(" Python.")
"""
# 60
"""Single inheritance"""
"""
class base:
    def __init__(self,head,nose,hand):
        self.Head=head
        self.Nose=nose
        self.Hand=hand
    def first(self):
        return f"The prents {self.Head},{self.Nose},{self.Hand}."
class drive(base):
    def __init__(self,head,nose,hand,leg):
        self.Head=head
        self.Nose=nose
        self.Hand=hand
        self.Leg=leg

    def second(self):
        return f"The prents {self.Head},{self.Nose},{self.Hand},{self.Leg}."
object=base("one","One","two")
object1=drive("three ","four ","five ","six ")
print(object1.second())
# print(object.first())
"""

# 61
"""Maltipal inheritance"""
"""
class Class1:
    var=1
    def __init__(self,name,stand):
        self.Name=name
        self.Stand=stand
    def first(self):
        return f"class {self.Name} is {self.Stand}."
class Class2:
    var=2
    def __init__(self,name,stand,line):
        self.Name=name
        self.Stand=stand
        self.Line=line
    def second(self):
        return f"class {self.Name} is {self.Stand},{self.Line}."
class Class3(Class1,Class2):
    # var = 3
    def third(self):
        print(self.var)
object1=Class1("Shaikh","one")
object2=Class2("Arbaz","Two","straight")
object3=Class3("Ahmed","Three")
print(object1.first())
print(object2.second())
print(object3.first())
print(Class3.var)
"""
# 62
"""Multilevel inheritance"""
"""
class Electronic:
    value1="***" #public
    def device(self):
        return f"The electronic device selling reating is {self.value1}."
class Pocket(Electronic):
    _value2 = "****" #protected
    def gadget(self):
        return f"The pocket gadget selling reating is {self._value2}."
class Phone(Pocket):
    __value3 = "*****" #private
    def mobile(self):
        return f"Woo hoo! The phone selling reating is {self.__value3} "
shikh=Electronic()
Arbaz=Pocket()
Ahmed=Phone()
print(Ahmed.device())
print(Ahmed.gadget())
print(Ahmed.mobile())
"""
# 63
"""
class Normal:
    public=1
    _protected=2
    __private=3
object=Normal()
print(object._Normal__private)
"""
# 67
"""operator overloding"""
"""
class Operator:
    def __init__(self,member,emp,sallery):
        self.Member=member
        self.Emp=emp
        self.Sallery=sallery
    def __mul__(self, other):
        return self.Sallery*other.Sallery
    def __eq__(self, other):
        return self.Emp==other.Emp
    def __ne__(self, other):
        return self.Member!=other.Member

object=Operator(19,5,150000)
object1=Operator(5,1,100000)
print(object * object1)
print(object==object1)
print(object!=object1)
"""
# 70
"""introseption"""
"""
# print(type(object1))
print(id(object))
print(dir(object))
import inspect
print(inspect.getmembers(object))
"""
# 72
"""Generators"""
"""
def func(x):
    for i in range(x):
        yield i
z=func(4)
print(z.__next__())
print(z.__next__())
print(z.__next__())
print(z.__next__())
def facto(n):
    x=1
    for i in range(n):
        x=x*(i+1)
    yield x
num=int(input("Enter the facto number"))
print(facto(num))

"""
# 73
""" Comprehensions"""
"""
ls=[x for x in range(1,33) if x%3==0]
# print(ls)
dict={i:f"Item {i}" for i in range(50) if i%5==0}
# print(dict)
evens = (i for i in range(100) if i%2==0)
# print(evens)
"""
# 74
"""Else with for loop"""
"""
list=["phone","tv","bike","mobile","laptop"]
for x in list:
    print(x,end=",")
    break
else:
    print("no,this is not available")
"""
# 75
"""Function Caching"""
"""
import time
from functools import lru_cache
@lru_cache(maxsize=int(input("Enter the runtime:")))
def func():
    time.sleep(5)
if __name__ == '__main__':
    print("Shaikh Arbaz")
func()
print("Ahmed")
func()
print("Shaikh Family")
"""
# 76
"Else And Finally"
"""
try:
    print(Shaikh)
except Exception as x:
    print(x)
else:
    print("No error through:")
finally:
    print("Run compulsory this line.")
"""
# 77
"""coroutines"""
"""
def cricket_team():
    import time
    player = ["Arbaz","Shahbaz","Shahnwaz","Arman","Shahid","Baba"]
    time.sleep(2)

    while True:
        text = (yield)
        if text in player:
            print("Your name is in the team.")
        else:
            print("Sorry,Your name is not in the team.")

object =cricket_team()
next(object)
user=input("Check you are selected or not in team: ")
user=user.capitalize()
object.send(user)
object.close()
"""

class Shape(metaclass=ABCMeta):
    def __init__(self):
        print("I am in init")
    @abstractmethod
    def draw_shape(self):
        pass

    @abstractmethod
    def set_color(self):
        pass
class Circle(Shape):
    def draw_shape(self):
        print("Draw Circile")
