from PyQt6 import QtCore, QtGui, QtWidgets
from classes import *
from DB import LibraryDatabase
class Ui_MainWindow(object):
    def __init__(self, db):
        self.db = db
    def setupUi(self, MainWindow):
        #setting up the window, sizing and shit :)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setMaximumSize(QtCore.QSize(1280, 720))
        self.centralwidget.setObjectName("centralwidget")
        self.tab_widget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tab_widget.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.tab_widget.setMinimumSize(QtCore.QSize(1280, 720))
        self.tab_widget.setMaximumSize(QtCore.QSize(1280, 720))
        self.tab_widget.setObjectName("tab_widget")

        #Home Tab

        #this is all for alignement purpose
        self.home = QtWidgets.QWidget()
        self.home.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.home.setObjectName("home")
        self.frame = QtWidgets.QFrame(parent=self.home)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 670))
        self.frame.setMinimumSize(QtCore.QSize(1280, 670))
        self.frame.setMaximumSize(QtCore.QSize(1280, 670))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upper_frame = QtWidgets.QFrame(parent=self.frame)
        self.upper_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.upper_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.upper_frame.setObjectName("upper_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.upper_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.upper_frame)
        self.label.setMinimumSize(QtCore.QSize(600, 184))
        self.label.setMaximumSize(QtCore.QSize(600, 184))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\graphics/lms_logo.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.upper_frame)
        self.lower_frame = QtWidgets.QFrame(parent=self.frame)
        self.lower_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.lower_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.lower_frame.setObjectName("lower_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.lower_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inner_frame_1 = QtWidgets.QFrame(parent=self.lower_frame)
        self.inner_frame_1.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.inner_frame_1.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.inner_frame_1.setObjectName("inner_frame_1")
        self.horizontalLayout_2.addWidget(self.inner_frame_1)
        self.inner_frame_2 = QtWidgets.QFrame(parent=self.lower_frame)
        self.inner_frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.inner_frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.inner_frame_2.setObjectName("inner_frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.inner_frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        #End of the alignment process

        #Add book button
        book_icon = QtGui.QIcon(r'graphics/book.png')
        self.add_book_button = QtWidgets.QPushButton(parent=self.inner_frame_2)
        self.add_book_button.setIcon(book_icon)
        self.add_book_button.setObjectName("add_book_button")
        self.horizontalLayout_3.addWidget(self.add_book_button)
        self.add_book_button.clicked.connect(self.add_book)
        
        
        #add magazine button
        mag_icon = QtGui.QIcon(r'graphics/magazine.png')
        self.add_magazine_button = QtWidgets.QPushButton(parent=self.inner_frame_2)
        self.add_magazine_button.setIcon(mag_icon)
        self.add_magazine_button.setObjectName("add_magazine_button")
        self.add_magazine_button.clicked.connect(self.add_mag)
        self.horizontalLayout_3.addWidget(self.add_magazine_button)
        
        #add journal button
        journ_icon = QtGui.QIcon(r'graphics/journal.png')
        self.add_journal_button = QtWidgets.QPushButton(parent=self.inner_frame_2)
        self.add_journal_button.setIcon(journ_icon)
        self.add_journal_button.setObjectName("add_journal_button")
        self.add_journal_button.clicked.connect(self.add_journ)
        self.horizontalLayout_3.addWidget(self.add_journal_button)

        #this is also an alignment process :)
        self.horizontalLayout_2.addWidget(self.inner_frame_2)
        self.inner_frame_3 = QtWidgets.QFrame(parent=self.lower_frame)
        self.inner_frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.inner_frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.inner_frame_3.setObjectName("inner_frame_3")
        self.horizontalLayout_2.addWidget(self.inner_frame_3)
        self.verticalLayout.addWidget(self.lower_frame)
        self.tab_widget.addTab(self.home, "")
        
        #Books Tab
        self.books = QtWidgets.QWidget()
        self.books.setObjectName("books")
        self.tab_widget.addTab(self.books, "")
        self.book_tab_layout = QtWidgets.QVBoxLayout(self.books)
        self.books_table_view = books_table(self.db)
        self.book_tab_layout.addWidget(self.books_table_view)
        

        #Magazines Tab
        self.magazines = QtWidgets.QWidget()
        self.magazines.setObjectName("magazines")
        self.tab_widget.addTab(self.magazines, "")
        self.magz_tab_layout = QtWidgets.QVBoxLayout(self.magazines)
        self.magz_table_view = magazines_table(self.db)
        self.magz_tab_layout.addWidget(self.magz_table_view)

        #Journals Tab
        self.journals = QtWidgets.QWidget()
        self.journals.setObjectName("journals")
        self.tab_widget.addTab(self.journals, "")
        self.journal_tab_layout = qtw.QVBoxLayout(self.journals)
        self.journals_tab_view = journals_table(self.db)
        self.journal_tab_layout.addWidget(self.journals_tab_view)
        
        # borrowing tab
        self.borrowing = QtWidgets.QWidget()
        self.borrowing.setObjectName("borrowing")
        self.tab_widget.addTab(self.borrowing, "")
        self.borrowing_tab_layout = qtw.QVBoxLayout(self.borrowing)
        self.borrowing_tab_view = borrowing_table(self.db)
        self.borrowing_tab_layout.addWidget(self.borrowing_tab_view)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tab_widget.currentChanged.connect(self.refreshTables)
    def refreshTables(self):
        current_index = self.tab_widget.currentIndex()
        if current_index == 0:
            pass
        elif current_index == 1:
            self.books_table_view.populateTable()
        elif current_index == 2:
            self.magz_table_view.populateTable()
        elif current_index == 3:
            self.journals_tab_view.populateTable()
        elif current_index == 4:
            self.borrowing_tab_view.populateTable()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_book_button.setText(_translate("MainWindow", "Add Book"))
        self.add_magazine_button.setText(_translate("MainWindow", "Add Magazine"))
        self.add_journal_button.setText(_translate("MainWindow", "Add Journal"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.home), _translate("MainWindow", "Home"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.books), _translate("MainWindow", "Books"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.magazines), _translate("MainWindow", "Magazines"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.journals), _translate("MainWindow", "Journals"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.borrowing), _translate("MainWindow", "Borrowing"))
    def add_book(self):
        #ab_mw stands for add book main window
        ab_mw = add_book_window(self.db)
        ab_mw.setWindowTitle('Add Book')
        ab_mw.setWindowIcon(QtGui.QIcon(r'graphics/book.png'))
        ab_mw.exec()
    def add_mag(self):
        am_mw = add_magazine_window(self.db)
        am_mw.setWindowTitle('Add Magazine')
        am_mw.setWindowIcon(QtGui.QIcon(r'graphics/magazine.png'))
        am_mw.exec()
    def add_journ(self):
        aj_mw = add_journal_window(self.db)
        # aj_mw = borrow_order_window(self.db, 123456789,'Permanent Record')
        aj_mw.setWindowTitle('Add Journal')
        aj_mw.setWindowIcon(QtGui.QIcon(r'graphics/journal.png'))
        aj_mw.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    style = open('style.css').read()
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setStyleSheet(style)
    # create database 
    db = LibraryDatabase('library.db')
    db.create_connection()
    db.create_tables()
    ui = Ui_MainWindow(db)
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('Library Management System')
    MainWindow.show()
    app.aboutToQuit.connect(db.close_connection)
    sys.exit(app.exec())


