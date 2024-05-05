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
    def __init__(self, book_price, quantity, total, document_id):
        self.book_price = book_price
        self.quantity = quantity
        self.total = total
        self.document_id = document_id

    def insert_into_database(self, cursor):
        cursor.execute("INSERT INTO Sell (book_price, quantity, total, Id_Document) VALUES (?, ?, ?, ?)", 
                        (self.book_price, self.quantity, self.total, self.document_id))
        return cursor.lastrowid

class Borrow:
    def __init__(self, borrower_name, borrower_phone_num, start_date, return_date, document_id):
        self.borrower_name = borrower_name
        self.borrower_phone_num = borrower_phone_num
        self.start_date = start_date
        self.return_date = return_date
        self.document_id = document_id

    def insert_into_database(self, cursor):
        cursor.execute("INSERT INTO Borrow (borrower_name, borrower_phone_num, start_date, return_date, Id_Document) VALUES (?, ?, ?, ?, ?)", 
                        (self.borrower_name, self.borrower_phone_num, self.start_date, self.return_date, self.document_id))

