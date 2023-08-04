"""The Library Management System"""
"""Mini project"""
all_books={"Mathematics":"Arbaz","Science":"Available"}
class Library:
    def __init__(self,all_book,library_name):
        self.all_book=all_book
        self.library_name=library_name
    @classmethod
    def display_book(cls,all_books):
        print(f"The total no of books in the library is {all_books}.")
    @classmethod
    def lend_book(cls,all_book):
        book_name=input("Enter the name of book you want to take.")
        book_name=book_name.capitalize()
        user_name=input("Please enter your name:")
        user_name=user_name.capitalize()
        if book_name in all_books.keys() and all_books[book_name]=="Available":
            print(f"Congrats you have received the book{book_name}")
            all_books.update({book_name:user_name})
        elif book_name in all_books.keys() and all_books[book_name]!="Available":
            print(f"Oops!Sorry the book has been lended to {all_books[book_name]}:")
        else:
            print("sorry we dont have the book you have requested.")

    @classmethod
    def add_book(cls,all_book):
        book_name=input("Enter the book you want to donate :")
        book_name=book_name.capitalize()
        all_books.update({book_name:"Available"})
        print("Successfully added")

    @classmethod
    def return_book(cls,all_book):
        book_name=input("Please enter the name of your book:")
        book_name=book_name.capitalize()
        all_books[book_name]="Available"
        print("Book is succesfully returned")


My_library=Library(all_books,"'The Next Page'")
print(f"Welcome to  {My_library.library_name} Library")
print("Type 'display' to view books.\nType 'lend' to lend books.\nType 'add' to add books.\nType 'return' to return books.\nType 'quit' to quit library.")
while True:
    dec=input("Enter your choice: ")
    if dec.capitalize()=="Display":
        My_library.display_book(all_books)
    elif dec.capitalize()=="Lend":
        My_library.lend_book(all_books)
    elif dec.capitalize() == "Add":
        My_library.add_book(all_books)
    elif dec.capitalize() == "Return":
        My_library.return_book(all_books)
    elif dec.capitalize() == "Quit":
        all_books=all_books
        break
    else:
        print("Wrong input!")



