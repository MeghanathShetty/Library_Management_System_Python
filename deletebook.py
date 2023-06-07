import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
import mysql.connector

class Deletebk():
   #Delete book function
    def Deletebook(self):
      # Getting bookid from lineditor and setting it to bookid variable
         bookid=self.bkidtxt.text()
         con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
         cursor=con.cursor()
         v='yes'
         chk="select * from book where BookID='%s' and Visible='%s'"
         args=(bookid,v)
         cursor.execute(chk%args)
         c=cursor.rowcount

         # Get avaialable column from Book where BookID=given input
         sqlbkav="select Avail from book where BookID='%s'"
         argbkav=(bookid)
         cursor.execute(sqlbkav%argbkav)
         # get the detail
         chkav=cursor.fetchone()
         # fetchone gets in a tuple data type so convert it to str(this line may not be necessary)
         chkavv=str(chkav)
         # assign unavailable to ch for later use
         ch="('Unavailable',)"


         # Checking if the bookid is empty
         if bookid=="":
            # Displaying book is is empty message and hiding uneseccary messages
            self.delbemp.setText("Input cannot be empty")
            self.delbemp.setHidden(False)
            self.delbsucesslb.setHidden(True)
            self.invalidbk.setHidden(True)

         # Checks if book is issued 
         elif chkavv==ch:
            self.delbemp.setHidden(False)
            self.delbemp.setText("Book is issued to someone")


         # If the book exist then deleting it
         elif c>=1:
            qry="UPDATE book SET Visible = 'no' WHERE BookID = '%s';"
            arg=(bookid)
            cursor.execute(qry%arg)
            con.commit()
            con.close()
            self.delbemp.setHidden(True)
            self.invalidbk.setHidden(True)
            self.delbsucesslb.setHidden(False)
            self.tableWidget.clear()
            ViewBook.viewbookfun(self)

            
         # If the book doesnt exist then displaying invalid book message and hiding uneseccary messages
         else:
            self.delbsucesslb.setHidden(True)
            self.invalidbk.setHidden(False)
            self.delbemp.setHidden(True)

         ViewBook.viewbookfun(self)
         self.bkidtxt.clear()
