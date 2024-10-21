class Book:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
class Library:
    def __init__(self):
        self.books=[]
    def addBook(self,book):
        self.books.append(book)
        print(f"{book} added")
    def removeBook(self,title):
        for book in self.books:
            if book.title==title:
                self.books.remove(book)
                print(f"{book} is removed")
                return
            else:
                print("Book not present in library")
    def showbooks(self):
        if not self.books:
            print("No books in library")
        else:
            print("Books in library")
            for book in self.books:
                print(book)
    def library_system():
        library=Library()
        book1 = Book("1984", "George Orwell", 1949)
        book2 = Book("To Kill a Mockingbird", "Harper Lee",1960)
        book3 = Book("The Great Gatsby", "F. ScottFitzgerald", 1925)   
        library.addBook(book1)
        library.addBook(book2)
        library.addBook(book3)
        library.showbooks()
        library.removeBook(book1)
    library_system()                 
                                   