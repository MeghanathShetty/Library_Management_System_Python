from sys import argv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from datetime import date,timedelta
from dateutil import parser
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
from viewstd import Viewstud
from viewstf import Viewstaff
from addbook import Addbook
from deletebook import Deletebk
from addstaff import Addstaff
from searchbk import SearchBook
from searchstf import SearchStaff
from searchstd import SearchStud
from adstud import Addstudent
from deletestaff import Deletestf
from deletestud import Deletestd
from issuestf import Issuestaff
from issuestd import Issuestud
from returnstud import  Returnstud
from returnstaf import Returnstaff
from renewstud import RenewStud
from renewstaf import RenewStaff
from viewisstf import ViewIsstf
from viewisstd import ViewIsstd
from srchisstd import Searchisstd
from srchisstf import Searchisstf
from createdb import Createdb
import mysql.connector 

class MainWindow(Ui_MainWindow):
    def __init__(self,window):
        # Necessary to setup UI
        self.setupUi(window)

        # Setting labels hidden
        self.invalidlb.setHidden(True)
        self.invalidbk.setHidden(True)
        self.delbsucesslb.setHidden(True)
        self.adbsucesslb.setHidden(True)
        self.adbexist.setHidden(True)
        self.adbkemp.setHidden(True)
        self.adstafemp.setHidden(True)
        self.delbemp.setHidden(True)
        self.adstafexist.setHidden(True)
        self.adstafsucesslb.setHidden(True)
        self.searchbkemp.setHidden(True)
        self.searchstfemp.setHidden(True)
        self.searchstdemp.setHidden(True)
        self.adstudexist.setHidden(True)
        self.adstudsucess.setHidden(True)
        self.adstudemp.setHidden(True)
        self.searchbktxtcombo.setHidden(True)
        self.searchstftxtcombo.setHidden(True)
        self.searchstdtxtcombo.setHidden(True)
        self.delstfemp.setHidden(True)
        self.invalidstf.setHidden(True)
        self.delstfsucesslb.setHidden(True)
        self.delstdemp.setHidden(True)
        self.invalidstd.setHidden(True)
        self.delstdsucesslb.setHidden(True)
        self.isstfemp.setHidden(True)
        self.isstdemp.setHidden(True)
        self.returnstudemp_2.setHidden(True)
        self.returnstudemp_3.setHidden(True)
        self.returnstaffemp.setHidden(True)
        self.returnstudemp.setHidden(True)

        # # Automatically calling view all book function when the app is opened
        # ViewBook.viewbookfun(self)      

        #Calling create database function when app is created
        Createdb.createdbs(self)

        # Connecting add book page back button to main page
        self.adbcbtn.clicked.connect(self.showpanel)
        # Connecting delete book page back button to main page
        self.dlbcbtn.clicked.connect(self.showpanel)
        # Connecting main page delete book button to showdelbkpage(Showdeletepage) function
        self.deletebk.clicked.connect(self.showdelbkpage)
        # Connecting main page add book button to showaddpage function
        self.adbook.clicked.connect(self.showaddpage)
        # Connecting main page add staff button to showaddstaffpage function
        self.adstaff.clicked.connect(self.showaddstafpage)
        # Connecting add staff page back button to main page
        self.adstafbcbtn.clicked.connect(self.showpanel)
         # Connecting main page add stud button to showaddstudpage function
        self.adstud.clicked.connect(self.showaddstudpage)
        # Connecting add stud page back button to main page
        self.adstudbcbtn.clicked.connect(self.showpanel)
        # Connecting main page view member button to select type of member page
        self.adispallmem.clicked.connect(self.showstafstudselpage)
        # Connecting stafstudp page back button to main page
        self.stafstudpbcbtn.clicked.connect(self.showpanel)
        # Connecting addstud page back button to main page
        self.adstudbcbtn.clicked.connect(self.showpanel)
        # Connecting main page searchbook button to searchbook page
        self.asearchbook.clicked.connect(self.showbooksearchp)
        # Connecting search book page back button to main page
        self.searchbbcbtn.clicked.connect(self.showpanel)
        # Connecting delete page staff button to staff delete page
        self.selstfbtn.clicked.connect(self.showstfdelp)
        # Connecting delete page student button to student delete page
        self.selstdbtn.clicked.connect(self.showstddelp)
        # Connecting main page search member button to searchmember page
        self.searchmm.clicked.connect(self.showsearchmemberp)
        # Connecting search member page back button to main page
        self.searchmbcbtn.clicked.connect(self.showpanel)
        #Connecting search member page staff button to search staff page
        self.selstfbtn_2.clicked.connect(self.showstfsearchp)
        #Connecting search member page student button to search staff page
        self.selstdbtn_2.clicked.connect(self.showstdsearchp)
        # Connecting issue book page back button to main page
        self.ismmbcbtn.clicked.connect(self.showpanel)
        # Connecting main page issue book button to issue page
        self.issuebk.clicked.connect(self.showissuep)
        # Connecting return page back button to main page
        self.rtnbcbtn.clicked.connect(self.showpanel)
        # Connecting main page return book button to return page
        self.returnbk.clicked.connect(self.showreturnp)
        #Connecting return book page student button to return student page
        self.selstdbtn_4.clicked.connect(self.showstdrtnp)
        #Connecting return book page staff button to return staff page
        self.selstfbtn_4.clicked.connect(self.showstfrtnp)
        # Connecting return page stud renew button to renew stud page
        self.renewstud.clicked.connect(self.showstudrenewp)
         # Connecting return page staff renew button to renew staff page
        self.renewstaff.clicked.connect(self.showstafrenewp)
        # Connecting stud renew page back button to return stud page
        self.renewstdbcbtn.clicked.connect(self.showstdrtnp)
        # Connecting staff renew page back button to return staff page
        self.renewstfbcbtn.clicked.connect(self.showstfrtnp)
        # Connecting main page view issued button member selection page
        self.viewissubk.clicked.connect(self.showisdmm)
        # Connecting issue member selection page back button to main page
        self.viewmmisdbcbtn.clicked.connect(self.showpanel)
        # Connecting logout button to login page
        self.logoutbtn.clicked.connect(self.logoutfun)

    # ==========================================================================
        # When PhoneNo text is changed then only number function is called
        self.adstafphno.textChanged.connect(self.onlynumber)
        self.adstudphno.textChanged.connect(self.onlynumberr)
    # ============================================================================================
        # When searchbook combobox text is changed to department this function will be called
        self.searchbkcombo.currentTextChanged.connect(self.searchbkcomboview)
        self.searchstfcombo.currentTextChanged.connect(self.searchstfcomboview)
        self.searchstdcombo.currentTextChanged.connect(self.searchstdcomboview)
    # ============================================================================================
        # When searchbook page back button is pressed the setsearchcombobktxt should be called
        self.searchbbcbtn.clicked.connect(self.setsearchbkcombotxt)

        # ============================================================================================
        # When searchmember page back button is pressed the setsearchcombomemtxt should be called
        self.searchmbcbtn.clicked.connect(self.setsearchmemcombotxt)

        # Making the login page visible
        self.stackedWidget.setCurrentWidget(self.loginpage)
        # Connecting login button to login function
        self.logbtn.clicked.connect(self.login)  

    # ================================================================================================
        # Connecting main Functions
        # Connecting add book button to addbook function
        self.adbtn.clicked.connect(lambda:Addbook.addbookfun(self))
        # Connecting delete book button to Deletebook function
        self.deletebkbtn.clicked.connect(lambda:Deletebk.Deletebook(self))
        # Connecting view all book button to viewbook function
        self.adispallbook.clicked.connect(lambda:ViewBook.viewbookfun(self))
        # Connecting add staff button to addstaff function
        self.adstafbtn.clicked.connect(lambda:Addstaff.addstaffun(self))
        # Connecting searchbook button to searchbook function
        self.searchbkbtn.clicked.connect(lambda:SearchBook.searchbkfun(self))
        # Connecting searchstaff button to searchstaff function
        self.searchstfbtn.clicked.connect(lambda:SearchStaff.searchstffun(self))
        # Connecting searchstaff button to searchstaff function
        self.searchstdbtn.clicked.connect(lambda:SearchStud.searchstdfun(self))
        # Connecting add student button to addstud function
        self.adstudbtn.clicked.connect(lambda:Addstudent.addstudfun(self))
        # Connecting delete staff button to Deletestaff function
        self.deletestfbtn.clicked.connect(lambda:Deletestf.Deletestaff(self))
        # Connecting delete student button to Deletestudent function
        self.deletestdbtn.clicked.connect(lambda:Deletestd.Deletestudent(self))
        # Connecting view all staff button to viewstaff function
        self.viewstaff.clicked.connect(lambda:Viewstaff.viewstafffun(self))
         # Connecting view all student button to viewstudent function
        self.viewstud.clicked.connect(lambda:Viewstud.viewstudfun(self))
        # Connecting Issue Staff page issue button to runissuestf function
        self.isstfbtn.clicked.connect(self.runissuestf)
        # Connecting Issue Stud page issue button to runissuestd function
        self.isstdbtn.clicked.connect(self.runissuestd)
        # Connecting Return Stud page return button to studreturnval function
        self.returnstud.clicked.connect(self.studreturnval)
        # Connecting Return Staff page return button to staffreturnval function
        self.returnstaff.clicked.connect(self.staffreturnval)
        # Connecting renew stud button to renew stud function
        self.renewstudbtn.clicked.connect(lambda:RenewStud.renewstudfun(self))
        # Connecting renew staff button to renew stud function
        self.renewstafbtn.clicked.connect(lambda:RenewStaff.renewstaffun(self))
        # Connecting issue member selection page staff button viewisstffun
        self.viewstaffisd.clicked.connect(lambda:ViewIsstf.viewisstffun(self))
        # Connecting issue member selection page staff button viewisstdfun
        self.viewstudisd.clicked.connect(lambda:ViewIsstd.viewisstdfun(self))
        # Connecting search issued student button to searchissuedvalidatestd function
        self.rtnstdfine.clicked.connect(self.searchissuedvalidatestd)
        # Connecting search issued staff button to searchissuedvalidatestf function
        self.rtnstdfine_2.clicked.connect(self.searchissuedvalidatestf)      
        
# =======================================================================================================================================================
# Setting UI icons and background,text and effects
        self.label.setStyleSheet("image:url(iconsc/storytelling.png)")
        self.logoutbtn.setIcon(QIcon("iconsc/logoutt.png"))
        self.logoutbtn.setIconSize(QSize(30,30))        
        self.loginpage.setStyleSheet("QWidget#loginpage{border-image : url(bgg/topbook.jpg)}")
        self.adwidget.setStyleSheet("QWidget#adwidget{border-image : url(bgg/topbook.jpg)}")
        self.lgiconlb.setStyleSheet("QLabel#lgiconlb{image:url(icons/user-6-line.svg)}")
        self.dlbcbtn.setIcon(QIcon("icons/arrow.png"))
        self.dlbcbtn.setIconSize(QSize(30,30))
        self.stafstudpbcbtn.setIcon(QIcon("icons/arrow.png"))
        self.stafstudpbcbtn.setIconSize(QSize(30,30))
        self.searchmbcbtn.setIcon(QIcon("icons/arrow.png"))
        self.searchmbcbtn.setIconSize(QSize(30,30))
        self.ismmbcbtn.setIcon(QIcon("icons/arrow.png"))
        self.ismmbcbtn.setIconSize(QSize(30,30))
        self.rtnbcbtn.setIcon(QIcon("icons/arrow.png"))
        self.rtnbcbtn.setIconSize(QSize(30,30))
        self.renewstdbcbtn.setIcon(QIcon("icons/arrow.png"))
        self.renewstdbcbtn.setIconSize(QSize(30,30))
        self.renewstfbcbtn.setIcon(QIcon("icons/arrow.png"))
        self.renewstfbcbtn.setIconSize(QSize(30,30))
        self.viewmmisdbcbtn.setIcon(QIcon("icons/arrow.png"))
        self.viewmmisdbcbtn.setIconSize(QSize(30,30))
    # ============================================================================================================================
        self.adispallbook.setIcon(QIcon("iconsc/bookshelf.png"))
        self.adispallbook.setIconSize(QSize(175,175))
        self.adispallbook.setText("View all Books")
        self.adispallbook.setStyleSheet("QToolButton#adispallbook{Padding-top:75px;border-radius:20px;background-color: #FADCD9;}QToolButton#adispallbook:pressed{margin-top:3px;};")
        self.adispallbook.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
    # ============================================================================================================================
        self.adispallmem.setIcon(QIcon("iconsc/groupp.png"))
        self.adispallmem.setText("View All Members")
        self.adispallmem.setIconSize(QSize(175,175))
        self.adispallmem.setStyleSheet("QToolButton#adispallmem{Padding-top:75px;border-radius:20px;background-color: #FADCD9;}QToolButton#adispallmem:pressed{margin-top:3px;};")
        self.adispallmem.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
    # =============================================================================================================================
        self.adbook.setIcon(QIcon("iconsc/bookp.png"))
        self.adbook.setIconSize(QSize(60,65))
        self.adbook.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.adbook.setStyleSheet("QToolButton#adbook{Padding-left:15px;border-radius:20px;background-color: #FADCD9;}QToolButton#adbook:pressed{margin-top:1px;};")
    # =============================================================================================================================
        self.asearchbook.setIcon(QIcon("iconsc/bookg.png"))
        self.asearchbook.setIconSize(QSize(100,100))
        self.asearchbook.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.asearchbook.setStyleSheet("QToolButton#asearchbook{Padding-top:15px;border-radius:20px;background-color: #FADCD9;}QToolButton#asearchbook:pressed{margin-top:1px;};")
    # =============================================================================================================================
        self.deletebk.setIcon(QIcon("iconsc/deleteee.png"))
        self.deletebk.setIconSize(QSize(105,105))
        self.deletebk.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.deletebk.setStyleSheet("QToolButton#deletebk{Padding-top:15px;border-radius:20px;background-color: #FADCD9;}QToolButton#deletebk:pressed{margin-top:1px;};")
    # =============================================================================================================================
        self.adstaff.setIcon(QIcon("iconsc/steward.png"))
        self.adstaff.setIconSize(QSize(60,60))
        self.adstaff.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.adstaff.setStyleSheet("QToolButton#adstaff{Padding-left:15px;border-radius:20px;background-color: #FADCD9;}QToolButton#adstaff:pressed{margin-top:1px;};")
    # =============================================================================================================================
        self.adstud.setIcon(QIcon("iconsc/usertp.png"))
        self.adstud.setIconSize(QSize(60,60))
        self.adstud.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.adstud.setStyleSheet("QToolButton#adstud{Padding-left:15px;border-radius:20px;background-color: #FADCD9;}QToolButton#adstud:pressed{margin-top:1px;};")
    # =============================================================================================================================
        self.searchmm.setIcon(QIcon("iconsc/srch.png"))
        self.searchmm.setIconSize(QSize(100,100))
        self.searchmm.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.searchmm.setStyleSheet("QToolButton#searchmm{Padding-top:15px;border-radius:20px;background-color: #FADCD9;}QToolButton#searchmm:pressed{margin-top:1px;};")
    # =============================================================================================================================
        self.returnbk.setIcon(QIcon("iconsc/hand-over.png"))
        self.returnbk.setIconSize(QSize(100,100))
        self.returnbk.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.returnbk.setStyleSheet("QToolButton#returnbk{Padding-top:15px;border-radius:20px;background-color: #FADCD9;}QToolButton#returnbk:pressed{margin-top:1px;};")
    # =============================================================================================================================
        self.issuebk.setIcon(QIcon("iconsc/hand-over.png"))
        self.issuebk.setIconSize(QSize(100,100))
        self.issuebk.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.issuebk.setStyleSheet("QToolButton#issuebk{Padding-top:15px;border-radius:20px;background-color: #FADCD9;}QToolButton#issuebk:pressed{margin-top:1px;};")
     # =============================================================================================================================
        self.viewissubk.setIcon(QIcon("iconsc/hand-over.png"))
        self.viewissubk.setIconSize(QSize(100,100))
        self.viewissubk.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.viewissubk.setStyleSheet("QToolButton#viewissubk{Padding-top:15px;border-radius:20px;background-color: #FADCD9;}QToolButton#viewissubk:pressed{margin-top:1px;};") 
     # =============================================================================================================================
        self.viewstaff.setIcon(QIcon("iconsc/teacher.png"))
        self.viewstaff.setIconSize(QSize(175,175))
        self.viewstaff.setText("View all Staffs")
        self.viewstaff.setStyleSheet("QToolButton#viewstaff{Padding-top:75px;border-radius:20px;background-color: #FADCD9;}QToolButton#viewstaff:pressed{margin-top:3px;};")
        self.viewstaff.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
     # =============================================================================================================================
        self.viewstud.setIcon(QIcon("iconsc/graduated.png"))
        self.viewstud.setIconSize(QSize(175,175))
        self.viewstud.setText("View all Students")
        self.viewstud.setStyleSheet("QToolButton#viewstud{Padding-top:75px;border-radius:20px;background-color: #FADCD9;}QToolButton#viewstud:pressed{margin-top:3px;};")
        self.viewstud.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
     # =============================================================================================================================
        self.viewstaffisd.setIcon(QIcon("iconsc/teacher.png"))
        self.viewstaffisd.setIconSize(QSize(175,175))
        self.viewstaffisd.setText("View Issued Staffs")
        self.viewstaffisd.setStyleSheet("QToolButton#viewstaffisd{Padding-top:75px;border-radius:20px;background-color: #FADCD9;}QToolButton#viewstaffisd:pressed{margin-top:3px;};")
        self.viewstaffisd.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
     # =============================================================================================================================
        self.viewstudisd.setIcon(QIcon("iconsc/graduated.png"))
        self.viewstudisd.setIconSize(QSize(175,175))
        self.viewstudisd.setText("View Issued Students")
        self.viewstudisd.setStyleSheet("QToolButton#viewstudisd{Padding-top:75px;border-radius:20px;background-color: #FADCD9;}QToolButton#viewstudisd:pressed{margin-top:3px;};")
        self.viewstudisd.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
     # =============================================================================================================================
       
# =========================================================================================================================================================
        self.tableWidget.setStyleSheet("background-color:#FADCD9;border:none;border-radius:20px;")
        self.tableWidget.setAlternatingRowColors(True)  # Alternate row colors
        #F79489;
        #FADCD9;
        #'alternate-background-color:#F79489;'
        # QHeaderView::section {background-color:#FADCD9;}
        # QHeaderView::section {background-color: rgb(100, 100, 100); color: rgb(200, 200, 200);}
# =========================================================================================================================================================
    # Shadow effect 
        # Creating object of shadoweffect
        shadow = QGraphicsDropShadowEffect()
        # setting blur radius (optional)
        shadow.setBlurRadius(20)
        shadow.setOffset(3)

        # Creating object of shadoweffect
        shadoww = QGraphicsDropShadowEffect()
        # setting blur radius (optional)
        shadoww.setBlurRadius(20)
        shadoww.setOffset(3)

        # Creating object of shadoweffect
        shadow1 = QGraphicsDropShadowEffect()
        # setting blur radius (optional)
        shadow1.setBlurRadius(20)
        shadow1.setOffset(2)

        # Creating object of shadoweffect
        shadow2 = QGraphicsDropShadowEffect()
        # setting blur radius (optional)
        shadow2.setBlurRadius(20)
        shadow2.setOffset(2)

        # Creating object of shadoweffect
        shadow3 = QGraphicsDropShadowEffect()
        # setting blur radius (optional)
        shadow3.setBlurRadius(20)
        shadow3.setOffset(3)
        # self.shadow.setColor(Qt.yellow)

        # self.deletebk.setGraphicsEffect(QGraphicsDropShadowEffect())
        # self.adbook.setGraphicsEffect(shadow)
        # self.deletebk.setGraphicsEffect(shadow)
        # self.issuebk.setGraphicsEffect(shadow)
        # self.adstaff.setGraphicsEffect(shadow)
        # self.adstud.setGraphicsEffect(shadow)
        # self.returnbk.setGraphicsEffect(shadow)
        # self.asearchbook.setGraphicsEffect(shadow)
        # self.searchmm.setGraphicsEffect(shadow)
        # self.viewissubk.setGraphicsEffect(shadow)
        self.adispallbook.setGraphicsEffect(shadow)
        self.adispallmem.setGraphicsEffect(shadoww)
        self.stackedWidget_2.setGraphicsEffect(shadow1)
        self.label_2.setGraphicsEffect(shadow2)
        self.tableWidget.setGraphicsEffect(shadow3)
    # =============================================================================================================================
        # self.opacity=QGraphicsOpacityEffect()
        # self.opacity.setOpacity(0.2)
        # self.widget.setGraphicsEffect(self.opacity)
# ==========================================================================================================================================

    # Set alphabet only validation to certain textboxes==========================================================

        # Create regular expression and set it to object
        reg_ex = QRegExp("^[A-Za-z]+$")
        # pass the reg_ex object to regular expression validator
        input_validator = QRegExpValidator(reg_ex)
        # pass the input_validator object to textboxes
        self.adstafirst.setValidator(input_validator)
        self.adstaflast.setValidator(input_validator)
        self.adstudfirst.setValidator(input_validator)
        self.adstudlast.setValidator(input_validator)

    # Set no special character validation========================================================================

        reg_exx=QRegExp("^[A-Za-z0-9]+$")
        input_validatorr = QRegExpValidator(reg_exx)
        self.adbkshelfno.setValidator(input_validatorr)
        self.bkidtxt.setValidator(input_validatorr)
        self.stddelidtxt.setValidator(input_validatorr)
        self.stfdelidtxt.setValidator(input_validatorr)
        self.adstafid.setValidator(input_validatorr)
        self.adbkid.setValidator(input_validatorr)
        # self.isstfid.setValidator(input_validatorr)
        self.isstfstafid.setValidator(input_validatorr)
        self.isstfbkid.setValidator(input_validatorr)
        # self.isstdid.setValidator(input_validatorr)
        self.isstdstudid.setValidator(input_validatorr)
        self.isstdbkid.setValidator(input_validatorr)
        self.searchbktxt.setValidator(input_validatorr)
        self.searchstftxt.setValidator(input_validatorr)
        self.searchstdtxt.setValidator(input_validatorr)

    # Set only alphabet,comma and space validation(For Author)==================================================================================

        reg_exxx=QRegExp("^[A-Za-z, ]+$")
        input_validatorrr = QRegExpValidator(reg_exxx)
        self.adbkauth.setValidator(input_validatorrr)

    # Set only alphabet and space validation(For Book Name)==================================================================================


        # Create regular expression and set it to object
        reg_ext = QRegExp("^[A-Za-z ]+$")
        # pass the reg_ex object to regular expression validator
        input_validatort = QRegExpValidator(reg_ext)
        # pass the input_validator object to textboxes
        self.adbkname.setValidator(input_validatort)

    # Set No Special Character except for space validation(For Book Search text)==================================================================================
        # Create regular expression and set it to object
        reg_extg = QRegExp("^[A-Za-z0-9 ]+$")
        # pass the reg_ex object to regular expression validator
        input_validatortg = QRegExpValidator(reg_extg)
        # pass the input_validator object to textboxes
        self.searchbktxt.setValidator(input_validatortg)

    # Set Only Digits validation(For Student Rollno)==================================================================================
        # Create regular expression and set it to object
        reg_extgi = QRegExp("^[0-9]+$")
        # pass the reg_ex object to regular expression validator
        input_validatortgi = QRegExpValidator(reg_extgi)
        # pass the input_validator object to textboxes
        self.adstudroll.setValidator(input_validatortgi)

# ==========================================================================================================================================

    # Set header font to 11 of tableWidget
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.horizontalHeader().setFont(font)

# =========================================================================================================================================

    #  Adding items to adstaff page combobox
        self.adstafcombo.addItem("Arts")
        self.adstafcombo.addItem("Commerce")
        self.adstafcombo.addItem("Biology")
        self.adstafcombo.addItem("Physics")
        self.adstafcombo.addItem("Zoology")
        self.adstafcombo.addItem("Mathematics")
        self.adstafcombo.addItem("Chemistry")
        self.adstafcombo.addItem("Computer Science")
        self.adstafcombo.addItem("Hindi")
        self.adstafcombo.addItem("Kannada")
        self.adstafcombo.addItem("English")
        self.adstafcombo.addItem("Sanskrit")
        self.adstafcombo.addItem("Non Teaching")

# ==========================================================================================================================================

    # Function to make the other combobox visible when searchbkcombo text is changed to department
    def searchbkcomboview(self):
        if self.searchbkcombo.currentIndex()==3:
            self.searchbktxtcombo.setHidden(False)
        else:
            self.searchbktxtcombo.setHidden(True)

# ==========================================================================================================================================

    # Function to make the other combobox visible when searchstfcombo text is changed to department
    def searchstfcomboview(self):
        if self.searchstfcombo.currentIndex()==2:
            self.searchstftxtcombo.setHidden(False)
        else:
            self.searchstftxtcombo.setHidden(True)
            
# ============================================================================================================================================
    # Function to make the other combobox visible when searchstdcombo text is changed to course
    def searchstdcomboview(self):
        if self.searchstdcombo.currentIndex()==2:
            self.searchstdtxtcombo.setHidden(False)
        else:
            self.searchstdtxtcombo.setHidden(True)          
#==========================================================================================================================================================
    # Function to set searchbkcombo index to 0
    def setsearchbkcombotxt(self):
        self.searchbkcombo.setCurrentIndex(0)
#==========================================================================================================================================================
    # Function to set searchstfcombo index to 0
    def setsearchmemcombotxt(self):
        self.searchstfcombo.setCurrentIndex(0)
        self.searchstdcombo.setCurrentIndex(0)
#==========================================================================================================================================================
    # Function to validate phno text 
    def onlynumber(self):
        if len(self.adstafphno.text())<=10:
            if not self.adstafphno.text().isnumeric():
                self.adstafphno.setText(self.adstafphno.text()[:-1])
        else:
             self.adstafphno.setText(self.adstafphno.text()[:-1])

    def onlynumberr(self):
        if len(self.adstudphno.text())<=10:
            if not self.adstudphno.text().isnumeric():
                self.adstudphno.setText(self.adstudphno.text()[:-1])
        else:
             self.adstudphno.setText(self.adstudphno.text()[:-1])
#===========================================================================================================================================
# Function to set current widget to deletebookpage
    def showdelbkpage(self):
        self.stackedWidget_2.setCurrentWidget(self.deletebookpage)
# Function to set current widget to addbook page
    def showaddpage(self):
        self.stackedWidget_2.setCurrentWidget(self.adbookp)
# Function to set current widget to main panel
    def showpanel(self):
        self.stackedWidget_2.setCurrentWidget(self.mainp)
        self.invalidlb.setHidden(True)
        self.invalidbk.setHidden(True)
        self.delbsucesslb.setHidden(True)
        self.adbsucesslb.setHidden(True)
        self.adbexist.setHidden(True)
        self.adbkemp.setHidden(True)
        self.delbemp.setHidden(True)
        self.adstudexist.setHidden(True)
        self.adstudsucess.setHidden(True)
        self.adstudemp.setHidden(True)
        self.adstafemp.setHidden(True)
        self.adstafexist.setHidden(True)
        self.adstafsucesslb.setHidden(True)
        self.searchbktxtcombo.setHidden(True)
        self.searchstftxtcombo.setHidden(True)
        self.searchstdtxtcombo.setHidden(True)
        self.delstfemp.setHidden(True)
        self.invalidstf.setHidden(True)
        self.delstfsucesslb.setHidden(True)
        self.delstdemp.setHidden(True)
        self.delstdsucesslb.setHidden(True)
        self.invalidstd.setHidden(True)
        self.searchbkemp.setHidden(True)
        self.searchstfemp.setHidden(True)
        self.searchstdemp.setHidden(True)
        self.isstfemp.setHidden(True)
        self.isstdemp.setHidden(True)
        self.returnstudemp_2.setHidden(True)
        self.returnstudemp_3.setHidden(True)
        self.returnstaffemp.setHidden(True)
        self.returnstudemp.setHidden(True)
        # Set Quantity label 0
        self.qtylb.setText("0")


# Functions to set different pages

    def showadminpanel(self):
        self.stackedWidget.setCurrentWidget(self.adminpanel)
    def showaddstafpage(self):
        self.stackedWidget_2.setCurrentWidget(self.adstaffp)
    def showaddstudpage(self):
        self.stackedWidget_2.setCurrentWidget(self.adstudp)
    def showstafstudselpage(self):
        self.stackedWidget_2.setCurrentWidget(self.stafstudp)
    def showbooksearchp(self):
        self.stackedWidget_2.setCurrentWidget(self.searchbookp)


    def showstfdelp(self):
        self.stackedWidget_3.setCurrentWidget(self.stafdelp)
        self.delstfemp.setHidden(True)
        self.invalidstf.setHidden(True)
        self.delstfsucesslb.setHidden(True)
    
    def showstddelp(self):
        self.stackedWidget_3.setCurrentWidget(self.studentdelp)
        self.delstdemp.setHidden(True)
        self.invalidstd.setHidden(True)
        self.delstdsucesslb.setHidden(True)

    def showsearchmemberp(self):
        self.stackedWidget_2.setCurrentWidget(self.searchmemberp)
    
    def showstfsearchp(self):
        self.searchstfemp.setHidden(True)
        self.stackedWidget_4.setCurrentWidget(self.page)

    def showstdsearchp(self):
        self.searchstdemp.setHidden(True)
        self.stackedWidget_4.setCurrentWidget(self.page_2)

    def showissuep(self):
        self.stackedWidget_2.setCurrentWidget(self.issuep)

    def showstfissuep(self):
        self.stackedWidget_5.setCurrentWidget(self.page_3)

    def showstdissuep(self):
        self.stackedWidget_5.setCurrentWidget(self.page_4)

    def showreturnp(self):
        self.stackedWidget_2.setCurrentWidget(self.returnp)
    
    def showstdrtnp(self):
        self.returnstudemp.setHidden(True)
        self.returnstudemp_2.setHidden(True)
        self.rtnbcbtn.setHidden(False)
        self.selstfbtn_4.setHidden(False)
        self.selstdbtn_4.setHidden(False)
        self.stackedWidget_6.setCurrentWidget(self.rtnstudp)
    
    def showstfrtnp(self):
        self.returnstaffemp.setHidden(True)
        self.returnstudemp_3.setHidden(True)
        self.rtnbcbtn.setHidden(False)
        self.selstfbtn_4.setHidden(False)
        self.selstdbtn_4.setHidden(False)
        self.stackedWidget_6.setCurrentWidget(self.rtnstaffp)

    def showisdmm(self):
        self.stackedWidget_2.setCurrentWidget(self.viewmmisdp)

    def logoutfun(self):
        self.stackedWidget.setCurrentWidget(self.loginpage)
        self.invalidlb.setHidden(True)
        self.tableWidget.clear()
        self.usertext.clear()
        self.usertext.setFocus()
        self.passtext.clear()
        self.stackedWidget_2.setCurrentWidget(self.mainp)
        # Automatically calling view all book function when the app is opened
        ViewBook.viewbookfun(self)


    def showstudrenewp(self):
        v='no'
        # This funcion also validates the buttons
        stdid=self.rtnstudtxt.text()
        cn=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cr=cn.cursor()
        chk="select * from issuestud where IssuedBID='%s' and returned='%s'"
        ar=(stdid,v)
        cr.execute(chk%ar)
        ckk=cr.rowcount
        if stdid=='':
            self.returnstudemp.setHidden(False)
            self.returnstudemp.setStyleSheet("color: rgb(232, 0, 0);") 
            self.returnstudemp.setText("Details cannot be empty")
            self.returnstudemp.adjustSize()
        elif ckk>=1:
            # retrieve issue date 
            sql="select IssuedDate from issuestud where IssuedBID='%s' and returned='%s' "
            arg=(stdid,v)
            cr.execute(sql%arg)
            oisiddd=cr.fetchone()[0]
            # Convert it to date type
            oisidd=parser.parse(oisiddd)
            # This converts it to back  to date
            oisidd=oisidd.date()

            # retrieve return date 
            sql="select ReturnDate from issuestud where IssuedBID='%s' and returned='%s' "
            arg=(stdid,v)
            cr.execute(sql%arg)
            ortnddd=cr.fetchone()[0]
            # Convert it to date type
            ortndd=parser.parse(ortnddd)
            # This converts it to back  to date
            ortndd=ortndd.date()

            # =======================================================================================================
            # get the current date
            currentdate=str(date.today())
            cdate=parser.parse(currentdate)
            cdtt=cdate.date()
            # if issuedate and currentdate are same
            if oisidd==cdtt:
                self.returnstudemp.setHidden(False)
                self.returnstudemp.setStyleSheet("color: rgb(232, 0, 0);")
                self.returnstudemp.setText("Cannot renew book today itself")
                self.returnstudemp.adjustSize()

            elif cdtt<ortndd:
                self.returnstudemp.setHidden(False)
                self.returnstudemp.setStyleSheet("color: rgb(232, 0, 0);")
                self.returnstudemp.setText("Cannot renew book ")
                self.returnstudemp.adjustSize()


            else:
                # Get current date
                currentdate=str(date.today())
                # Convert it to date format
                cdate=parser.parse(currentdate)
                # Current date
                isdt=cdate.date()
                # ==================================
                rtndt = isdt
                rtndt += timedelta(days=7)
                self.renewstddate.setDate(rtndt)
                self.stackedWidget_6.setCurrentWidget(self.renewstudp)
                self.rtnbcbtn.setHidden(True)
                self.selstfbtn_4.setHidden(True)
                self.selstdbtn_4.setHidden(True)
        else:
            self.rtnstudtxt.clear()
            self.returnstudemp.setHidden(False)
            self.returnstudemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstudemp.setText("No such record exists")
            self.returnstudemp.adjustSize()

        cr.close()
        cn.close()
    
    def showstafrenewp(self):
        v='no'
        # This funcion also validates the buttons
        stdid=self.rtnstafftxt.text()
        cn=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cr=cn.cursor()
        chk="select * from issuestaff where IssuedBID='%s' and returned='%s'"
        ar=(stdid,v)
        cr.execute(chk%ar)
        ckk=cr.rowcount
        if stdid=='':
            self.returnstaffemp.setHidden(False)
            self.returnstaffemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstaffemp.setText("Details cannot be empty")
            self.returnstaffemp.adjustSize()

        elif ckk>=1:
            # retrieve issue date 
            sql="select IssuedDate from issuestaff where IssuedBID='%s' and returned='%s' "
            arg=(stdid,v)
            cr.execute(sql%arg)
            oisiddd=cr.fetchone()[0]
            # Convert it to date type
            oisidd=parser.parse(oisiddd)
            # This converts it to back  to date
            oisidd=oisidd.date()

            # retrieve return date 
            sql="select ReturnDate from issuestaff where IssuedBID='%s' and returned='%s' "
            arg=(stdid,v)
            cr.execute(sql%arg)
            ortnddd=cr.fetchone()[0]
            # Convert it to date type
            ortndd=parser.parse(ortnddd)
            # This converts it to back  to date
            ortndd=ortndd.date()

            # ==============================================s=========================================================
            # get the current date
            currentdate=str(date.today())
            cdate=parser.parse(currentdate)
            cdtt=cdate.date()
            # if issuedate and currentdate are same
            if oisidd==cdtt:
                self.returnstaffemp.setHidden(False)
                self.returnstaffemp.setStyleSheet("color: rgb(232, 0, 0);")
                self.returnstaffemp.setText("Cannot renew book today itself")
                self.returnstaffemp.adjustSize()
            elif cdtt<ortndd:
                self.returnstaffemp.setHidden(False)
                self.returnstaffemp.setStyleSheet("color: rgb(232, 0, 0);")
                self.returnstaffemp.setText("Cannot renew book ")
                self.returnstaffemp.adjustSize()             
            else:
                # Get current date
                currentdate=str(date.today())
                # Convert it to date format
                cdate=parser.parse(currentdate)
                # Current date
                isdt=cdate.date()
                # ==================================
                rtndt = isdt
                rtndt += timedelta(days=7)
                self.renewstfdate.setDate(rtndt)
                self.stackedWidget_6.setCurrentWidget(self.renewstafp)
                self.rtnbcbtn.setHidden(True)
                self.selstfbtn_4.setHidden(True)
                self.selstdbtn_4.setHidden(True)
        else:
            self.rtnstafftxt.clear()
            self.returnstaffemp.setHidden(False)
            self.returnstaffemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstaffemp.setText("No such record exists")
            self.returnstaffemp.adjustSize()
        cr.close()
        cn.close()

    def searchissuedvalidatestd(self):
        v='no'
        # This funcion validates the buttons==========
        # Get input
        srch=self.rtnstudtxt.text()
        cn=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cr=cn.cursor()
        chk="select * from issuestud where Issuedstud='%s'"
        ar=(srch)
        cr.execute(chk%ar)
        if srch=='':
            self.returnstudemp.setHidden(False)
            self.returnstudemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstudemp.setText("Details cannot be empty")
            self.returnstudemp.adjustSize()
        elif cr.rowcount>=1:      
            Searchisstd.searchisstdfun(self)
        else:
            self.rtnstudtxt.clear()
            self.returnstudemp.setHidden(False)
            self.returnstudemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstudemp.setText("No such record exists")
            self.returnstudemp.adjustSize()

            # self.tableWidget.clear()
            # Setting horizontal header labels
            self.tableWidget.setHorizontalHeaderLabels(["IssueID","StudentID","BookID","IssuedDate","ExpectedReturnDate","Fine","Renewals","ReturnDate","Returned",])
        
        cr.close()
        cn.close()

    def searchissuedvalidatestf(self):
        v='no'
        # This funcion validates the buttons==========
        # Get input
        srch=self.rtnstafftxt.text()
        cn=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cr=cn.cursor()
        chk="select * from issuestaff where Issuedstaff='%s'"
        ar=(srch)
        cr.execute(chk%ar)
        if srch=='':
            self.returnstaffemp.setHidden(False)
            self.returnstaffemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstaffemp.setText("Details cannot be empty")
            self.returnstaffemp.adjustSize()
        elif cr.rowcount>=1:   
            Searchisstf.searchisstffun(self)
        else:
            self.rtnstafftxt.clear()
            self.returnstaffemp.setHidden(False)
            self.returnstaffemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstaffemp.setText("No such record exists")
            self.returnstaffemp.adjustSize()

            # self.tableWidget.clear()
            # Setting horizontal header labels
            # self.tableWidget.setHorizontalHeaderLabels(["IssueID","StaffID","BookID","IssuedDate","ExpectedReturnDate","ReturnDate","Returned"])

        cr.close()
        cn.close()

    def studreturnval(self):
        # This funcion validates the buttons==========
        v='no'
        # Get input
        srch=self.rtnstudtxt.text()
        cn=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cr=cn.cursor()
        chk="select * from issuestud where IssuedBID='%s' and returned='%s'"
        ar=(srch,v)
        cr.execute(chk%ar)
        if srch=='':
            self.returnstudemp.setHidden(False)
            self.returnstudemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstudemp.setText("Details cannot be empty")
            self.returnstudemp.adjustSize()
        elif cr.rowcount>=1:   
            Returnstud.rtnstudfun(self)
        else:
            self.rtnstudtxt.clear()
            self.returnstudemp.setHidden(False)
            self.returnstudemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstudemp.setText("No such record exists")
            self.returnstudemp.adjustSize()

            # self.tableWidget.clear()
            # # Setting horizontal header labels
            self.tableWidget.setHorizontalHeaderLabels(["IssueID","StudentID","BookID","IssuedDate","ReturnDate","Fine","Renewals"])

        cr.close()
        cn.close()

    def staffreturnval(self):
        v='no'
        # This funcion validates the buttons==========
        # Get input
        srch=self.rtnstafftxt.text()
        cn=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cr=cn.cursor()
        chk="select * from issuestaff where IssuedBID='%s' and returned='%s'"
        ar=(srch,v)
        cr.execute(chk%ar)
        if srch=='':
            self.returnstaffemp.setHidden(False)
            self.returnstaffemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstaffemp.setText("Details cannot be empty")
            self.returnstaffemp.adjustSize()
        elif cr.rowcount>=1:            
            Returnstaff.rtnstafffun(self)
        else:
            self.rtnstafftxt.clear()
            self.returnstaffemp.setHidden(False)
            self.returnstaffemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstaffemp.setText("No such record exists")
            self.returnstaffemp.adjustSize()
            # self.tableWidget.clear()
            # # Setting horizontal header labels
            # self.tableWidget.setHorizontalHeaderLabels(["IssueID","StaffID","BookID","IssuedDate","ReturnDate","Renewals"])

        cr.close()
        cn.close()

    def runissuestd(self):
        # sets the validations
        istd=self.isstdstudid.text()
        bkid=self.isstdbkid.text()

        v='yes'

        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()

        # Get detail from student where rollno=given input
        sqlstdchk="select * from student where rollno='%s' and Visible='%s'"
        argstdchk=(istd,v)
        cursor.execute(sqlstdchk%argstdchk)
        # Store the detail in variable
        stdchk=cursor.rowcount
          
        # Get detail from Book where BookID=given input
        sqlbkidchk="select * from book where BookID='%s' and Visible='%s'"
        argbkidchk=(bkid,v)
        cursor.execute(sqlbkidchk%argbkidchk)
        # Store the detail in variable
        bkidchk=cursor.rowcount

        if istd=='' or bkid=='':
            self.isstdemp.setHidden(False)
            self.isstdemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstdemp.setText("Details cannot be empty")
            self.isstdemp.adjustSize()

        elif stdchk<1:
            self.isstdemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstdemp.setText("Student does not exist")
            self.isstdemp.adjustSize()
            self.isstdemp.setHidden(False)
            self.isstdstudid.clear()
   

        elif bkidchk<1:
            self.isstdemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstdemp.setText("Book does not exist")
            self.isstdemp.adjustSize()
            self.isstdemp.setHidden(False)
            self.isstdbkid.clear()

        elif stdchk<1 and bkidchk<1:
            self.isstdemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstdemp.setText("Book and student do not exist")
            self.isstdemp.adjustSize()
            self.isstdemp.setHidden(False)
            self.isstdstudid.clear()
            self.isstdbkid.clear()

        else:
            self.isstdemp.setHidden(True)
            Issuestud.issuestdfun(self)

    def runissuestf(self):
        # sets the validations
        istd=self.isstfstafid.text()
        bkid=self.isstfbkid.text()

        v='yes'

        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()

        # Get detail from student where rollno=given input
        sqlstdchk="select * from staff where StaffID='%s' and Visible='%s'"
        argstdchk=(istd,v)
        cursor.execute(sqlstdchk%argstdchk)
        # Store the detail in variable
        stdchk=cursor.rowcount
          
        # Get detail from Book where BookID=given input
        sqlbkidchk="select * from book where BookID='%s' and Visible='%s'"
        argbkidchk=(bkid,v)
        cursor.execute(sqlbkidchk%argbkidchk)
        # Store the detail in variable
        bkidchk=cursor.rowcount

        if istd=='' or bkid=='':
            self.isstfemp.setHidden(False)
            self.isstfemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstfemp.setText("Details cannot be empty")
            self.isstfemp.adjustSize()

        elif stdchk<1:
            self.isstfemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstfemp.setText("Staff does not exist")
            self.isstfemp.adjustSize()
            self.isstfemp.setHidden(False)
            self.isstfstafid.clear()
   

        elif bkidchk<1:
            self.isstfemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstfemp.setText("Book does not exist")
            self.isstfemp.adjustSize()
            self.isstfemp.setHidden(False)
            self.isstfbkid.clear()

        elif stdchk<1 and bkidchk<1:
            self.isstfemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstfemp.setText("Book and staff do not exist")
            self.isstfemp.adjustSize()
            self.isstfemp.setHidden(False)
            self.isstfstafid.clear()
            self.isstfbkid.clear()

        else:
            self.isstfemp.setHidden(True)
            Issuestaff.issuestffun(self)

    # def show(self):
    #     self.mainwin.show()

    # Login function
    def login(self):
        aname=self.usertext.text()
        apass=self.passtext.text()
        daname='admin'
        dapass='1234'
        if aname==daname and apass==dapass:
            self.showadminpanel()
            # Automatically calling view all book function when the app is opened
            ViewBook.viewbookfun(self)
        else:
            self.invalidlb.setHidden(False)
            self.usertext.clear()
            self.passtext.clear()
            self.usertext.setFocus()

# Necessary to display UI
app = QtWidgets.QApplication(argv)
Mainwindow = QtWidgets.QMainWindow()
ui = MainWindow(Mainwindow)
Mainwindow.show()
app.exec()




