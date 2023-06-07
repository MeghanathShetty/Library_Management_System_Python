import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from returnstud import  Returnstud
from datetime import date
from dateutil import parser
from srchisstf import Searchisstf
import mysql.connector

class RenewStaff():

    def renewstaffun(self):

        v='no'    
        # Get input
        rnid=self.rtnstafftxt.text()
        rtndate=self.renewstfdate.text()
        # Create connection
        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        # Get current date
        currentdate=str(date.today())
        # Get old Return date from issued staff table========
        chk="select ReturnDate from issuestaff where IssuedBID='%s' and returned='%s'"
        arg=(rnid,v)
        cursor.execute(chk%arg)
        oldate=str(cursor.fetchone()[0])
        #====================================================
        # Convert old date str format to date format
        oldatee=parser.parse(oldate)
        # Remove time and make it only date
        oldt=oldatee.strftime('%Y-%m-%d')
        # Do the same to new date============================
        newdate=parser.parse(rtndate)
        newdt=newdate.strftime('%Y-%m-%d')

        # ===================================================      

        # If the new date and old date and current date are not same
        if newdt!=oldt and newdt!=currentdate:
            # Add the new date to issue staff table
            sqll="UPDATE issuestaff SET IssuedDate='%s',ReturnDate='%s' where IssuedBID = '%s' and returned='%s'"
            argg=(currentdate,rtndate,rnid,v)
            cursor.execute(sqll%argg)
            con.commit()
            # Display message
            self.returnstudemp_3.setHidden(False)
            self.returnstudemp_3.setStyleSheet("color: rgb(2, 170, 27);")
            self.returnstudemp_3.setText("Book sucessfully renewd")
            # Automatically adjusts the size of the label
            self.returnstudemp_3.adjustSize()
            Searchisstf.searchisstffun(self)       
        else:
            # Display message
            self.returnstudemp_3.setHidden(False)
            self.returnstudemp_3.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstudemp_3.setText("Enter valid new date")
            # Automatically adjusts the size of the label
            self.returnstudemp_3.adjustSize()
            

     




        