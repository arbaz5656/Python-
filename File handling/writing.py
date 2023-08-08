# f=open("Arbaz.txt","rt")
# print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.read())
# for x in f:
#     print(len(x))
# #     print(x.strip())
# f.close()
# #
# f=open("Arbaz2.txt","w")
# f.write("\nThis is a new line add 2")
# f.close()
# f=open("Arbaz2.txt","r")
# print(f.read())
# f.close()
# f=open("Arbaz.txt","a")
# f.write("the new line!")
# f.close()
# import os
# os.remove("Arbaz2.txt")
"""x=int(input("Enter no:"))
# i=0
# while i<x:
#     print("*")
# i=i+1
for i in range(x,0,-1):
    print("*"*i)"""
#
# f=open("Arbaz.txt","a")
# x=f.write("\nArbaz is very honest boy:")
# print(x)
# f.close()
# f=open("Arbaz.txt","r")
# print(f.read())

"""f=open("Arbaz.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
print(f.seek(6))
# print(f.readline())
print(f.tell())
f.close()
"""
# num=int(input("enter you have wright"))
# with open("Arbaz.txt") as f:
#     x=f.read()
#     print(x)

"""
# f=open("Arbaz.txt","w")
# print(f.write("Arbaz is verey nice boy"))
y = input("What do you want to write or read??\n")
if y=="Read" or y=="read":
    f=open("Arbaz.txt","a")
    print(f.write(" bahot hard"))
elif y=="write" or y=="Write":
    f=open("Arbaz.txt")
    x=f.read()
    print(x)
"""


# import os
# os.remove("Hammad_exercise.txt")
"""
f=open("Harry_exercies.txt","rt")
x=(f.read())
print(x)
# print("[",getdate(),"]")
f=open("Harry_food.txt")
r=f.read()
print(r)
# y = input("What do you want to write or read??\n")

"""
"""
import emojis
# emoji = emojis.encode(':sweat_droplets:')
# print(emoji)
emoji = emojis.encode(':gun:')
print("Gun",emoji)
emoji = emojis.encode(':snake:')
print("Snake",emoji)
import emoji
print("Water",emoji.emojize(':sweat_droplets:'))
#
import random
list=["Snake","Gun","Water"]
x=random.choice(list)
y=str(input("Enter your choice:"))
if x==y:
    print("same")
else:
    print("difrent")
"""
# iv= "asdf"
p=input()
print("\n",p)