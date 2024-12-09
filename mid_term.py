class Library:
    book_list=[]

    @classmethod
    def view_all_books(cls):
        if not cls.book_list:
            print("No books available.")
        else:
            for book in cls.book_list:
                book.view_book_info()

    @classmethod
    def entry_book(cls,book):
        cls.book_list.append(book)

    @classmethod
    def find_book(cls,book_id):
        for book in cls.book_list:
            if book.get_book_id()==book_id:
                return book
        return None

class Book:
    def __init__(self,book_id,title,author):
        self.__book_id=book_id
        self.__title=title
        self.__author=author
        self.__availability=True
        Library.entry_book(self)

    def get_book_id(self):
        return self.__book_id
    
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
            print(f"'{self.__title}' has been borrowed.")
        else:
            print(f"'{self.__title}' is already borrowed.")

    def return_book(self):
        if not self.__availability:
            self.__availability=True
            print(f"'{self.__title}' has been returned.")
        else:
            print(f"'{self.__title}' was not borrowed.")

    def view_book_info(self):
        availability_status="Available" if self.__availability else "Not Available"
        print(f"ID:{self.__book_id},Title:{self.__title},Author:{self.__author},Availability:{availability_status}")

def menu():
    while True:
        print("\nLibrary Menu:")
        print("1.View All Books")
        print("2.Borrow a Book")
        print("3.Return a Book")
        print("4.Exit")

        choice=input("Enter your choice: ")
        if choice=="1":
            Library.view_all_books()
        elif choice=="2":
            book_id=input("Enter the Book ID to borrow: ")
            book=Library.find_book(book_id)
            if book:
                book.borrow_book()
            else:
                print("Error: Book ID not found.")
        elif choice=="3":
            book_id=input("Enter the Book ID to return: ")
            book=Library.find_book(book_id)
            if book:
                book.return_book()
            else:
                print("Error: Book ID not found.")
        elif choice=="4":
            print("Goodbye")
            break
        else:
            print("Invalid choice.Please try again.")

Book("001","Abar Jok-er Dhon","Hemendra Kumar Ray")
Book("002","Megha Mallar","Bibhutibhushan Bandyopadhyay")
Book("003","Sonkhar Sanket","Sujan DasGupta")
Book("004","Feluda Shomogro","Satyajit Ray")
Book("005","Bhomkash Shomogro","Sharadindu Bandyopadhyay")
menu()
