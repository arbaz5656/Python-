"""Exercise:6 Game Devlopment """
import emojis
import emoji
import random
print("snake:",emoji.emojize(':snake:'))
print("water:",emoji.emojize(':sweat_droplets:'))
print("gun  :",emojis.encode(':gun:'))

list=["snake","gun","water"]
user_p=0
pc_p=0
i=1
while (i<=10):
    pc = random.choice(list)
    # print(pc)
    user=input("Your turn,Choose any one!\n")
    if pc==user:
        print("tie")
        print("0 point to each.")
        print(f"pc is {pc_p} and your point is {user_p}.")
    elif user=="gun" and pc=="water":
        pc_p= pc_p+1
        print("You lose,pc is win.")
        print(f"The gun will drown in water,hence a point is {pc}:")
        print(f"pc is {pc_p} and your point is {user_p}")
    elif user=="gun" and pc=="snake":
        user_p=user_p+1
        print("You Win,pc is lose")
        print(f"Gun will kill the snake,hence a point is {user}")
        print(f"pc is {pc_p} and your point is {user_p}")
    elif user == "snake" and pc == "water":
        user_p=user_p+1
        print("You Win,pc is lose")
        print(f"Snake drinks the water,hence a point is {user} ")
        print(f"pc is {pc_p} and your point is {user_p}")
    elif user == "snake" and pc == "gun":
        pc_p=pc_p+1
        print("You lose,pc is win")
        print(f"Gun will kill the snake,hence a point is {pc}")
        print(f"pc is {pc_p} and your point is {user_p}")
    elif user == "water" and pc == "snake":
        pc_p=pc_p+1
        print("You lose,pc is win")
        print(f"Snake drinks the water,hence a point is {pc}")
        print(f"pc is {pc_p} and your point is {user_p}")
    elif user == "water" and pc == "gun":
        user_p=user_p+1
        print("You Win,pc is lose")
        print(f"The gun will drown in water,hence a point is {user}")
        print(f"pc is {pc_p} and your point is {user_p}")
    else:
        print("Spelling Mistake,Check your spelling:")
        print(f"pc is {pc_p} and your point is {user_p}")
        print(i, "no.of guesses you finish.")
    print(10-i, "no. of guesses left.\n")

    i=i+1
if (i>10):
    print("Game over")

if pc_p == user_p:
    print("Tie")

elif pc_p > user_p:
    print("Computer wins and you loose")

else:
    print("Wooho,you win and computer loose")

print(f"your point is {user_p} and computer point is {pc_p}")




