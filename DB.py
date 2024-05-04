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
                           isbn INTEGER,
                           num_pages INTEGER,
                           genre TEXT,
                           price INTEGER,
                           FOREIGN KEY(Id_Document) REFERENCES Document(Id_Document)
                        )''')

        # Magazine table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Magazine(
                           Id_Document INTEGER PRIMARY KEY,
                           issn INTEGER,
                           issue_num INTEGER,
                           frequency TEXT,
                           price INTEGER,
                           FOREIGN KEY(Id_Document) REFERENCES Document(Id_Document)
                        )''')

        # Journal table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Journal(
                           Id_Document INTEGER PRIMARY KEY,
                           doi INTEGER,
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
    def __init__(self, title, author, publication_year, copies_available, total_copies, isbn, num_pages, genre, price):
        super().__init__(title, author, publication_year, copies_available, total_copies)
        self.isbn = isbn
        self.num_pages = num_pages
        self.genre = genre
        self.price = price

    def insert_into_database(self, cursor):
        try:
            document_id = super().insert_into_database(cursor)
            cursor.execute("INSERT INTO Book (Id_Document, isbn, num_pages, genre, price) VALUES (?, ?, ?, ?, ?)", 
                            (document_id, self.isbn, self.num_pages, self.genre, self.price))
            return True  # Return True if insertion is successful
        except Exception as e:
            print("Error inserting Book into database:", e)
            return False  # Return False if insertion fails
class Magazine(Document):
    def __init__(self, title, author, publication_year, copies_available, total_copies, issn, issue_num, frequency, price):
        super().__init__(title, author, publication_year, copies_available, total_copies)
        self.issn = issn
        self.issue_num = issue_num
        self.frequency = frequency
        self.price = price

    def insert_into_database(self, cursor):
        document_id = super().insert_into_database(cursor)
        cursor.execute("INSERT INTO Magazine (Id_Document, issn, issue_num, frequency, price) VALUES (?, ?, ?, ?, ?)", 
                        (document_id, self.issn, self.issue_num, self.frequency, self.price))

class Journal(Document):
    def __init__(self, title, author, publication_year, copies_available, total_copies, doi, issue):
        super().__init__(title, author, publication_year, copies_available, total_copies)
        self.doi = doi
        self.issue = issue

    def insert_into_database(self, cursor):
        document_id = super().insert_into_database(cursor)
        cursor.execute("INSERT INTO Journal (Id_Document, doi, issue) VALUES (?, ?, ?)", 
                        (document_id, self.doi, self.issue))

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

def main():
    db = LibraryDatabase('library.db')
    db.create_connection()
    db.create_tables()

    # Inserting data
    book = Book('Python Programming', 'John Doe', 2020, 30, 50, 9781234567890, 300, 'Programming', 25)
    book.insert_into_database(db.cursor)

    magazine = Magazine('Tech Magazine', 'Tech Publications', 2024, 20, 30, 12345678, 5, 'Monthly', 10)
    magazine.insert_into_database(db.cursor)

    journal = Journal('Science Journal', 'Science Journal Publishers', 2024, 50, 50, 123456789, 1)
    journal.insert_into_database(db.cursor)

    sell = Sell(20, 50, 1000, book.insert_into_database(db.cursor))

    borrow = Borrow('Alice', 1234567890, '2024-04-01', '2024-04-15', magazine.insert_into_database(db.cursor))

    db.close_connection()

if __name__ == "__main__":
    main()
