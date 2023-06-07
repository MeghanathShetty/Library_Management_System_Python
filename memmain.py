from sys import argv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from searchbk import SearchBook
from viewexe import ViewBook
from memberui import Ui_MainWindow

class MainWindow(Ui_MainWindow):
    def __init__(self,window):
        # Necessary to setup UI
        self.setupUi(window)

        # Hiding the labels
        self.searchbkemp.setHidden(True)

        # Automatically calling view all book function when the app is opened
        ViewBook.memviewbookfun(self)

        # Connecting main page searchbook button to searchbook page
        self.msearchbook.clicked.connect(self.showbooksearchp)
        # Connecting search book page back button to main page
        self.searchbbcbtn.clicked.connect(self.showpanel)

        # ============================================================================================
        # When searchbook combobox text is changed to department this function will be called
        self.searchbkcombo.currentTextChanged.connect(self.searchbkcomboview)

         # ============================================================================================
        # When searchbook page back button is pressed the setsearchcombobktxt should be called
        self.searchbbcbtn.clicked.connect(self.setsearchbkcombotxt)

        # Connecting searchbook button to searchbook function
        self.searchbkbtn.clicked.connect(lambda:SearchBook.memsearchbkfun(self))

        # Connecting view all book button to viewbook function
        self.mdispallbook.clicked.connect(lambda:ViewBook.memviewbookfun(self))

        # =============================================================================================
        self.tableWidget.setStyleSheet("background-color:#FADCD9;border:none;border-radius:20px;")
        self.tableWidget.setAlternatingRowColors(True)  # Alternate row colors
        # =============================================================================================
        self.widget.setStyleSheet("QWidget#widget{border-image : url(bgg/topbook.jpg)}")
        # ============================================================================================================================
        self.mdispallbook.setIcon(QIcon("iconsc/bookshelf.png"))
        self.mdispallbook.setIconSize(QSize(175,175))
        self.mdispallbook.setText("View all Books")
        self.mdispallbook.setStyleSheet("QToolButton#mdispallbook{Padding-top:75px;border-radius:20px;background-color: #FADCD9;}QToolButton#mdispallbook:pressed{margin-top:3px;};")
        self.mdispallbook.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        # ============================================================================================================================
        self.msearchbook.setIcon(QIcon("iconsc/searchg.png"))
        self.msearchbook.setIconSize(QSize(175,175))
        self.msearchbook.setText("Search Books")
        self.msearchbook.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.msearchbook.setStyleSheet("QToolButton#msearchbook{Padding-top:75px;border-radius:20px;background-color: #FADCD9;}QToolButton#msearchbook:pressed{margin-top:3px;};")
        # ============================================================================================================================
        self.label_48.setStyleSheet("color:rgb(255, 255, 255)")
        self.qtylb.setStyleSheet("color:rgb(255, 255, 255)")
        # Set no special character validation========================================================================
        reg_exx=QRegExp("^[A-Za-z0-9]+$")
        input_validatorr = QRegExpValidator(reg_exx)
        self.searchbktxt.setValidator(input_validatorr)
        # ================================================================================================================
        # Set header font to 11 of tableWidget
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.horizontalHeader().setFont(font)
        # ===============================================================================================================
        # Creating object of shadoweffect
        shadow = QGraphicsDropShadowEffect()
        # setting blur radius (optional)
        shadow.setBlurRadius(20)
        shadow.setOffset(2)

        # Creating object of shadoweffect
        shadoww = QGraphicsDropShadowEffect()
        # setting blur radius (optional)
        shadoww.setBlurRadius(20)
        shadoww.setOffset(2)

        # Creating object of shadoweffect
        shadowww = QGraphicsDropShadowEffect()
        # setting blur radius (optional)
        shadowww.setBlurRadius(20)
        shadowww.setOffset(2)

        self.stackedWidget.setGraphicsEffect(shadow)
        self.label_2.setGraphicsEffect(shadoww)
        self.tableWidget.setGraphicsEffect(shadowww)

        # ===============================================================================================================
        
    def showpanel(self):
        self.stackedWidget.setCurrentWidget(self.mmainp)
        self.searchbkemp.setHidden(True)
        self.searchbktxtcombo.setHidden(True)
        # Set Quantity label 0
        self.qtylb.setText("0")


    # Functions to set different pages
    def showbooksearchp(self):
        self.stackedWidget.setCurrentWidget(self.searchp)

    

    #=============================================================================================================================
    # Function to set searchbkcombo index to 0
    def setsearchbkcombotxt(self):
        self.searchbkcombo.setCurrentIndex(0)

    # ============================================================================================================================
    # Function to make the other combobox visible when searchbkcombo text is changed to department
    def searchbkcomboview(self):
        if self.searchbkcombo.currentIndex()==3:
            self.searchbktxtcombo.setHidden(False)
            self.searchbktxt.setHidden(True)
        else:
            self.searchbktxtcombo.setHidden(True)
            self.searchbktxt.setHidden(False)

# Necessary to display UI
app = QtWidgets.QApplication(argv)
Mainwindow = QtWidgets.QMainWindow()
ui = MainWindow(Mainwindow)
Mainwindow.show()
app.exec()




