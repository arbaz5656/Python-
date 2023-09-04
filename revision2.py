"""
import pyautogui as pg
import time
time.sleep(10)

for i in range(100):
    pg.write('omkar bhadva hai ')
    pg.press('Enter')
"""
"""dictionary={"key":"value","college":"Theem","name":"Arbaz","number":126}
# print(dictionary)
input=input("Enter key: ")
x=dictionary[input]
print(x)"""
"""
print(19%10)
print(22%2)
print(5%3)
print(3**4)
print(5**3)
print(21//2)
print(35//3)
print(15%4)
print(15**4)
print(15//4)"""

"""# 
# one=int(input("ENTER first number:"))
# second=int(input("Enter Second Number:"))
# o=input("Enter operator")
# if o=="+":
#     print(one+second)
# elif o=="-":
#     print(one-second)
# elif o=="*":
#     print(one*second)
# elif o=="/":
#     print(one/second)
# elif o=="%":
#     print(one%second)
# elif o=="**":
#     print(one**second)
# elif o=="//":
#     print(one//second)
# else:
#     print("something is Wrong:")
"""
"""o=1
while o<=11:
    o=o+2
    if o==5:
        continue
    print(o)
"""
"""i=2
while i<20:
    print(i,end=" ")
    i=i+2
    if i==10:
        break
"""
"""
import random
number=random.randint(0,5)
i=1
while (i<=3):
    user=int(input("Enter the number and guess."))
    if user==number:
        print("Right Answer")
        break
    elif user<=number:
        print("you are less ")
    elif user>=number:
        print("you are grater ")
    else:
        print("GAME OVER")
        print("You guesses is fineshed.")
        break
    print(3-i,"left")
    i=i+1

if i>3:
    print("Game")


"""
"""
for i in range(0,10,2):
    print(i)
else:
    print("the number is even")
"""
"""
demo = ["arbaz", "shaikh", 12, 45, 6, 5, 3, 21, 3, "ahmed"]
for x in demo:
    if str(x).isnumeric() and x >= 6:
        print(x)
"""
"""def func(i):
    print(i)
func("arbaz")
"""
"""
def song(*two):
    print("Best raper "+ two[3])
song("Honey singh","Devine","emiway","Raftar")"""


"""def keyatr(one,two):
    print(two)
keyatr(one="arbaz",two="shaikh")"""


"""
def sad(**three):
    print("Best Sad Song "+ three["two"])
sad(one="Arjit singh",two="Atif Aslam",three="darshn rawal")
"""
"""
def retur(w):
    return "Bahot Hard "+ w
print(retur("u"))
fruite=["KELA ","Santra","Nagur"]
def for1():
    for x in fruite:
        print(x)
for1()"""

"""
def func(a,b):
    print("add",a+b)
    print("minus",a-b)
    print("mul",a*b)
    print("div",a/b)
    print("moduleus",a%b )
    print("floor devision",a//b )
    print("Exponention",a**b )

a1=int(input("Enter 1st "))
b1=int(input("Enter 2nd "))
func(a1,b1)

"""

# lambda
x=lambda a:a*5
print(x(5))
def lambd(a):
    print(a*5)
lambd(5)