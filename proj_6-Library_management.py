# create a library class
#display book
# lend book - ( who owns the book if not present)
# add book
# return book
# HarryLibrary = Library(list of books, library_name)

# dictionary (books-nameofperson)
# create a main function and run an infinite while loop while asking users for their input


class library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"Books available in our library {self.name} : ")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("lender book is updated, you can check if the book is free for you !!")
        else:
            print(f"book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Book added to booklist")

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    harry = library(['python', 'Rich dad Poor dad', 'c++ with harry', 'Yek chihan'],"codewithme")

    while(True):
        print(f"Welcome to {harry.name} library")
        print("Enter your choice to continue")
        print("1. Display book")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = int(input())

        if user_choice == 1:
            print("Available books are : ")
            harry.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of book you want to lend : ")
            user = input("Enter your name")
            harry.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of book you want to add : ")
            harry.addBook(book)

        elif user_choice == 4:
            book = input("Enter the book you want to return : ")
            harry.returnBook(book)

        else:
             print("Invalid option")
        print("Press q to quit and c to continue")
        user_choice_2 = "1"
        while(user_choice_2 != "q" and user_choice_2 != "c"):
            user_choice_2 = input()
            if user_choice_2 == "q":
                exit()
            if user_choice_2 == "c":
                continue
