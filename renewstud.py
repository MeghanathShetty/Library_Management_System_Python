import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from returnstud import  Returnstud
from datetime import date
from dateutil import parser
from srchisstd import Searchisstd
import mysql.connector

class RenewStud():
    def renewstudfun(self):

        v='no'

        self.returnstudemp_2.setHidden(False)

        # Get input
        rnid=self.rtnstudtxt.text()
        rtndate=self.renewstddate.text()
        # Create connection
        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()

        # Get current date
        currentdate=str(date.today())
        # Convert it to date format
        cdate=parser.parse(currentdate)

        # ===========================================================
        # Get Old Fine from issuestud table==================
        sql="select Fine from issuestud where IssuedBID='%s' and returned='%s'"
        arg=(rnid,v)
        cursor.execute(sql%arg)
        oldfine=int(cursor.fetchone()[0])
        # ===================================================
        # Get ReturnDate from issuestud table================
        chk="select ReturnDate from issuestud where IssuedBID='%s' and returned='%s'"
        arg=(rnid,v)
        cursor.execute(chk%arg)
        oldate=str(cursor.fetchone()[0])
        # Convert old date to date format
        oldatee=parser.parse(oldate)
        # Remove the time from old date but this converts it to str format(this line is not used because date() is better)
        oldt=oldatee.strftime('%Y-%m-%d')
        # =============================================================
        # Convert newdate to date format
        newdate=parser.parse(rtndate)
        # Remove the time from new date but this converts it to str format(this line is not used because date() is better)
        newdt=newdate.strftime('%Y-%m-%d')

# Calculating fine=============================================================================================
        # Current date
        cdtt=cdate.date()
        # Old return date
        oldtt=oldatee.date()
        # Calculate the new fine to be added by getting the difference between current date and old return date
        fn=cdtt-oldtt
        # this converts date to int type
        fnn=fn.days
        # Adding old fine plus newly calculated fine============================================
        finee=oldfine+fnn
# ==============================================================================================================


        # If new date and old date and current date are not the same
        if newdt!=oldt and newdt!=currentdate:
            # Get the number of renewals available from the issuestud table
            sq="select Renewals from issuestud where IssuedBID='%s' and returned='%s'"
            ar=(rnid,v)
            cursor.execute(sq%ar)
            # Store it in rn variable
            rn=int(cursor.fetchone()[0])

            # if the no of renewals available =2
            if rn==2:
                # Create a new variable rnno and set it to 1
                rnno=1
                # Set return date=new return date,renewals=1 and fine=finee(finee variable)
                sqll="UPDATE issuestud SET IssuedDate='%s',ReturnDate='%s',Renewals='%s',Fine='%s' where IssuedBID = '%s' and returned='%s'"
                argg=(currentdate,rtndate,rnno,finee,rnid,v)
                cursor.execute(sqll%argg)
                con.commit()
                # Display proper message
                self.returnstudemp_2.setText("Book sucessfully renewd")
                # Automatically adjusts the size of the lable
                self.returnstudemp_2.adjustSize()
                # Set font color to green 
                self.returnstudemp_2.setStyleSheet("color: rgb(2, 170, 27);")
                Searchisstd.searchisstdfun(self)


            # if the no of renewals avaialable=1
            elif rn==1:
                # Create a new variable rnno and set it to 1
                rnno=0
                # Set return date=new return date,renewals=0 and fine=finee(finee variable)
                sqll="UPDATE issuestud SET IssuedDate='%s',ReturnDate='%s',Renewals='%s',Fine='%s' where IssuedBID = '%s' and returned='%s'"
                argg=(currentdate,rtndate,rnno,finee,rnid,v)
                cursor.execute(sqll%argg)
                con.commit()
                # Display proper message
                self.returnstudemp_2.setText("Book sucessfully renewd")
                # Automatically adjusts the size of the lable
                self.returnstudemp_2.adjustSize()
                # Set font color to green 
                self.returnstudemp_2.setStyleSheet("color: rgb(2, 170, 27);")
                Searchisstd.searchisstdfun(self)

            # if the no of renewals avaialable=0
            elif rn==0:
                # Display proper message that the book cannot be renewed more than twice
                self.returnstudemp_2.setText("Book cannot be renewed more than twice")
                self.returnstudemp_2.setStyleSheet("color: rgb(232, 0, 0);")
                self.returnstudemp_2.adjustSize()            
        else:
            # If new date and old date and current date are the same,display message
            self.returnstudemp_2.setText("Enter valid new date")
            self.returnstudemp_2.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstudemp_2.adjustSize()
            

     




        