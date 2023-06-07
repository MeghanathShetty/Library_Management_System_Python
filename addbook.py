import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
import mysql.connector

class Addbook():
    # Add book function
    def addbookfun(self):

        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()

        # Getting data from line editors then setting them to variables
        bid=self.adbkid.text()
        btitle=self.adbkname.text()
        bauth=self.adbkauth.text()
        shelfno=self.adbkshelfno.text()
        # Setting available to av
        av="Available"
        # Getting selected text from combobox(Department)
        dpt=self.adbkcombo.currentText()
        # setting visible to yes
        v='yes'

        sql="select * from book where BookID='%s' and Visible='%s'"
        arg=(bid,v)
        cursor.execute(sql%arg)
        rg=cursor.rowcount
    
        # checking if the input fields are empty
        if btitle=="" or bauth=="" or shelfno=="" or bid=="":
            self.adbkemp.setHidden(False)
            self.adbsucesslb.setHidden(True)
            self.adbexist.setHidden(True)

        elif rg>=1:
            self.adbexist.setStyleSheet("color: rgb(232, 0, 0);")
            self.adbexist.setText("Book ID already exist")
            self.adbexist.setHidden(False)
            self.adbkemp.setHidden(True)
            self.adbsucesslb.setHidden(True)
                                  
        # Adding the book to database
        else:
            qry="insert into book(BookID,Name,Author,Dept,shelf,Avail,Visible)values('%s','%s','%s','%s','%s','%s','%s')"
            args=(bid,btitle,bauth,dpt,shelfno,av,v)
            cursor.execute(qry%args)
            con.commit()
            con.close()
            self.adbkemp.setHidden(True)
            self.adbexist.setHidden(True)
            self.adbsucesslb.setHidden(False)
            # Clearing the fields
            self.adbkid.clear()
            self.adbkname.clear()
            self.adbkauth.clear()
            self.adbkshelfno.clear()
            
    

        # Calling viewallbooks functions
        ViewBook.viewbookfun(self)
        
        
        

