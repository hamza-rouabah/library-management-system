import sqlite3


class LibraryDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def create_connection(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
    
    def create_tables(self):
        # Document table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Document(
                           Id_Document INTEGER PRIMARY KEY AUTOINCREMENT,
                           title TEXT,
                           author TEXT,
                           publication_year INTEGER,
                           copies_available INTEGER,
                           total_copies INTEGER
                        )''')

        # Book table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Book(
                           Id_Document INTEGER PRIMARY KEY,
                           num_pages INTEGER,
                           genre TEXT,
                           price INTEGER,
                           FOREIGN KEY(Id_Document) REFERENCES Document(Id_Document)
                        )''')

        # Magazine table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Magazine(
                           Id_Document INTEGER PRIMARY KEY,
                           issue_num INTEGER,
                           frequency TEXT,
                           price INTEGER,
                           FOREIGN KEY(Id_Document) REFERENCES Document(Id_Document)
                        )''')

        # Journal table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Journal(
                           Id_Document INTEGER PRIMARY KEY,
                           issue INTEGER,
                           FOREIGN KEY(Id_Document) REFERENCES Document(Id_Document)
                        )''')

        # Sell table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Sell(
                           Id_Sell INTEGER PRIMARY KEY AUTOINCREMENT,
                           book_price INTEGER,
                           quantity INTEGER,
                           total INTEGER,
                           Id_Document INTEGER,
                           FOREIGN KEY(Id_Document) REFERENCES Document(Id_Document)
                        )''')

        # Borrow table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Borrow(
                           Id_Borrow_book INTEGER PRIMARY KEY AUTOINCREMENT,
                           borrower_name TEXT,
                           borrower_phone_num INTEGER,
                           start_date DATE,
                           return_date DATE,
                           Id_Document INTEGER,
                           FOREIGN KEY(Id_Document) REFERENCES Document(Id_Document)
                        )''')
    
    def close_connection(self):
        self.connection.commit()
        self.connection.close()

class Document:
    def __init__(self, title, author, publication_year, copies_available, total_copies):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.copies_available = copies_available
        self.total_copies = total_copies
    def __str__(self):
        return f"title: {self.title}\nauthor: {self.author}\npublication_year: {self.publication_year}\ncopies_available: {self.copies_available}\ntotal_copies: {self.total_copies}"
    def insert_into_database(self, cursor):
        cursor.execute("INSERT INTO Document (title, author, publication_year, copies_available, total_copies) VALUES (?, ?, ?, ?, ?)", 
                        (self.title, self.author, self.publication_year, self.copies_available, self.total_copies))
        return cursor.lastrowid
class Book(Document):
    def __init__(self, title, author, publication_year, copies_available, total_copies, num_pages, genre, price):
        super().__init__(title, author, publication_year, copies_available, total_copies)
        self.num_pages = num_pages
        self.genre = genre
        self.price = price
    def __str__(self):
        return f"title: {self.title}\nauthor: {self.author}\npublication_year: {self.publication_year}\ncopies_available: {self.copies_available}\ntotal_copies: {self.total_copies}\nnum_pages: {self.num_pages}\ngenre: {self.genre}\nprice: {self.price}"
  
    def insert_into_database(self, cursor):
        document_id = super().insert_into_database(cursor)
        cursor.execute("INSERT INTO Book (Id_Document, num_pages, genre, price) VALUES (?, ?, ?, ?)", 
                            (document_id, self.num_pages, self.genre, self.price))
class Magazine(Document):
    def __init__(self, title, author, publication_year, copies_available, total_copies, issue_num, frequency, price):
        super().__init__(title, author, publication_year, copies_available, total_copies)
        self.issue_num = issue_num
        self.frequency = frequency
        self.price = price
    def __str__(self):
        return f"title: {self.title}\nauthor: {self.author}\npublication_year: {self.publication_year}\ncopies_available: {self.copies_available}\ntotal_copies: {self.total_copies}\nissue_num: {self.issue_num}\nfrequency: {self.frequency}\nprice: {self.price}"
    def insert_into_database(self, cursor):
        document_id = super().insert_into_database(cursor)
        cursor.execute("INSERT INTO Magazine (Id_Document, issue_num, frequency, price) VALUES (?, ?, ?, ?)", 
                        (document_id , self.issue_num, self.frequency, self.price))
class Journal(Document):
    def __init__(self, title, author, publication_year, copies_available, total_copies, issue):
        super().__init__(title, author, publication_year, copies_available, total_copies)
        self.issue = issue
    def __str__(self):
        return f"title: {self.title}\nauthor: {self.author}\npublication_year: {self.publication_year}\ncopies_available: {self.copies_available}\ntotal_copies: {self.total_copies}\nissue: {self.issue}"
    def insert_into_database(self, cursor):
        document_id = super().insert_into_database(cursor)
        cursor.execute("INSERT INTO Journal (Id_Document, issue) VALUES (?, ?)", 
                        (document_id, self.issue))
class Sell:
    def __init__(self, book_price, quantity, total, document_id,doc_type):
        self.book_price = book_price
        self.quantity = quantity
        self.total = total
        self.document_id = document_id
        self.doc_type = doc_type
    def __str__(self):
        return f"book_price: {self.book_price}\nquantity: {self.quantity}\ntotal: {self.total}\ndocument_id: {self.document_id}\ndoc_type: {self.doc_type}"
    def verify_quantity(self, cursor):
        cursor.execute("SELECT copies_available FROM Document WHERE Id_Document = ?", (self.document_id,))
        copies_available = cursor.fetchone()[0]
        return copies_available >= self.quantity
    def insert_into_database(self, cursor):
        cursor.execute("INSERT INTO Sell (book_price, quantity, total, Id_Document) VALUES (?, ?, ?, ?)", 
                        (self.book_price, self.quantity, self.total, self.document_id))
        return cursor.lastrowid
    def update_copies_available(self, cursor):
        # if copies_available - quantity = 0 , remove from  db
        cursor.execute("SELECT copies_available ,total_copies  FROM Document WHERE Id_Document = ?", (self.document_id,))
        copies_available, total_copies = cursor.fetchone()
        new_copies_available = copies_available - self.quantity
        new_total_copies = total_copies - self.quantity
        if new_total_copies == 0:
            # delete document 
            cursor.execute("DELETE FROM Document WHERE Id_Document = ?", (self.document_id,))
            # delete from book, magazine
            if self.doc_type == "Book":
                cursor.execute("DELETE FROM Book WHERE Id_Document = ?", (self.document_id,))
            elif self.doc_type == "Magazine":
                cursor.execute("DELETE FROM Magazine WHERE Id_Document = ?", (self.document_id,))
        else:
            # update copies_available and total_copies
            cursor.execute("UPDATE Document SET copies_available = ?, total_copies = ? WHERE Id_Document = ?", (new_copies_available, new_total_copies, self.document_id))
class Borrow:
    def __init__(self, borrower_name, borrower_phone_num, start_date, return_date, document_id):
        self.borrower_name = borrower_name
        self.borrower_phone_num = borrower_phone_num
        self.start_date = start_date
        self.return_date = return_date
        self.document_id = document_id
    def __str__(self):
        return f"borrower_name: {self.borrower_name}\nborrower_phone_num: {self.borrower_phone_num}\nstart_date: {self.start_date}\nreturn_date: {self.return_date}\ndocument_id: {self.document_id}"
    def verify_quantity(self, cursor):
        cursor.execute("SELECT copies_available FROM Document WHERE Id_Document = ?", (self.document_id,))
        copies_available = cursor.fetchone()[0]
        return copies_available >= 1
    def update_copies_available(self, cursor):
        cursor.execute("SELECT copies_available FROM Document WHERE Id_Document = ?", (self.document_id,))
        copies_available = cursor.fetchone()[0]
        new_copies_available = copies_available - 1
        cursor.execute("UPDATE Document SET copies_available = ? WHERE Id_Document = ?", (new_copies_available, self.document_id))
    def insert_into_database(self, cursor):
        cursor.execute("INSERT INTO Borrow (borrower_name, borrower_phone_num, start_date, return_date, Id_Document) VALUES (?, ?, ?, ?, ?)", 
                        (self.borrower_name, self.borrower_phone_num, self.start_date, self.return_date, self.document_id))

