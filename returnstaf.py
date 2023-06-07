import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
from datetime import date
from dateutil import parser
import mysql.connector

class Returnstaff():

    def rtnstafffun(self):

        self.returnstaffemp.setHidden(False)
        v='no'
        vi='yes'
        # Getting input
        isstfid=self.rtnstafftxt.text()
        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()

        # retrieve issue date 
        sql="select IssuedDate from issuestaff where IssuedBID='%s' and returned='%s'"
        arg=(isstfid,v)
        cursor.execute(sql%arg)
        oisiddd=cursor.fetchone()[0]


        # Convert it to date type
        oisidd=parser.parse(oisiddd)
        # This converts it to back  to date
        oisidd=oisidd.date()

        # ===========================================================================================================
        # get the current date
        currentdate=str(date.today())
        cdate=parser.parse(currentdate)
        cdtt=cdate.date()

        # Check if the id exists
        sqlchk="select * from issuestaff where IssuedBID='%s' and returned='%s'"
        argchk=(isstfid,v)
        cursor.execute(sqlchk%argchk)
        ck=cursor.rowcount

        sql="select Issuedstaff from issuestaff where IssuedBID='%s' and returned='%s'"
        arg=(isstfid,v)
        cursor.execute(sql%arg)
        stfid=str(cursor.fetchone()[0])

        sql="select totalbk from staff where StaffID='%s' and Visible='%s'"
        arg=(stfid,vi)
        cursor.execute(sql%arg)
        # print(cursor.fetchone()[0])
        x=cursor.fetchone()[0]
        tbv=int(x)
        tbb=tbv+1
        tb=str(tbb)

        # # if issuedate and currentdate are same
        # if oisidd==cdtt:
        #     self.returnstaffemp.setStyleSheet("color: rgb(232, 0, 0);")
        #     self.returnstaffemp.setText("Cannot return book today itself")
        #     self.returnstaffemp.adjustSize()

        # if it exists
        if ck>=1:
            

            sql="UPDATE issuestaff SET returneddt='%s' WHERE IssuedBID='%s' and returned='%s';"
            arg=(currentdate,isstfid,v)
            cursor.execute(sql%arg)

            sql="UPDATE staff SET totalbk = '%s' WHERE StaffID = '%s' and Visible='%s';"
            arg=(tb,stfid,vi)
            cursor.execute(sql%arg)

            conn=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
            cursorr=conn.cursor()
            # Retrieve bookid 
            sq="select IssuedBID from issuestaff where IssuedBID='%s' and returned='%s'"
            ar=(isstfid,v)
            cursorr.execute(sq%ar)
            # [0] is added in the end because to only return the value
            bkid=cursorr.fetchone()[0]
            conn.commit()
            cursorr.close()
            conn.close()

            # Delete row from issuestud table
            sql="UPDATE issuestaff SET returned = 'yes' WHERE IssuedBID = '%s' and returned='%s';"
            arg=(isstfid,v)
            cursor.execute(sql%arg)
       
            # Set the book to available in book table
            sqll="UPDATE book SET Avail = 'Available' where BookID = '%s' and Visible='%s'"
            argg=(bkid,vi)
            cursor.execute(sqll%argg)
            con.commit()
            self.returnstaffemp.setStyleSheet("color: rgb(2, 170, 27);")
            self.returnstaffemp.setText("Succesfull")
            con.close()
            # self.rtnstafftxt.clear()
        else:
            # Clear the input field
            self.rtnstafftxt.clear()
            # Display proper message
            self.returnstaffemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstaffemp.setText("No such record found")