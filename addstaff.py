import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
from viewstf import Viewstaff
import mysql.connector

class Addstaff():
    # Add Staff function
    def addstaffun(self):
        
        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        # Getting data from line editors then setting them to variables
        stafid=self.adstafid.text()
        staffname=self.adstafirst.text()
        staflname=self.adstaflast.text()
        # Getting selected text from combobox
        dpt=self.adstafcombo.currentText()
        phno=self.adstafphno.text()
        # setting yes to Visible
        v='yes'

        sql="select * from staff where StaffID='%s' and Visible='%s'"
        arg=(stafid,v)
        cursor.execute(sql%arg)
        rg=cursor.rowcount

        # checking if the input fields are empty
        if staffname=="" or staflname==""  or phno=="" or stafid=="":
            self.adstafemp.setHidden(False)
            self.adstafsucesslb.setHidden(True)
            self.adstafexist.setHidden(True)

        elif rg>=1:
            self.adstafemp.setHidden(True)
            self.adstafsucesslb.setHidden(True)
            self.adstafexist.setText("Staff ID already exist")
            self.adstafexist.adjustSize()
            self.adstafexist.setHidden(False)

        elif len(phno)<10:
            self.adstafsucesslb.setHidden(True)
            self.adstafemp.setHidden(True)
            self.adstafexist.setHidden(False)
            self.adstafexist.setText("Invalid phone number")
            self.adstafexist.adjustSize()
            self.adstafphno.clear()
            self.adstafphno.setFocus()
            
  
        # Adding the staff to database
        else:
            phno=self.adstafphno.text()
            qry="insert into staff(StaffID,Fname,Lname,PhoneNo,Dept,Visible)values('%s','%s','%s','%s','%s','%s')"
            args=(stafid,staffname,staflname,phno,dpt,v)
            cursor.execute(qry%args)
            con.commit()
            con.close()
            self.adstafemp.setHidden(True)
            self.adstafexist.setHidden(True)
            self.adstafsucesslb.setHidden(False)
            # Clearing the fields
            self.adstafid.clear()
            self.adstafirst.clear()
            self.adstaflast.clear()
            self.adstafphno.clear()
            self.adstafirst.setFocus()

        Viewstaff.viewstafffun(self)
        
        
    

