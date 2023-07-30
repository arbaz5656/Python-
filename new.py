"""
a=96
import random
x=random.randint(90,99)
print(x)
import main
print(main.cal(2,2))
"""
"""
list_of_books={"Mathematics":"Sumit","Science":"Available"}
class Library:
    def __init__(self,list_of_book,library_name):
        self.list_of_book=list_of_book
        self.library_name=library_name
    @classmethod
    def display_book(cls,list_of_books):
        print(f"The total no of books in the library is {list_of_books}")
    @classmethod
    def lend_book(cls,list_of_book):
        book_name=input("Enter the name of book you want to take")
        book_name=book_name.capitalize()
        member_name=input("Please enter your name")
        member_name=member_name.capitalize()
        if book_name in list_of_books.keys() and list_of_books[book_name]=="Available":
            print(f"Congrats you have received the book{book_name}")
            list_of_books.update({book_name:member_name})
        elif book_name in list_of_books.keys() and list_of_books[book_name]!="Available":
            print(f"Oops!Sorry the book has been lended to {list_of_books[book_name]}")
        else:
            print("sorry we dont have the book you have requested")

    @classmethod
    def add_book(cls,list_of_book):
        book_name=input("Enter the book you want to donate")
        book_name=book_name.capitalize()
        list_of_books.update({book_name:"Available"})
        print("Successfully added")

    @classmethod
    def return_book(cls,list_of_book):
        book_name=input("Please enter the name of your book")
        book_name=book_name.capitalize()
        list_of_books[book_name]="Available"
        print("Book is succesfully returned")


sumit_library=Library(list_of_books,"My library")
print(f"Welcome to My {sumit_library.library_name}")
print("Type 'display' to view books\nType 'lend' to lend books\nType 'add' to add books\nType 'return' to return books\nType 'quit' to quit library")
while True:
    dec=input("Enter your choice")
    if dec.capitalize()=="Display":
        sumit_library.display_book(list_of_books)
    elif dec.capitalize()=="Lend":
        sumit_library.lend_book(list_of_books)
    elif dec.capitalize() == "Add":
        sumit_library.add_book(list_of_books)
    elif dec.capitalize() == "Return":
        sumit_library.return_book(list_of_books)
    elif dec.capitalize() == "Quit":
        list_of_books=list_of_books
        break
    else:
        print("Wrong input")


"""
"""Song"""

'''
from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("song.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# infinite loop
while True:

    print("Press 'p' to pause, 'r' to resume")
    print("Press 'e' to exit the program")
    query = input(" ")

    if query == 'p':

        # Pausing the music
        mixer.music.pause()
    elif query == 'r':

        # Resuming the music
        mixer.music.unpause()
    elif query == 'e':

        # Stop the mixer
        mixer.music.stop()
        break

'''


print("Welcome Back Arbaz.")
import turtle
colors= ['red','blue','orange','green','white','red','blue','orange','green','white','red','blue','orange','green','white','red','blue','orange','green','white','red','blue','orange','green','white','red','blue','orange','green','white']
t = turtle.Pen()
t.speed(40)
t.pensize(0.1)
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
"""
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
"""