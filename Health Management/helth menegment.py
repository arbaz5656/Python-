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
