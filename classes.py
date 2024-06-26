from datetime import datetime
from DB import *
from PyQt6 import (
    QtGui as qtg,
    QtCore as qtc,
    QtWidgets as qtw
)
style = open('style.css').read()
db  = LibraryDatabase('library.db')
class del_button(qtw.QPushButton):
    def __init__(self, title) -> None:
        super().__init__(title)
        self.setStyleSheet(style)
class sell_button(qtw.QPushButton):
    def __init__(self, title) -> None:
        super().__init__(title)
        self.setStyleSheet(style)
class borrow_button(qtw.QPushButton):
    def __init__(self, title) -> None:
        super().__init__(title)
        self.setStyleSheet(style)
class add_book_window(qtw.QDialog):
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
        self.num_pages.setValidator(qtg.QIntValidator())
        layout.addRow('# of pages', self.num_pages)

        #Price
        self.price = qtw.QSpinBox(value=10, maximum=1000000, minimum=1, suffix='  DA', singleStep=10)
        layout.addRow('Price', self.price)

        self.pub_year = qtw.QDateEdit()
        initial_date = qtc.QDate(2024, 1, 1)  # Set the initial date to January 1, 2024
        self.pub_year.setDate(initial_date)
        self.pub_year.setDisplayFormat("yyyy")  # Display only the year
        layout.addRow('Publication Year', self.pub_year)

        #Copies
        self.num_copies = qtw.QLineEdit()
        self.num_copies.setPlaceholderText('number of available copies')
        self.num_copies.setValidator(qtg.QIntValidator())
        self.total_copies = qtw.QLineEdit()
        self.total_copies.setPlaceholderText('number of total copies')
        self.total_copies.setValidator(qtg.QIntValidator())
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
        genre = self.genre.currentData() 
        num_pages = int(self.num_pages.text())
        price = self.price.value()
        publication_year = self.pub_year.date().year()
        copies_available = int(self.num_copies.text())
        total_copies = int(self.total_copies.text())   
        # Create a new Book object
        book = Book(title, author, publication_year, copies_available, total_copies, num_pages, genre, price)
        # Add the book to the database
        book.insert_into_database(self.db.cursor)
        self.db.connection.commit()
        self.close()
class add_magazine_window(qtw.QDialog):
    def __init__(self,db) -> None:
        super().__init__()
        self.db = db
        self.setStyleSheet(style)
        self.setMaximumSize(400,410)
        self.setMinimumSize(400,410)
        
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

        # publication yeaar
        self.pub_year = qtw.QDateEdit()
        initial_date = qtc.QDate(2024, 1, 1)  # Set the initial date to January 1, 2024
        self.pub_year.setDate(initial_date)
        self.pub_year.setDisplayFormat("yyyy")  # Display only the year
        layout.addRow('Publication Year', self.pub_year)

        #Issue number
        self.issue_num = qtw.QLineEdit()
        self.issue_num.setValidator(qtg.QIntValidator())
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
        self.num_copies.setValidator(qtg.QIntValidator())
        self.total_copies = qtw.QLineEdit()
        self.total_copies.setPlaceholderText('number of total copies')
        self.total_copies.setValidator(qtg.QIntValidator())
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
        publication_year = self.pub_year.date().year()
        issue_num = int(self.issue_num.text())
        frequency = self.genre.currentData()
        price = self.price.value()
        copies_available = int(self.num_copies.text())
        total_copies = int(self.total_copies.text())
        # Create a new Magazine object
        magazine = Magazine(title, author, publication_year, copies_available, total_copies, issue_num, frequency, price)
        # Add the magazine to the database
        magazine.insert_into_database(self.db.cursor)
        self.db.connection.commit()
        self.close()
class add_journal_window(qtw.QDialog):
    def __init__(self,db) -> None:
        super().__init__()
        self.db = db
        self.setStyleSheet(style)
        self.setMaximumSize(400,310)
        self.setMinimumSize(400,310)
        
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

        self.pub_year = qtw.QDateEdit()
        initial_date = qtc.QDate(2024, 1, 1)  # Set the initial date to January 1, 2024
        self.pub_year.setDate(initial_date)
        self.pub_year.setDisplayFormat("yyyy")  # Display only the year
        layout.addRow('Publication Year', self.pub_year)

        #Issue number
        self.issue_num = qtw.QLineEdit()
        self.issue_num.setValidator(qtg.QIntValidator())
        layout.addRow('Issue Number', self.issue_num)
        
        #Copies
        self.num_copies = qtw.QLineEdit()
        self.num_copies.setPlaceholderText('number of available copies')
        self.num_copies.setValidator(qtg.QIntValidator())
        self.total_copies = qtw.QLineEdit()
        self.total_copies.setPlaceholderText('number of total copies')
        self.total_copies.setValidator(qtg.QIntValidator())
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
        publication_year = self.pub_year.date().year()
        copies_available = int(self.num_copies.text())
        total_copies = int(self.total_copies.text())
        issue = int(self.issue_num.text())
        # Create a new Journal object
        journal = Journal(title, author, publication_year, copies_available, total_copies, issue)
        # Add the journal to the database
        journal.insert_into_database(self.db.cursor)
        self.db.connection.commit()
        self.close()
class books_table(qtw.QWidget):
    def __init__(self,db):
        super().__init__()
        self.setupUi()
        self.db = db
        self.borrowing_table = borrowing_table
        self.doc_type = 'Book'
        # Assuming you have a `books_table` instance called `books_table_widget`
    def setupUi(self):
        self.layout = qtw.QVBoxLayout(self)
        self.tableWidget = qtw.QTableWidget()
        self.layout.addWidget(self.tableWidget)
        self.populateTable()
    def populateTable(self):
        connection = sqlite3.connect('library.db')
        self.cur = connection.cursor()
        self.cur.execute("""SELECT D.Id_document, D.title, D.author, D.publication_year, D.copies_available, D.total_copies, B.num_pages, B.genre, B.price
                            FROM Document D
                            JOIN Book B ON D.Id_document = B.Id_document;
                        """)
        rows = self.cur.fetchall()

        self.tableWidget.setRowCount(len(rows))
        if len(rows) > 0:
            self.tableWidget.setColumnCount(len(rows[0]) + 2)  # Adding two additional columns

            # Set horizontal header labels
            column_names = [description[0] for description in self.cur.description]
            column_names.extend(["Sell", "Borrow"])  # Additional column names
            self.tableWidget.setHorizontalHeaderLabels(column_names)

            # Populate the table with data
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = qtw.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, j, item)

                # Add buttons to the additional columns
                btn1 = sell_button("Sell")
                btn1.clicked.connect(lambda _, i=i: self.buttonClicked("Sell"))
                self.tableWidget.setCellWidget(i, len(row), btn1)

                btn2 = borrow_button("Borrow")
                btn2.clicked.connect(lambda _, i=i: self.buttonClicked("Borrow"))
                self.tableWidget.setCellWidget(i, len(row) + 1, btn2)

             # Enable sorting when clicking on the header
            self.tableWidget.horizontalHeader().sectionClicked.connect(self.sortTable)
    def sortTable(self, logicalIndex):
        # select wich column
        list_column = ["Id_document", "title", "author", "publication_year", "copies_available", "total_copies", "num_pages", "genre", "price"]
        self.tableWidget.sortItems(logicalIndex)        
    def buttonClicked(self, button):
        button_clicked = self.sender()
        if button_clicked:
            index = self.tableWidget.indexAt(button_clicked.pos())
            if index.isValid():
                row = index.row()
                # Retrieve data from the clicked row
                data = []
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item:
                        data.append(item.text())
                    else:
                        widget = self.tableWidget.cellWidget(row, column)
                        if widget:
                            data.append(widget.text())
                if button == 'Sell':
                    self.sell_book(data[0], data[1], data[8])
                elif button == 'Borrow':
                    self.borrow_book(data[0], data[1])                   
    def sell_book(self, doc_id, doc_title, doc_price):
        sw = sell_order_window(self.db, doc_id, doc_price, doc_title, self.doc_type)
        sw.setWindowTitle('Sell Book')
        sw.setWindowIcon(qtg.QIcon(r'graphics/sell.png'))
        sw.exec()
        self.populateTable()      
    def borrow_book(self, doc_id, doc_title):
        bw = borrow_order_window(self.db, doc_id, doc_title)
        bw.setWindowTitle('Borrow Book')
        bw.setWindowIcon(qtg.QIcon(r'graphics/borrow.png'))
        bw.exec()
        self.populateTable()
class magazines_table(qtw.QWidget):
    def __init__(self,db):
        super().__init__()
        self.setupUi()
        self.db = db
        self.doc_type = 'Magazine'
        self.borrowing_table = borrowing_table

    def setupUi(self):
        self.layout = qtw.QVBoxLayout(self)
        self.tableWidget = qtw.QTableWidget()
        self.layout.addWidget(self.tableWidget)
        self.populateTable()

    def populateTable(self):
        connection = sqlite3.connect('library.db')
        self.cur = connection.cursor()
        self.cur.execute("""SELECT M.Id_document, M.issue_num, M.frequency, M.price,
                            D.title, D.author, D.publication_year, D.copies_available, D.total_copies
                            FROM Magazine M
                            JOIN Document D ON M.Id_document = D.Id_document;
                        """)
        rows = self.cur.fetchall()

        self.tableWidget.setRowCount(len(rows))
        if len(rows) > 0:
            self.tableWidget.setColumnCount(len(rows[0]) + 2)  # Adding two additional columns

            # Set horizontal header labels
            column_names = [description[0] for description in self.cur.description]
            column_names.extend(["Sell", "Borrow"])  # Additional column names
            self.tableWidget.setHorizontalHeaderLabels(column_names)

            # Populate the table with data
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = qtw.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, j, item)

                # Add buttons to the additional columns
                btn1 = sell_button("Sell")
                btn1.clicked.connect(lambda _, i=i: self.buttonClicked("Sell"))
                self.tableWidget.setCellWidget(i, len(row), btn1)

                btn2 = borrow_button("Borrow")
                btn2.clicked.connect(lambda _, i=i: self.buttonClicked("Borrow"))
                self.tableWidget.setCellWidget(i, len(row) + 1, btn2)

            # Enable sorting when clicking on the header
            self.tableWidget.horizontalHeader().sectionClicked.connect(self.sortTable)

    def sortTable(self, logicalIndex):
        self.tableWidget.sortItems(logicalIndex)
    
    def buttonClicked(self, button):
        button_clicked = self.sender()
        if button_clicked:
            index = self.tableWidget.indexAt(button_clicked.pos())
            if index.isValid():
                row = index.row()
                # Retrieve data from the clicked row
                data = []
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item:
                        data.append(item.text())
                    else:
                        widget = self.tableWidget.cellWidget(row, column)
                        if widget:
                            data.append(widget.text())
                if button == 'Sell':
                    self.sell_magazine(data[0], data[4], data[3])
                elif button == 'Borrow':
                    self.borrow_magazine(data[0], data[4])

    def sell_magazine(self, doc_id, doc_title, doc_price):
        sw = sell_order_window(self.db, doc_id, doc_price, doc_title, self.doc_type)
        sw.setWindowTitle('Sell Magazine')
        sw.setWindowIcon(qtg.QIcon(r'graphics/sell.png'))
        sw.exec()
        self.populateTable()

    def borrow_magazine(self, doc_id, doc_title):
        bw = borrow_order_window(self.db, doc_id, doc_title)
        bw.setWindowTitle('Borrow Magazine')
        bw.setWindowIcon(qtg.QIcon(r'graphics/borrow.png'))
        bw.exec()
        self.populateTable()
class journals_table(qtw.QWidget):
    def __init__(self,db):
        super().__init__()
        self.setupUi()
        self.db = db

    def setupUi(self):
        self.layout = qtw.QVBoxLayout(self)
        self.tableWidget = qtw.QTableWidget()
        self.layout.addWidget(self.tableWidget)
        self.populateTable()

    def populateTable(self):
        connection = sqlite3.connect('library.db')
        self.cur = connection.cursor()
        self.cur.execute("""SELECT J.Id_document, J.issue, D.title, D.author, D.publication_year, D.copies_available, D.total_copies
                            FROM Journal J
                            JOIN Document D ON D.Id_document = J.Id_document;
                        """)
        rows = self.cur.fetchall()

        self.tableWidget.setRowCount(len(rows))
        if len(rows) > 0:
            self.tableWidget.setColumnCount(len(rows[0]) + 1)  # Adding two additional columns

            # Set horizontal header labels
            column_names = [description[0] for description in self.cur.description]
            column_names.extend(["Borrow"])  # Additional column names
            self.tableWidget.setHorizontalHeaderLabels(column_names)

            # Populate the table with data
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = qtw.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, j, item)

                # Add buttons to the additional columns
                btn1 = borrow_button("Borrow")
                btn1.clicked.connect(lambda _, i=i: self.buttonClicked("Borrow"))
                self.tableWidget.setCellWidget(i, len(row), btn1)

            # Enable sorting when clicking on the header
            self.tableWidget.horizontalHeader().sectionClicked.connect(self.sortTable)

    def sortTable(self, logicalIndex):
        self.tableWidget.sortItems(logicalIndex)


    def borrow_journal(self, doc_id, doc_title):
        #bw short for sell window
        bw = borrow_order_window(self.db, doc_id, doc_title)
        bw.setWindowTitle('Borrow Journal')
        borrow_icon = qtg.QIcon(r'graphics/borrow.png')
        bw.setWindowIcon(borrow_icon)
        bw.exec()
        self.populateTable()
    
    def buttonClicked(self, button):
        button_clicked = self.sender()
        if button_clicked:
            index = self.tableWidget.indexAt(button_clicked.pos())
            if index.isValid():
                row = index.row()
                # Retrieve data from the clicked row
                data = []
                for column in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, column)
                    if item:
                        data.append(item.text())
                    else:
                        widget = self.tableWidget.cellWidget(row, column)
                        if widget:
                            data.append(widget.text())
                self.borrow_journal(data[0], data[2])
class borrowing_table(qtw.QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setupUi()

    def setupUi(self):
        self.layout = qtw.QVBoxLayout(self)
        self.tableWidget = qtw.QTableWidget()
        self.layout.addWidget(self.tableWidget)
        self.populateTable()

    def populateTable(self):
        connection = sqlite3.connect('library.db')
        cur = connection.cursor()
        cur.execute("""SELECT Borrow.Id_Borrow_book, Document.title, Borrow.borrower_name, Borrow.borrower_phone_num, Borrow.start_date, Borrow.return_date
                        FROM Borrow
                        JOIN Document ON Borrow.Id_Document = Document.Id_Document
                    """)
        rows = cur.fetchall()

        self.tableWidget.setRowCount(len(rows))
        if len(rows) > 0:
            self.tableWidget.setColumnCount(len(rows[0]) + 1)  # Set number of columns, plus one for the button

            # Set horizontal header labels
            column_names = [description[0] for description in cur.description]
            column_names.append("Unborrow")  # Add column for unborrow button
            self.tableWidget.setHorizontalHeaderLabels(column_names)

            # Populate the table with data
            for i, row in enumerate(rows):
                for j, value in enumerate(row):
                    item = qtw.QTableWidgetItem(str(value))
                    self.tableWidget.setItem(i, j, item)

                # Add unborrow button to the last column
                unborrow_btn = qtw.QPushButton("Unborrow", self)
                unborrow_btn.clicked.connect(lambda _, i=i: self.unborrowButtonClicked(i))
                self.tableWidget.setCellWidget(i, len(row), unborrow_btn)

            # Enable sorting when clicking on the header
            self.tableWidget.horizontalHeader().sectionClicked.connect(self.sortTable)

    def sortTable(self, logicalIndex):
        self.tableWidget.sortItems(logicalIndex)

    def unborrowButtonClicked(self, row):
        # Get the ID of the borrowed book from the selected row
        borrow_id = self.tableWidget.item(row, 0).text()  # Assuming the ID is in the first column
        return_date = self.tableWidget.item(row, 5).text()

        # Show confirmation dialog
        confirmation_dialog = UnborrowConfirmationWindow(self)
        response = confirmation_dialog.exec()
        if response == qtw.QMessageBox.StandardButton.Yes:
            # Get today's date
            today = qtc.QDate.currentDate()
            # Get the return date
            return_date = qtc.QDate.fromString(return_date, "yyyy-MM-dd")
            # Check if return date is earlier than today
            if return_date < today:
                # Show a message
                qtw.QMessageBox.warning(self, "Invalid Return Date", "Return date is late")
                # Unborrow the book
                self.unborrowBook(borrow_id)
            self.unborrowBook(borrow_id)

    def unborrowBook(self, borrow_id):
        # update copies_available in Document
        self.db.cursor.execute("SELECT Id_Document FROM Borrow WHERE Id_Borrow_book = ?", (borrow_id,))
        doc_id = self.db.cursor.fetchone()[0]
        self.db.cursor.execute("UPDATE Document SET copies_available = copies_available + 1 WHERE Id_Document = ?", (doc_id,))
        # Delete the borrow record from the database
        self.db.cursor.execute("DELETE FROM Borrow WHERE Id_Borrow_book = ?", (borrow_id,))
        self.db.connection.commit()
        self.populateTable()
class UnborrowConfirmationWindow(qtw.QMessageBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Confirmation")
        self.setText("Are you sure you want to unborrow this book?")
        self.setStandardButtons(qtw.QMessageBox.StandardButton.Yes | qtw.QMessageBox.StandardButton.No)
        self.setDefaultButton(qtw.QMessageBox.StandardButton.No)
class borrow_order_window(qtw.QDialog):
    def __init__(self,db, doc_id, doc_title) -> None:
        super().__init__()
        self.db = db
        self.setStyleSheet(style)
        self.setMaximumSize(400,370)
        self.setMinimumSize(400,370)
        self.doc_id = doc_id
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
        
        #Borrower name
        b_name_label = qtw.QLabel('Borrower Name')
        self.b_name = qtw.QLineEdit()
        layout.addRow(b_name_label)
        layout.addRow(self.b_name)

        #Borrower phone num 
        b_phone_label = qtw.QLabel('Borrower Phone Number')
        self.b_phone = qtw.QLineEdit()
        self.b_phone.setValidator(qtg.QIntValidator())
        layout.addRow(b_phone_label)
        layout.addRow(self.b_phone)

        #Start and return dates
        # start date from today
        today = datetime.today().date()
        self.start_date = qtw.QDateEdit()
        self.start_date.setDate(today)
        layout.addRow('Start Date', self.start_date)
        self.return_date = qtw.QDateEdit()
        self.return_date.setDate(today)
        layout.addRow('Return Date', self.return_date)

        #Add & cancel buttons 
        self.cancel_button = del_button('Cancel')
        self.cancel_button.clicked.connect(self.close)
        self.borrow_button = borrow_button('Borrow')
        self.borrow_button.clicked.connect(self.borrow_doc)
        layout.addRow(self.cancel_button, self.borrow_button)
    def borrow_doc(self):
        # get all input fields
        start_date = self.start_date.date().toPyDate()
        return_date = self.return_date.date().toPyDate()
        doc_id = self.doc_id
        borrower_name = self.b_name.text()
        borrower_phone_num = self.b_phone.text()
        borrow = Borrow(borrower_name, borrower_phone_num, start_date, return_date, doc_id)
        if borrow.verify_quantity(self.db.cursor):
            borrow.insert_into_database(self.db.cursor)
            borrow.update_copies_available(self.db.cursor)
            self.db.connection.commit()
            self.close()
        else:
            qtw.QMessageBox.warning(self, 'Error', 'The quantity is greater than the available copies.')
class sell_order_window(qtw.QDialog):
    def __init__(self,db, doc_id, doc_price, doc_title,doc_type) -> None:
        super().__init__()
        self.db = db
        self.setStyleSheet(style)
        self.setMaximumSize(400,290)
        self.setMinimumSize(400,290)
        self.doc_id = doc_id
        self.doc_price = doc_price
        self.doc_title = doc_title
        self.doc_type = doc_type

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
        self.quantity.setText('0')
        self.quantity.setValidator(qtg.QIntValidator())
        layout.addRow('Quantity', self.quantity)

        #Total Row    
        self.total = qtw.QLineEdit()
        self.total.setText(f'{int(self.quantity.text()) * int(self.pr.text())}')
        self.total.setReadOnly(True)
        self.quantity.textChanged.connect(self.set_total)
        layout.addRow('Total', self.total)

        #Add & cancel buttons 
        self.cancel_button = del_button('Cancel')
        self.cancel_button.clicked.connect(self.close)
        self.sell_button = sell_button('Sell')
        self.sell_button.clicked.connect(self.sell_doc)
        layout.addRow(self.cancel_button, self.sell_button)
    def sell_doc(self):
        # get all input fields
        quantity = int(self.quantity.text())
        total = int(self.total.text())
        doc_id = self.doc_id
        doc_type = self.doc_type
        sell = Sell(self.doc_price, quantity, total, doc_id, doc_type)
        if sell.verify_quantity(self.db.cursor):
            sell.update_copies_available(self.db.cursor)
            sell.insert_into_database(self.db.cursor)
            self.db.connection.commit()
            self.close()
        else:
            qtw.QMessageBox.warning(self, 'Error', 'The quantity is greater than the available copies.')
    def set_total(self):
        if self.quantity.text() == '':
            self.total.setText('0')
        else:
            self.total.setText(f'{int(self.quantity.text()) * int(self.pr.text())}')
