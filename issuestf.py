import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
from viewisstf import ViewIsstf
from datetime import date,timedelta
from dateutil import parser
import mysql.connector

class Issuestaff():
    
    def issuestffun(self):

        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        # Get count of IssueID from Issued Staff
        qry="select IssueID from issuestaff"
        cursor.execute(qry)
        isid=cursor.rowcount
        # Getting all the inputs and storing it in variables

        isstfid=self.isstfstafid.text()
        isbkid=self.isstfbkid.text()

        # Get current date
        currentdate=str(date.today())
        # Convert it to date format
        cdate=parser.parse(currentdate)
        # Current date
        isdt=cdate.date()
           
# ==================================

        rtndt = isdt
        rtndt += timedelta(days=7)
        rtndts=str(rtndt)
# ==============================

        v='yes'

        sql="select totalbk from staff where StaffID='%s' and Visible='%s'"
        arg=(isstfid,v)
        cursor.execute(sql%arg)
        x=cursor.fetchone()[0]
        tb=int(x)


        # Get avaialable column from Book where BookID=given input
        sqlbkav="select Avail from book where BookID='%s' and Visible='%s'"
        argbkav=(isbkid,v)
        cursor.execute(sqlbkav%argbkav)
        # get the detail
        chkav=cursor.fetchone()
        # fetchone gets in a tuple data type so convert it to str(this line may not be necessary)
        chkavv=str(chkav)
        # assign unavailable to ch for later use
        ch="('Unavailable',)"


        # Validations===========================================

        if isdt==rtndt:
            self.isstfemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstfemp.setText("Issue date and return date cannot be same")
            self.isstfemp.adjustSize()
            self.isstfemp.setHidden(False)

        elif rtndt<isdt:
            self.isstfemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstfemp.setText("Issue date must be greater than return date")
            self.isstfemp.adjustSize()
            self.isstfemp.setHidden(False)


        elif chkavv==ch:
            self.isstfemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstfemp.setText("Book is already issued to someone")
            self.isstfemp.adjustSize()
            self.isstfemp.setHidden(False)
            self.isstfbkid.clear()
        
        
        elif tb>0:


            isid=isid+1
            tb=tb-1
            tbb=str(tb)

            # insert the issue details to issuestaff table 
            sql="insert into issuestaff(IssueID,Issuedstaff,IssuedBID,IssuedDate,ReturnDate)values('%s','%s','%s','%s','%s')"
            args=(isid,isstfid,isbkid,currentdate,rtndts)
            cursor.execute(sql%args)

            sql="UPDATE staff SET totalbk = '%s' WHERE StaffID = '%s' and Visible='%s';"
            arg=(tbb,isstfid,v)
            cursor.execute(sql%arg)

            # Set issued book to unavailable in Book table
            sqlupd="UPDATE book SET Avail = 'Unavailable' WHERE BookID = '%s' and Visible='%s';"
            argsup=(isbkid,v)
            cursor.execute(sqlupd%argsup)
            self.isstfemp.setStyleSheet("color: rgb(2, 170, 27);")
            self.isstfemp.setText("Successfully issued")
            self.isstfemp.adjustSize()
            self.isstfemp.setHidden(False)
            con.commit()
            con.close()
            # Calling view issued staff
            ViewIsstf.viewisstffun(self)
            # Clearing the fields 
            # self.isstfid.clear()
            self.isstfstafid.clear()
            self.isstfbkid.clear()

        else:
            self.isstfemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstfemp.setText("Staff has already taken maximum books")
            self.isstfemp.adjustSize()
            self.isstfemp.setHidden(False)


    



        