import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
import mysql.connector

class SearchStud():

    def searchstdfun(self):
        
        v='yes'
        self.searchstdemp.setHidden(True)
        self.tableWidget.clear()
        # Setting table widget column count to 6
        self.tableWidget.setColumnCount(6)
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

        # Setting horizontal header labels
        self.tableWidget.setHorizontalHeaderLabels(["Rollno","First Name","Last Name","Course","Phone No","No of Books"])
        # Initializing table row to 0
        tablerow=0
        # ===================================================================================================
        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        # Get the input and store it in a variable
        searchtxt=self.searchstdtxt.text()
        # if the input is not empty
        if searchtxt!="":
            # if the combobox index=0 ie..RollNo
            if self.searchstdcombo.currentIndex()==0:
                self.searchstdtxt.clear()
                # Get details where RollNo=given input
                sqlrlno="Select * from student where rollno='%s' and Visible='%s'"
                argsid=(searchtxt,v)
                self.tableWidget.clear()
                # Setting horizontal header labels
                self.tableWidget.setHorizontalHeaderLabels(["Rollno","First Name","Last Name","Course","Phone No","No of Books"])
                cursor.execute(sqlrlno%argsid)
                # Fetch the details from the cursor
                rowsrlno=cursor.fetchall()
                # If the details are not empty
                if cursor.rowcount>=1:
                    for row in rowsrlno:
                        # Setting data to table widget column one by one
                        self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                        self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))

                        # Increasing row count to move to the next row
                        tablerow+=1
                    # Display proper message
                    self.searchstdemp.setStyleSheet("color: rgb(2, 170, 27);")
                    self.searchstdemp.setText("Search Successfull")
                    self.searchstdemp.setHidden(False)
                else:
                    # If the details are empty display proper message
                    self.searchstdemp.setText("Student does not exist") 
                    self.searchstdemp.setStyleSheet("color: rgb(232, 0, 0);") 
                    self.searchstdemp.setHidden(False)   

            # if the combobox index=1 ie..FirstName
            elif self.searchstdcombo.currentIndex()==1:
                self.searchstdtxt.clear()
                sqlstfname="Select * from student where FName='%s' and Visible='%s'"
                argfname=(searchtxt,v)
                self.tableWidget.clear()
                # Setting horizontal header labels
                self.tableWidget.setHorizontalHeaderLabels(["Rollno","First Name","Last Name","Course","Phone No","No of Books"])
                cursor.execute(sqlstfname%argfname)
                rowsstdname=cursor.fetchall()
                if cursor.rowcount>=1:
                    for row in rowsstdname:
                        # Setting data to table widget column one by one
                        self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                        self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))

                        # Increasing row count to move to the next row
                        tablerow+=1
                    self.searchstdemp.setStyleSheet("color: rgb(2, 170, 27);")
                    self.searchstdemp.setText("Search Successfull")
                    self.searchstdemp.setHidden(False)
                else:
                    self.searchstdemp.setStyleSheet("color: rgb(232, 0, 0);")
                    self.searchstdemp.setText("Student does not exist")
                    self.searchstdemp.setHidden(False)   

        # if the input field is empty display proper message
        else:
            self.searchstdemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.searchstdemp.setText("Input cannot be empty")     
            self.searchstdemp.setHidden(False)  

        # if the combobox index=2 ie..Course
        if self.searchstdcombo.currentIndex()==2:
            self.searchstdtxt.clear()
            # Get the input from the input combobox(Another combobox which will be visible when searchstdcombo box index=2)
            searchcombo=self.searchstdtxtcombo.currentText()
            sqlcrs="Select * from student where course='%s' and Visible='%s'"
            argcrs=(searchcombo,v)
            self.tableWidget.clear()
            # Setting horizontal header labels
            self.tableWidget.setHorizontalHeaderLabels(["Rollno","First Name","Last Name","Course","Phone No","No of Books"])
            cursor.execute(sqlcrs%argcrs)
            rowsstd=cursor.fetchall()
            if cursor.rowcount>=1:
                for row in rowsstd:
                    # Setting data to table widget column one by one
                    self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                    self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                    self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                    self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                    self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))

                    # Increasing row count to move to the next row
                    tablerow+=1
                self.searchstdemp.setStyleSheet("color: rgb(2, 170, 27);")
                self.searchstdemp.setText("Search Successfull")
                self.searchstdemp.setHidden(False)
            else:
                self.searchstdemp.setStyleSheet("color: rgb(232, 0, 0);")
                self.searchstdemp.setText("Student does not exist")
                self.searchstdemp.setHidden(False)        
 
        