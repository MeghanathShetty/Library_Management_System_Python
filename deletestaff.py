import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
from viewstf import Viewstaff
import mysql.connector

class Deletestf():
   #Delete staff function
    def Deletestaff(self):
      # Getting staffid from lineditor and setting it to staffid variable
         staffid=self.stfdelidtxt.text()
         con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
         cursor=con.cursor()
         v='yes'
         chkstf="select * from staff where StaffID='%s' and Visible='%s'"
         args=(staffid,v)
         cursor.execute(chkstf%args)

         # Checking if the staffid is empty
         if staffid=="":
            self.delstfemp.setHidden(False)
            self.delstfsucesslb.setHidden(True)
            self.invalidstf.setHidden(True)


         # If the staff exist then deleting it
         elif cursor.rowcount>=1:
            qry="UPDATE staff SET Visible = 'no' WHERE StaffID = '%s';"
            arg=(staffid)
            cursor.execute(qry%arg)
            con.commit()
            con.close()
            self.delstfemp.setHidden(True)
            self.invalidstf.setHidden(True)
            self.delstfsucesslb.setHidden(False)
            self.tableWidget.clear()

            
         # If the staff doesnt exist then displaying invalid staff message and hiding uneseccary messages
         else:
            self.delstfsucesslb.setHidden(True)
            self.invalidstf.setHidden(False)
            self.delstfemp.setHidden(True)


         Viewstaff.viewstafffun(self)
         
         self.stfdelidtxt.clear()
