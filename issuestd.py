import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
from datetime import date
from viewisstd import ViewIsstd
from datetime import date,timedelta
from dateutil import parser
import mysql.connector

class Issuestud():
    
    def issuestdfun(self):

        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        # Get count of IssueID from Issued Student
        qry="select IssueID from issuestud"
        cursor.execute(qry)
        isid=cursor.rowcount
        # Getting all the inputs and storing it in variables
        # isid=self.isstdid.text()
        isstdid=self.isstdstudid.text()
        isbkid=self.isstdbkid.text()

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
        # r is renewals
        r=2
        # ==============================

        v='yes'
        
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

        sql="select totalbk from student where rollno='%s' and Visible='%s'"
        arg=(isstdid,v)
        cursor.execute(sql%arg)
        x=cursor.fetchone()[0]
        tb=int(x)

        # Validations===========================================
        if isdt==rtndt:
            self.isstdemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstdemp.setText("Issue date and return date cannot be same")
            self.isstdemp.adjustSize()
            self.isstdemp.setHidden(False)

        elif rtndt<isdt:
            self.isstdemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstdemp.setText("Issue date must be greater than return date")
            self.isstdemp.adjustSize()
            self.isstdemp.setHidden(False)

        elif chkavv==ch:
            self.isstdemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstdemp.setText("Book is already issued to someone")
            self.isstdemp.adjustSize()
            self.isstdemp.setHidden(False)
            self.isstdbkid.clear()
        
        
        elif tb>0:
            fine=0
            isid=isid+1
            tb=tb-1
            tbb=str(tb)
            # insert the issue details to issuestud table 
            sql="insert into issuestud(IssueID,Issuedstud,IssuedBID,IssuedDate,ReturnDate,Fine,Renewals)values('%s','%s','%s','%s','%s','%s','%s')"
            args=(isid,isstdid,isbkid,currentdate,rtndts,fine,r)
            cursor.execute(sql%args)

            sql="UPDATE student SET totalbk = '%s' WHERE rollno = '%s' and Visible='%s';"
            arg=(tbb,isstdid,v)
            cursor.execute(sql%arg)

            # Set issued book to unavailable in Book table
            sqlupd="UPDATE book SET Avail = 'Unavailable' WHERE BookID = '%s' and Visible='%s';"
            argsup=(isbkid,v)
            cursor.execute(sqlupd%argsup)
            self.isstdemp.setStyleSheet("color: rgb(2, 170, 27);")
            self.isstdemp.setText("Successfully issued")
            self.isstdemp.adjustSize()
            self.isstdemp.setHidden(False)
            con.commit()
            con.close()
            # Calling view issue student 
            ViewIsstd.viewisstdfun(self)
            # Clearing all the fields
            # self.isstdid.clear()
            self.isstdstudid.clear()
            self.isstdbkid.clear()
        else:
            self.isstdemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.isstdemp.setText("Student has already taken maximum books")
            self.isstdemp.adjustSize()
            self.isstdemp.setHidden(False)

        


    

        


        