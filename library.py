import datetime

class Author:
    def __init__(self, name, born = None, died = None):
        if not isinstance(name, str):
            raise Exception("A wrong type of name parameter was passed to Author initialization")
        else:
            self.name = name
        if not isinstance(born, datetime.date) and born != None:
            raise Exception("A wrong type of born parameter was passed to Author initialization")
        else:
            self.born = born
        if not isinstance(died, datetime.date) and died != None:
            raise Exception("A wrong type of died parameter was passed to Author initialization")
        else:
            self.died = died

class Clerk:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("A wrong type of name parameter was passed to Clerk initialization")
        else:
            self.name = name

class Reader:
    def __init__(self, name, born):
        if not isinstance(name, str):
            raise Exception("A wrong type of name parameter was passed to Reader initialization")
        else:
            self.name = name
        if not isinstance(born, datetime.date):
            raise Exception("A wrong type of born parameter was passed to Reader initialization. It has to be date")
        else:
            self.born = born
    def borrow(self, book, clerk):
        if not isinstance(book, Book):
            raise Exception("A wrong type of book parameter was passed to borrow() method of the Reader class")
        if not isinstance(clerk, Clerk):
            raise Exception("A wrong type of clerk parameter was passed to borrow() method of the Reader class")
        book.set_borrowed_by(self)
        book.set_lent_by(clerk)
    def give_back(self, book):
        if not isinstance(book, Book):
            raise Exception("A wrong type of book parameter was passed to give_back() method of the Reader class")
        else:
            book._lent_by = None
            book._borrowed_by = None

class Book:
    def __init__(self, name, authors, date_published, publisher, isbn):
        if not isinstance(name, str):
            raise Exception("A wrong type of name parameter was passed to book initialization")
        else:
            self.name = name
        if not isinstance(authors, list):
            raise Exception("A collection of Authors has to be a list")
        elif not all(isinstance(val, Author) for val in authors):
            raise Exception("A list of Authors has to contain only Authors objects")
        else:
            self.authors = authors
        if not isinstance(date_published, datetime.date) and date_published != None:
            raise Exception("A wrong type of date_published parameter was passed to book initialization")
        else:
            self.date_published = date_published
        if not isinstance(publisher, str):
            raise Exception("A wrong type of publisher parameter was passed to book initialization")
        else:
            self.publisher = publisher
        if not isinstance(isbn, str):
            raise Exception("A wrong type of isbn parameter was passed to book initialization")
        else:
            self.isbn = isbn
        self._borrowed_by = None
        self._lent_by = None
    
    def is_borrowed(self):
        if self._borrowed_by == None and self._lent_by == None:
            return False
        else:
            return True

    def borrowed_by(self):
        return self._borrowed_by

    def set_borrowed_by(self, reader):
        if not isinstance(reader, Reader):
            raise Exception("A wrong type of Reader parameter was passed to _borrowed_by() borrowed")
        else:
            self._borrowed_by = reader

    def lent_by(self):
        return self._lent_by
    
    def set_lent_by(self, clerk):
        if not isinstance(clerk, Clerk):
            raise Exception("A wrong type of Clerk parameter was passed to _lent_by setter")
        else:
            self._lent_by = clerk

class Department:
    def __init__(self, clerks = None, books = None):
        if clerks == None:
            clerks = []
        if books == None:
            books = []
        if not isinstance(clerks, list):
            raise Exception("A collection of Clerks passed to Department initialization has to be a list")
        elif not all(isinstance(val, Clerk) for val in clerks):
            raise Exception("A list of Clerks passed to Department initialization has to contain only Clerks objects")
        else:
            self._staff = clerks
        if not isinstance(books, list):
            raise Exception("A collection of Books passed to Department initialization has to be a list")
        elif not all(isinstance(val, Book) for val in books):
            raise Exception("A list of Books passed to Department initialization has to contain only Books objects")
        else: 
            self._books = books

    def staff(self):
        return self._staff

    def books(self):
        return self._books

    def available_books(self):
        avail_books = []
        for book in self._books:
            if not book.is_borrowed():
                avail_books.append(book)
        return avail_books

    def clerk_in_staff(self, checking_clerk):
        for clerk in self._staff:
                if clerk == checking_clerk:
                    return True
        return False

    def add_staff(self, whom):
        if isinstance(whom, str):
            new_clerk = Clerk(whom)
            self._staff.append(new_clerk)
            return new_clerk
        elif not isinstance(whom, Clerk):
            raise Exception("A wrong type of the parameter was passed to add_staff() method of Department class. It has to be a Clerk or a string")
        else:
            if not self.clerk_in_staff(whom):
                self._staff.append(whom)
                return whom
            else:
                return whom
                #print ("The clerk passed as a parameter to add_staff() method of Department class is already in the staff collection")

    
class Library:

    def __init__(self):
        self._departments = []
        self._authors = []
        self._readers = []

    #returns a list of Department instances
    def departments(self):
        return self._departments
    
    def book_exist(self, department, checking_book):
        for book in department._books:
                if book == checking_book:
                    return True
        return False
    
    #constraint about books?
    def add_book(self, name, authors, date_published, publisher, isbn, department):
        new_book = Book(name, authors, date_published, publisher, isbn)
        if not isinstance(department, Department):
            raise Exception("A wrong type of the parameter was passed to add_book() method of Library class")
        else:
            department._books.append(new_book)
            return new_book

    #Author constraint
    def author_exist(self, cheking_author):
        for author in self._authors:
            if author.name == cheking_author.name and author.born == cheking_author.born and author.died == cheking_author.died:
                #print("Adding author already exists in the authors list")
                return author
        return None

    def add_author(self, name, born = None, died = None):
        new_author = Author(name, born, died)
        old_author = self.author_exist(new_author)
        if old_author == None:
            self._authors.append(new_author)
            return new_author
        else:
            return old_author
    
    def add_reader(self, name, born):
        new_reader = Reader(name, born)
        self._readers.append(new_reader)
        return new_reader

    def add_department(self, clerks = None, books = None):
        new_department = Department(clerks, books)
        self._departments.append(new_department)
        return new_department

    def staff(self):
        clerks = []
        for department in self._departments:
            for clerk in department.staff():
                clerks.append(clerk)
        return list(set(clerks))

    def books(self):
        books = []
        for department in self._departments:
            for book in department.books():
                books.append(book)
        return books

    def available_books(self):
        books= []
        for department in self._departments:
            books.extend(department.available_books())
        return books