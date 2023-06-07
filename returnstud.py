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

class Returnstud():

    def rtnstudfun(self):

        self.returnstudemp.setHidden(False)
        
        # Getting input
        isstdid=self.rtnstudtxt.text()

        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()

        # ============================================================================================================

        self.tableWidget.clear()
        # Setting table widget column count to 7
        self.tableWidget.setColumnCount(7)
        # Setting table widget row count to 100
        self.tableWidget.setRowCount(100)
        # Setting horizontal header of tablewidget to header variable
        header=self.tableWidget.horizontalHeader()
        #Resizing header section based on number of columns
        header.setSectionResizeMode(0,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(3,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(5,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(6,QtWidgets.QHeaderView.Stretch)
        # Setting horizontal header labels
        self.tableWidget.setHorizontalHeaderLabels(["IssueID","StudentID","BookID","IssuedDate","ReturnDate","Fine","Renewals"])
        # Initializing table row to 0
        tablerow=0

        # ==============================================================================================================

        v='no'
        vi='yes'

        # retrieve issue date 
        sql="select IssuedDate from issuestud where IssuedBID='%s' and returned='%s'"
        arg=(isstdid,v)
        cursor.execute(sql%arg)
        oisiddd=cursor.fetchone()[0]


        # Convert it to date type
        oisidd=parser.parse(oisiddd)
        # This converts it to back  to date
        oisidd=oisidd.date()

        # ==============================================s=========================================================
        # get the current date
        currentdate=str(date.today())
        cdate=parser.parse(currentdate)
        cdtt=cdate.date()

        # Check if the id exists
        sql="select * from issuestud where IssuedBID='%s' and returned='%s'"
        arg=(isstdid,v)
        cursor.execute(sql%arg)
        ck=cursor.rowcount

        
        sql="select Issuedstud from issuestud where IssuedBID='%s' and returned='%s'"
        arg=(isstdid,v)
        cursor.execute(sql%arg)
        stdid=str(cursor.fetchone()[0])

        sql="select totalbk from student where rollno='%s' and Visible='%s'"
        arg=(stdid,vi)
        cursor.execute(sql%arg)
        # print(cursor.fetchone()[0])
        x=cursor.fetchone()[0]
        tbv=int(x)
        tbb=tbv+1
        tb=str(tbb)

        # # if issuedate and currentdate are same
        # if oisidd==cdtt:
        #     self.returnstudemp.setStyleSheet("color: rgb(232, 0, 0);")
        #     self.returnstudemp.setText("Cannot return book today itself")
        #     self.returnstudemp.adjustSize()
 
        # if it exists
        if ck>=1:

            # Fine things###################################################################################################

            # Get ReturnDate from issuestud table 
            chk="select ReturnDate from issuestud where IssuedBID='%s' and returned='%s'"
            arg=(isstdid,v)
            cursor.execute(chk%arg)
            oldate=str(cursor.fetchone()[0])
            # Convert it to date type
            oldatee=parser.parse(oldate)
            # This converts it to back  to date
            oldtt=oldatee.date()
            # print(oldtt)
            # =======================================================================================================
            # Get Old Fine from issuestud table
            sql="select Fine from issuestud where IssuedBID='%s' and returned='%s'"
            arg=(isstdid,v)
            cursor.execute(sql%arg)
            oldfine=int(cursor.fetchone()[0])
            # print(oldfine)
            # =======================================================================================================
            # Calculate the new fine to be added by getting the difference between current date and return date
            fn=cdtt-oldtt
            # print(fn)
            # this converts date to int type
            fnn=fn.days
            # =======================================================================================================
            # Adding old fine plus newly calculated fine
            finee=oldfine+fnn
            # print(finee)


            # if the value is negative,make it 0
            if finee<0:
                finee=0

            #################################################################################################################

            # Retrieve bookid ========================================================
            sq="select IssuedBID from issuestud where IssuedBID='%s' and returned='%s'"
            ar=(isstdid,v)
            cursor.execute(sq%ar)
            bkid=cursor.fetchone()[0]

            sql="UPDATE student SET totalbk = '%s' WHERE rollno = '%s' and Visible='%s';"
            arg=(tb,stdid,vi)
            cursor.execute(sql%arg)

            
            # Update the fine========================================================
            sqll="UPDATE issuestud SET Fine='%s' where IssuedBID = '%s' and returned='%s'"
            argg=(finee,bkid,v)
            cursor.execute(sqll%argg)

            # Get the details from issuestud table
            sqlbkid="Select * from issuestud where IssuedBID='%s' and returned='%s'"
            argsid=(isstdid,v)
            cursor.execute(sqlbkid%argsid)
            rowsbkid=cursor.fetchall()
            for row in rowsbkid:
                # Setting data to table widget column one by one
                self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
                self.tableWidget.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
                # Increasing row count to move to the next row
                tablerow+=1

        
            sql="UPDATE issuestud SET returneddt='%s' WHERE IssuedBID='%s' and returned='%s';"
            arg=(currentdate,isstdid,v)
            cursor.execute(sql%arg)

            
       
            sql="UPDATE issuestud SET returned = 'yes' WHERE IssuedBID = '%s' and returned='%s';"
            arg=(isstdid,v)
            cursor.execute(sql%arg)
            con.commit()

            # Set the book to available in book table
            sqll="UPDATE book SET Avail = 'Available' where BookID = '%s' and Visible='%s'"
            argg=(bkid,vi)
            cursor.execute(sqll%argg)
            con.commit()
            self.returnstudemp.setStyleSheet("color: rgb(2, 170, 27);")
            self.returnstudemp.setText("Succesfull")
            cursor.close()
            con.close()
            # self.rtnstudtxt.clear()
        # if it does not exist
        else:
            # Clear the input field
            self.rtnstudtxt.clear()
            # Display no such records found
            self.returnstudemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.returnstudemp.setText("No such record found")