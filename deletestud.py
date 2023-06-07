import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
from viewstd import Viewstud
import mysql.connector

class Deletestd():
   #Delete student function
    def Deletestudent(self):
      # Getting studentid from lineditor and setting it to studentid variable
         studid=self.stddelidtxt.text()
         v='yes'
         con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
         cursor=con.cursor()
         chkstd="select * from student where rollno='%s' and Visible='%s'"
         args=(studid,v)
         cursor.execute(chkstd%args)

         # Checking if the studentid is empty
         if studid=="":
            self.delstdemp.setHidden(False)
            self.delstdsucesslb.setHidden(True)
            self.invalidstd.setHidden(True)


         # If the student exist then deleting it
         elif cursor.rowcount>=1:
            qry="UPDATE student SET Visible = 'no' WHERE rollno = '%s';"
            arg=(studid)
            cursor.execute(qry%arg)
            con.commit()
            con.close()
            self.delstdemp.setHidden(True)
            self.invalidstd.setHidden(True)
            self.delstdsucesslb.setHidden(False)
            self.tableWidget.clear()

            
         # If the student doesnt exist then displaying invalid student message and hiding uneseccary messages
         else:
            self.delstdsucesslb.setHidden(True)
            self.invalidstd.setHidden(False)
            self.delstdemp.setHidden(True)

         Viewstud.viewstudfun(self)
         self.stddelidtxt.clear()
