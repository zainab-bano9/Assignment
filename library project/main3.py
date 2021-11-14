class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books:
            print("*" + book)
        
    def borrowBook(self, bookName):  
        if bookName in self.books:
            print(f"you have been issued {bookName}. please keep it safe and return it within 30 days")
            self.books.remove(bookName)
        else:
            print("Sorry, This book is not available or has alreay been issued to someone else. please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a greate day ahead!")

    
class Student:
     def requestBook(self):
         self.book = input("Enyer the name of the book you want to borrow: ")
         return self.book 

     def returnBook(self):
         self.book = input("Enyer the name of the book you want to return: ")
         return self.book 



if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Django","Clrs", "python Notes"])
    Student = Student()
    # centralLibrary.displayAvailableBooks()
    while(True):
        WelcomeMsg = '''====== Welcome to Central Library ======
        please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(WelcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(Student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(Student.returnBook())  
        elif a == 4:
            print("Thanks choosing central Library. have a greate day ahead!")
            exit()
        else:
            print("Invalid Choice")  

       