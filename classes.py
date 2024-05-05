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
    def __init__(self, title) -> None:
        super().__init__(title)
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
        self.setMaximumSize(400,450)
        self.setMinimumSize(400,450)
        
        layout = qtw.QFormLayout()
        self.setLayout(layout)

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
        title = self.title.text()
        author = self.author.text()
        genre = self.genre.currentData()  # Get current data (genre value) from combobox
        num_pages = int(self.num_pages.text())
        price = self.price.value()
        pub_date = self.pub_year.date().toPyDate()  # Convert QDate to Python date
        copies_available = int(self.num_copies.text())
        total_copies = int(self.total_copies.text())   
        # Create a new Book object
        book = Book(title, author, genre, num_pages, price, pub_date, copies_available, total_copies)
        # Add the book to the database
        book.insert_into_database(self.db.cursor)
        self.close()

class add_magazine_window(qtw.QDialog):
    def __init__(self,db) -> None:
        super().__init__()
        self.db = db
        self.setStyleSheet(style)
        self.setMaximumSize(400,430)
        self.setMinimumSize(400,430)
        
        layout = qtw.QFormLayout()
        self.setLayout(layout)

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
        title = self.title.text()
        author = self.author.text()
        pub_date = self.pub_year.date().toPyDate()
        issue_num = int(self.issue_num.text())
        frequency = self.genre.currentData()
        price = self.price.value()
        copies_available = int(self.num_copies.text())
        total_copies = int(self.total_copies.text())
        # Create a new Magazine object
        magazine = Magazine(title, author, pub_date, issue_num, frequency, price, copies_available, total_copies)
        # Add the magazine to the database
        magazine.insert_into_database(self.db.cursor)
        self.close()

class add_journal_window(qtw.QDialog):
    def __init__(self,db) -> None:
        super().__init__()
        self.db = db
        self.setStyleSheet(style)
        self.setMaximumSize(400,340)
        self.setMinimumSize(400,340)
        
        layout = qtw.QFormLayout()
        self.setLayout(layout)

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
        title = self.title.text()
        author = self.author.text()
        pub_date = self.pub_year.date().toPyDate()
        copies_available = int(self.num_copies.text())
        total_copies = int(self.total_copies.text())
        self.close()

class sell_order_window(qtw.QDialog):
    def __init__(self,db, doc_id, doc_price, doc_title) -> None:
        super().__init__()
        self.db = db
        self.setStyleSheet(style)
        self.setMaximumSize(400,270)
        self.setMinimumSize(400,270)
        self.doc_id = doc_id
        self.doc_price = doc_price
        self.doc_title = doc_title
        
        layout = qtw.QFormLayout()
        self.setLayout(layout)

        #Document identifier
        #di is short for document identifier
        di_label = qtw.QLabel('Document identifier')
        self.di = qtw.QLineEdit()
        self.di.setText(str(self.doc_id))
        self.di.setReadOnly(True)
        layout.addRow(di_label)
        layout.addRow(self.di)

        #Title Row   
        #tl is short for title
        tl_label = qtw.QLabel('Document Title')
        self.tl = qtw.QLineEdit()
        self.tl.setText(self.doc_title)
        self.tl.setReadOnly(True)
        layout.addRow(tl_label)
        layout.addRow(self.tl)
        
        #Price Row   
        #pr is short for price
        self.pr = qtw.QLineEdit()
        self.pr.setText(str(self.doc_price))
        self.pr.setReadOnly(True)
        layout.addRow('Price',self.pr)

        #Quanity Row    
        self.quantity = qtw.QLineEdit()
        self.quantity.setPlaceholderText('how many copies')
        layout.addRow('Quantity', self.quantity)

        #Add & cancel buttons 
        self.cancel_button = del_button('Cancel')
        self.cancel_button.clicked.connect(self.close)
        self.sell_button = sell_button('Sell')
        self.sell_button.clicked.connect(self.sell_doc)
        layout.addRow(self.cancel_button, self.sell_button)
    def sell_doc(self):
        # get all input fields
        doi = self.doi.text()
        title = self.title.text()
        author = self.author.text()
        pub_date = self.pub_year.date().toPyDate()
        copies_available = int(self.num_copies.text())
        total_copies = int(self.total_copies.text())
