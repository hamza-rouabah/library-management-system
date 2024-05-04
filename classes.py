from DB import *
from PyQt6 import (
    QtGui as qtg,
    QtCore as qtc,
    QtWidgets as qtw
)
style = open('style.css').read()

class del_button(qtw.QPushButton):
    def __init__(self, title) -> None:
        super().__init__(title)
        self.setStyleSheet(style)

class sell_button(qtw.QPushButton):
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet(style)

class borrow_button(qtw.QPushButton):
    def __init__(self) -> None:
        super().__init__()
        self.setStyleSheet(style)

class add_book_window(qtw.QDialog):
    def __init__(self,db) -> None:
        super().__init__()
        self.db = db
        self.setStyleSheet(style)
        self.setMaximumSize(400,470)
        self.setMinimumSize(400,470)
        
        layout = qtw.QFormLayout()
        self.setLayout(layout)

        #ISBN Row
        isbn_label = qtw.QLabel('ISBN')
        self.isbn = qtw.QLineEdit()
        self.isbn.setPlaceholderText('enter full ISBN here')
        layout.addRow(isbn_label)
        layout.addRow(self.isbn)

        #Title Row    
        title_label = qtw.QLabel('Title')
        self.title = qtw.QLineEdit()
        self.title.setPlaceholderText('enter document title here')
        layout.addRow(title_label)
        layout.addRow(self.title)

        #Author Row    
        author_label = qtw.QLabel('Author')
        self.author = qtw.QLineEdit()
        self.author.setPlaceholderText('full name of the author')
        layout.addRow(author_label)
        layout.addRow(self.author)

        #Genre Row    
        genre_label = qtw.QLabel('Genre')
        self.genre = qtw.QComboBox()
        self.genre.addItem('Fiction','fiction')
        self.genre.addItem('Non-fiction','nonfiction')
        self.genre.addItem('Novel','novel')
        self.genre.addItem('Thriller','thriller')
        layout.addRow(genre_label)
        layout.addRow(self.genre)

        #Num of pages
        self.num_pages = qtw.QLineEdit()
        self.num_pages.setPlaceholderText('total number of the pages')
        layout.addRow('# of pages', self.num_pages)

        #Price
        self.price = qtw.QSpinBox(value=10, maximum=1000000, minimum=1, suffix='  DA', singleStep=10)
        layout.addRow('Price', self.price)

        #Pub Date
        self.pub_year = qtw.QDateEdit()
        layout.addRow('Publication Date', self.pub_year)

        #Copies
        self.num_copies = qtw.QLineEdit()
        self.num_copies.setPlaceholderText('number of available copies')
        self.total_copies = qtw.QLineEdit()
        self.total_copies.setPlaceholderText('number of total copies')
        layout.addRow('Copies Available', self.num_copies)
        layout.addRow('Total Copies', self.total_copies)

        #Add & cancel buttons 
        self.cancel_button = del_button('Cancel')
        self.cancel_button.clicked.connect(self.close)
        self.add_button = qtw.QPushButton('Add Book')
        self.add_button.clicked.connect(self.add_book)
        layout.addRow(self.cancel_button, self.add_button)
    def add_book(self):
        # Get values from input fields
        isbn = self.isbn.text()
        title = self.title.text()
        author = self.author.text()
        genre = self.genre.currentData()  # Get current data (genre value) from combobox
        num_pages = int(self.num_pages.text())
        price = self.price.value()
        pub_date = self.pub_year.date().toPyDate()  # Convert QDate to Python date
        copies_available = int(self.num_copies.text())
        total_copies = int(self.total_copies.text())   
        # Create a new Book object
        book = Book(isbn, title, author, genre, num_pages, price, pub_date, copies_available, total_copies)
        # Add the book to the database
        book.insert_into_database(self.db.cursor)

class add_magazine_window(qtw.QDialog):
    def __init__(self,db) -> None:
        super().__init__()
        self.db = db
        self.setStyleSheet(style)
        self.setMaximumSize(400,450)
        self.setMinimumSize(400,450)
        
        layout = qtw.QFormLayout()
        self.setLayout(layout)

        #ISS Row
        issn_label = qtw.QLabel('ISSN')
        self.issn = qtw.QLineEdit()
        self.issn.setPlaceholderText('enter full ISSN here')
        layout.addRow(issn_label)
        layout.addRow(self.issn)

        #Title Row    
        title_label = qtw.QLabel('Title')
        self.title = qtw.QLineEdit()
        self.title.setPlaceholderText('enter document title here')
        layout.addRow(title_label)
        layout.addRow(self.title)

        #Author Row    
        author_label = qtw.QLabel('Author')
        self.author = qtw.QLineEdit()
        self.author.setPlaceholderText('full name of the author')
        layout.addRow(author_label)
        layout.addRow(self.author)

        #Pub Date
        self.pub_year = qtw.QDateEdit()
        layout.addRow('Publication Date', self.pub_year)

        #Issue number
        self.issue_num = qtw.QLineEdit()
        layout.addRow('Issue Number', self.issue_num)

        #Frequency Row    
        self.genre = qtw.QComboBox()
        self.genre.addItem('Bi-weekly','biweekly')
        self.genre.addItem('Monthly','monthly')
        self.genre.addItem('Quarterly','quarterly')
        layout.addRow('Frequency', self.genre)
        
        #Price
        self.price = qtw.QSpinBox(value=10, maximum=1000000, minimum=1, suffix='  DA', singleStep=10)
        layout.addRow('Price', self.price)
        
        #Copies
        self.num_copies = qtw.QLineEdit()
        self.num_copies.setPlaceholderText('number of available copies')
        self.total_copies = qtw.QLineEdit()
        self.total_copies.setPlaceholderText('number of total copies')
        layout.addRow('Copies Available', self.num_copies)
        layout.addRow('Total Copies', self.total_copies)

        #Add & cancel buttons 
        self.cancel_button = del_button('Cancel')
        self.cancel_button.clicked.connect(self.close)
        self.add_button = qtw.QPushButton('Add Magazine')
        self.add_button.clicked.connect(self.add_magazine)
        layout.addRow(self.cancel_button, self.add_button)
    def add_magazine(self):
        # get all values of input fields
        issn = self.issn.text()
        title = self.title.text()
        author = self.author.text()
        pub_date = self.pub_year.date().toPyDate()
        issue_num = int(self.issue_num.text())
        frequency = self.genre.currentData()
        price = self.price.value()
        copies_available = int(self.num_copies.text())
        total_copies = int(self.total_copies.text())
        # Create a new Magazine object
        magazine = Magazine(issn, title, author, pub_date, issue_num, frequency, price, copies_available, total_copies)
        # Add the magazine to the database
        magazine.insert_into_database(self.db.cursor)

class add_journal_window(qtw.QDialog):
    def __init__(self,db) -> None:
        super().__init__()
        self.db = db
        self.setStyleSheet(style)
        self.setMaximumSize(400,350)
        self.setMinimumSize(400,35)
        
        layout = qtw.QFormLayout()
        self.setLayout(layout)

        #DOI Row
        doi_label = qtw.QLabel('DOI')
        self.doi = qtw.QLineEdit()
        self.doi.setPlaceholderText('enter full doi here')
        layout.addRow(doi_label)
        layout.addRow(self.doi)

        #Title Row    
        title_label = qtw.QLabel('Title')
        self.title = qtw.QLineEdit()
        self.title.setPlaceholderText('enter document title here')
        layout.addRow(title_label)
        layout.addRow(self.title)

        #Author Row    
        author_label = qtw.QLabel('Author')
        self.author = qtw.QLineEdit()
        self.author.setPlaceholderText('full name of the author')
        layout.addRow(author_label)
        layout.addRow(self.author)

        #Pub Date
        self.pub_year = qtw.QDateEdit()
        layout.addRow('Publication Date', self.pub_year)

        #Copies
        self.num_copies = qtw.QLineEdit()
        self.num_copies.setPlaceholderText('number of available copies')
        self.total_copies = qtw.QLineEdit()
        self.total_copies.setPlaceholderText('number of total copies')
        layout.addRow('Copies Available', self.num_copies)
        layout.addRow('Total Copies', self.total_copies)

        #Add & cancel buttons 
        self.cancel_button = del_button('Cancel')
        self.cancel_button.clicked.connect(self.close)
        self.add_button = qtw.QPushButton('Add Journal')
        self.add_button.clicked.connect(self.add_journal)
        layout.addRow(self.cancel_button, self.add_button)
    def add_journal(self):
        # get all input fields
        doi = self.doi.text()
        title = self.title.text()
        author = self.author.text()
        pub_date = self.pub_year.date().toPyDate()
        copies_available = int(self.num_copies.text())
        total_copies = int(self.total_copies.text())


