import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
from viewstd import Viewstud
import mysql.connector

class Addstudent():
    # Add Student function
    def addstudfun(self):

        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        # Getting data from line editors then setting them to variables
        studid=self.adstudroll.text()
        studfname=self.adstudfirst.text()
        studlname=self.adstudlast.text()
        # Getting selected text from combobox
        course=self.adstudcombo.currentText()
        phnostud=self.adstudphno.text()
        # setting yes to visible
        v='yes'

        sql="select * from student where rollno='%s' and Visible='%s'"
        arg=(studid,v)
        cursor.execute(sql%arg)
        rg=cursor.rowcount
        
        # checking if the input fields are empty
        if studfname=="" or studlname==""  or phnostud=="" or studid=="":
            self.adstudemp.setHidden(False)
            self.adstudsucess.setHidden(True)
            self.adstudexist.setHidden(True)

        elif rg>=1:
            self.adstudemp.setHidden(True)
            self.adstudsucess.setHidden(True)
            self.adstudexist.setText("Roll No already exist")
            self.adstudexist.adjustSize()
            self.adstudexist.setHidden(False)


        elif len(phnostud)<10:
            self.adstudsucess.setHidden(True)
            self.adstudemp.setHidden(True)
            self.adstudexist.setHidden(False)
            self.adstudexist.setText("Invalid phone number")
            self.adstudexist.adjustSize()
            self.adstudphno.clear()
            self.adstudphno.setFocus()

            
            
        # Adding the student to database
        else:
            phnostud=self.adstudphno.text()
            qry="insert into student(rollno,Fname,Lname,Phoneno,course,Visible)values('%s','%s','%s','%s','%s','%s')"
            args=(studid,studfname,studlname,phnostud,course,v)
            cursor.execute(qry%args)
            con.commit()
            con.close()
            self.adstudemp.setHidden(True)
            self.adstudexist.setHidden(True)
            self.adstudsucess.setHidden(False)
            # Clearing the fields
            self.adstudroll.clear()
            self.adstudfirst.clear()
            self.adstudlast.clear()
            self.adstudphno.clear()
            self.adstudfirst.setFocus()

        Viewstud.viewstudfun(self)
        

        
        