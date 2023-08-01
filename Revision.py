"""print("\"**Welcome Back Shaikh  Arbaz**\"")
 # b=("\"**Welcome Back Shaikh  Arbaz**\"")"""
# v1="90"
# v2="10"""
# ""print(2*int(v1)+int(v2))
# # print(30*"Arbaz\n")
# k1=int(input("Enter your 1st number:"))
# k2=int(input("Enter your 2nd number:"))
# a=int(input("enter first no:"))
# b=int(input("enter second no:"))
# result=a+b
# a= ("ahmedrazakhan")
# b=("shaikharbaz")
# c=a+b
# print(a.upper())
# print(a.lower())
# print(a[2])
# print(a[3])
# print(len(c))
# print(a+b)
# print(k1+k2)
# print(b[::-1])
# print(b.endswith("Arbaz**\""))
# print(b.upper())
# # print(b.lower())
# # print(b.capitalize())
# # print(b.find("Arbaz"))
# # print(b.split())
# # print(b.count("a"))
# # print(b.strip())
# list=["arbaz","96","11","shaikh"]
# print(list[-1])
dict={"name":"Ahmed","roll":113,"dipartment":"AIML","phone no":9786760990}
v=input("Enter you key: ")
print(dict.get(v))

# print(dict.keys())
# print(dict.values())
# v1=dict.update({"co":"5ia"})
# print(dict)
# dict={"loyal":"imandaar","sad":"dukhi","broken":"toota hua"}
# print(dict)
# i=input("Enter the word: ")
# v=dict.get(i)
# print(v)
# o=dict.fromkeys("ahmed","me")
# print(o)
# set={2, 4, 5, 6 , 8}
# print(type(set))
# w=set.remove(8)
# print(set)
# a=80
# b=80
# if a>b:
#     print("a is greater then b.")
# elif a<b:
#     print("a is less then b.")
# else:
#     print("not ")

# list=[1,3,4,5]
# if 2 in list:
#     print("right")
# else:
    # print("wrong")
# list=["ahmed","arbaz","ishaque","saif"]
# if "usman"in list:
#     print("yes")
# else:
#     print("no")

'''
v1=int(input("Enter your Age: "))
if v1 in range(7,100) and v1>18:
    print("you can get license to drive.")
elif v1==18:
    print("i can not decide.")
elif v1 < 18:
    print("you  cannot drive vehicle.")
else:
    print("Entered invalid age")'''
'''
n1=int(input("1st Number: "))
op=input("enter operater.")
n2=int(input("2nd Number: "))
if op=="+":
    if n1==56 and n2==9:
        print("77")
    else:
        print(n1+n2)
if op=="-":
    print(n1-n2)
if op=="*":
    if n1==45 and n2==3:
        print("135")
    else:
        print(n1*n2)
if op=="/":
    if n1==56 and n2==6:
        print("4")
    else:
        print(n1/n2)'''

# s="Shaikh Arbez"
# s=[["n","name"],["n1","name2"]]
# for i,e in s:
#     print(i,e)
#
# l=["arbaz",2,6,888,"asd",78,890,8]
# for i in l:
#     if str(i).isnumeric() and i>=6:
#         print(i)
#
# o=0
# while o<10:
#     print(o,end=" ")
#     o=o+2
#
# input=int(input("Enter your number:"))
# while input==96:
#     print("your gussing is correct.")
#     break
# else:
#     print("retry")
#
# i=1
# while (i<4):
#     input1 = int(input("Enter your number:"))
#     if input1==96:
#         print("your gussing is correct.")
#     else:
#         print("retry")
# print(2**8)
# print(2%6)
# a=True
# b=False
# print(a and a)
# v=5+7/2
# # print(v)
# def func(fn,ln):
#     print("First name:",fn,"\nSecond name:",ln)
# a1=input("Enter fn  ")
# b1=input("Enter ln ")
# func(a1,b1)
# print(func.__doc__)
# p1=input("1st")
# p2=input("2nd")
# try:
#     print(int(p1)+int(p2))
# except Exception as e:
#     print(e)
# print("Arbaz")
# v=open("Arbaz2.txt","r")
# p=v.write("kl")
# p=v.read()
# print(p)
# print(v.read())
# print(v.write("Shaikh ARBAZ10 AHMED\n"))
# print(v.tell())
# print(v.seek(1))
# print(v.tell())
# print(v.read())
import os
# os.remove("Arbaz1.txt")
# os.remove("Arbaz2.txt")
# v.close()
#
# with open("Arbaz.txt","r") as v:
#     # print(v.write("Shaikh Arbaz Ahmed Akhlaque Ahmed\n"))
#     print(v.read())
#     v.close()
#
"""
# i = input("Enter: ")
# if i.capitalize() == "Arbaz":
#     print("hi")
# else:
#     print("by")
#
# dec = input("Enter your choice: ")
# if dec.capitalize() == "Display":
#     print("r")
# else:
#     print("f")
# """
# def fun():
#     return "hi"
# print(fun())
"""Exercise:5 Health mangement system"""
# print("***** HEALTH MANAGEMENT SYSTEM *****")
"""
f=open("Harry_food.txt","x")
f=open("Harry_exersice.txt","x")
f=open("Rohan_food.txt","x")
f=open("Rohan_exersice.txt","x")
f=open("Hammad_food.txt","x")
f=open("Hammad_exersice.txt","x")
"""
"""
import datetime
def getdate():
    return (datetime.datetime.now())
x=int(input("Press the number you have to following name:\n(1) For Harry\n(2) For Rohan\n(3) For Hammad\n"))
if x==1:
    s=str(input("What do you want Harry food list or exersice list??\n"))
    if s.capitalize() =="Food" :
        y = str(input("What do you want to write or read??\n"))
        if y.capitalize() =="Write":
            print("[", getdate, "]")
            f=open("Harry_food.txt","a")
            print("What you eat:")
            d=input()
            f.write(d)
            print("You have succesfully eneter.")
        elif y.capitalize() =="Read":
            print("[", getdate(), "]")
            f = open("Harry_food.txt")
            r = f.read()
            print(r)
        else:
            print("Invalid,please try again.")
    elif s.capitalize() =="Exersice":
        z = str(input("What do you want to write or read??\n"))
        if z.capitalize() =="Write":
            print("[",getdate(),"]")
            f=open("Harry_exersice.txt","a")
            d=input("What do you do today:")
            f.write(d)
            print("You have succesfully eneter.")
        elif z.capitalize() =="Read":
            print("[",getdate(),"]")
            f=open("Harry_exersice.txt")
            r=f.read()
            print(r)
        else:
            print("invalid,please try again.")
    else:
        print("invalid,please try again.")

elif x==2:
    s=str(input("What do you want Rohan food list or exersice list??\n"))
    if s.capitalize() =="Food":
        y = str(input("What do you want to write or read??\n"))
        if y.capitalize() =="Write":
            print("[", getdate, "]")
            f=open("Rohan_food.txt","a")
            print("What you eat:")
            d=input()
            f.write(d)
            print("You have succesfully eneter.")
        elif y.capitalize() =="Read":
            print("[", getdate(), "]")
            f = open("Rohan_food.txt")
            r = f.read()
            print(r)
        else:
            print("Invalid,please try again.")
    elif s.capitalize() =="Exersice":
        z = str(input("What do you want to write or read??\n"))
        if z.capitalize() =="Write":
            print("[",getdate(),"]")
            f=open("Rohan_exersice.txt","a")
            d=input("What do you do today:")
            f.write(d)
            print("You have succesfully eneter.")
        elif z.capitalize() =="Read":
            print("[",getdate(),"]")
            f=open("Rohan_exersice.txt")
            r=f.read()
            print(r)
        else:
            print("invalid,please try again.")
    else:
        print("invalid,please try again.")


elif x==3:
    s=str(input("What do you want Hammad food list or exersice list??\n"))
    if s.capitalize() =="Food":
        y = str(input("What do you want to write or read??\n"))
        if y.capitalize() =="Write":
            print("[", getdate, "]")
            f=open("Hammad_food.txt","a")
            print("What you eat:")
            d=input()
            f.write(d)
            print("You have succesfully eneter.")
        elif y.capitalize() =="Read":
            print("[", getdate(), "]")
            f = open("Hammad_food.txt")
            r = f.read()
            print(r)
        else:
            print("Invalid,please try again.")
    elif s.capitalize() =="Exersice":
        z = str(input("What do you want to write or read??\n"))
        if z.capitalize() =="Write":
            print("[",getdate(),"]")
            f=open("Hammad_exersice.txt","a")
            d=input("What do you do today:")
            f.write(d)
            print("You have succesfully eneter.")
        elif z.capitalize() =="Read":
            print("[",getdate(),"]")
            f=open("Hammad_exersice.txt")
            r=f.read()
            print(r)
        else:
            print("invalid,please try again.")
    else:
        print("invalid,please try again.")
else:
    print("invalid, Please press the correct number.")
print("THANKS FOR USING:\nBY@SHAIKH ARBAZ AHMED")
    # if x==1:
    #     with open("Harry_food.txt") as f:
    #         x=f.read()
    #         print(x)
"""





"""
No=int(input("Enter the number how many star line you want to print: "))
b=int(input("You want to print star in lower,Enter 0 key or you want to print upper, Enter 1 key.:"))
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
gv=2
def myfunc(fn):
    global gv
    lv=4
    print(gv+lv,fn)
myfunc("Bahot hard")
# print(gv)"""
# o=5!=5*(5-1)
# print(o)
"""
# 0 1 1 2 3 5 8 13
def fi(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fi(n-1)+ fi(n-2)
number = int(input("Enter then number"))
print(fi(number))"""
# import random
# v=random.seed(10)
# print(v)
"""
import time
x=time.asctime(time.localtime(time.time()))
print(x)
input=input("Enter your number ")
i2="2nd"
i3="3rd"
print("my number is %s%s%s"%(input,i2,i3))"""
# import time
# value = time.process_time()
# a=f"{value}"
# print(a)
# d=96
# y="bao%d"% d
# print(y)

# import random
# list=["S","G","W"]
# p_p=0
# u_p=0
# i=0
# while i<3:
#     pc=random.choice(list)
#     print(pc)
#     user=input("Enter your choice \n")
#     if pc==user:
#         print("Tie")
#         print(f"user {u_p} and pc is {p_p}")
#
#     i=i+1
#
"""
def kw(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
kl={"f":"Shaikh","S":"Arbaz","w":"ww"}
kw(**kl)"""
import time
"""t=time.time()
for i in range(2):
    print("Shaikh arbaz")
    print(time.time()-t)
t2=time.time()
i=0
while i<2:
    print("shaikh arbaz")
    print(time.time()-t2)
    i=i+1"""
"""
print(time.asctime(time.localtime(time.time())))
l=["rice","Noodles","Soop","fry"]
i=0
for item in l:
    if i%4 != 0:
        print(f"{item}")
    i=i+1"""
"""
list=["pani","puri","plate","katori","Chainees"]

y=enumerate(list)
print(dict(y))"""
"""import calendar
var=calendar.month(1920,8)
var1=calendar.month(2021,8)
print(var)
print(var1)"""

# import sys
# print(sys.path)
"""
import main
print(main.vars)
# print(main.p)"""
"""
listw=[6]
list1=[2]
listw=list(map(int,listw))
list1=list(map(int,list1))
list1[0]=list1[0]+5
print(list1)
""""""
# filter
list_1=[2,45,6,6,5,7,4,4,81,53]
x=list(filter(lambda a:a>6,list_1))
print(x)
from functools import reduce
listt=[4,5,6]
v=reduce(lambda x,y:x+y,listt)
print(v)
"""


"""
def Der():
    print("Sk")
Der()


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
func3()"""
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
""""""
class post:
    v=7
    def func(self):
        return f"{self.add}. and this  {self.road} p {self.list}"
one=post()
two=post()
one.add="shivaji nager"
one.road=5
two.add="shivaji"
two.road=2
two.list=["muskan","zara","alfiya"]
# print(one.__dict__)
# one.v=8
# print(one.__dict__)
# print(two.__dict__)
print(two.func())"""
"""
class classname:
    def __init__(self,one,two,three):
        self.name=one
        self.add=two
        self.pin=three
variable=classname("shaikh Arbaz","Shivaji nager","400043")
print(variable.__dict__)
def func(*mul):
    print(*mul)
func("Shaikh arbaz","Shivaji nager",400043)
class wtf:
    var=96
obj="98"
print(obj)
"""
"""
class myclass:
    r=96
obj=myclass()
print(obj.r)

# Reduce
from functools import reduce
l=[2,4,6,1]
num=0
for x in l:
    num=num+x
print(num)
# num=reduce(lambda x,y:x+y,l) #Reduse function
# print(num)
""""""
class fuck:
    p=96
    pass
f=fuck()
d=fuck()
f.name="Shaikh"
d.roll="99"
print(f.name,"\n",d.roll)
print(fuck.p)"""
"""
class classname:
    var=100
    def wtf(self):
        return f"This is my name {self.name}.Enrollment is {self.enroll} and Percentage is {self.p}."
first=classname()
second=classname()
first.name="Arbaz"
first.enroll=96
first.p=83.94
second.name="saif"
second.enroll=95
second.p=82.54
print(first.name,second.enroll)
print(first.wtf())
print(second.wtf())
"""
#
# class student():
#     def __init__(self,fname,froll,fp):
#         self.name=fname
#         self.roll=froll
#         self.p=fp
#     @classmethod
#     def alter(cls,string):
#         # third=string.split("-")
#         # print(third)
#         # return cls(third[0],third[1],third[2])
#         return cls(*string.split("-"))  #alternative class method
# first=student("Arbaz",96,78)
# third=student.alter("Arbaz-69-64")
# print(third.roll)
# cap=input("Enter word \n")
# # cap=cap.capitalize()
# if cap=="arbaz":
#     print("same")
# else:
#     print("not same")'''
#