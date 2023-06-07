import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
import mysql.connector

class SearchStaff():

    def searchstffun(self):
        
        v='yes'
        self.searchstfemp.setHidden(True)
        # Clear the previous data in the table
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
        self.tableWidget.setHorizontalHeaderLabels(["Staff ID","First Name","Last Name","Phone No","Department","No of Books"])
        # Initializing table row to 0
        tablerow=0
        # ==========================================================================================================
        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        # Get the input
        searchtxt=self.searchstftxt.text()
        # If the input is not empty
        if searchtxt!="":
            # if the combobox index is 0 ie..StaffID
            if self.searchstfcombo.currentIndex()==0:
                self.searchstftxt.clear()
                # Get the staff detail where StaffID=given input
                sqlstfid="Select * from staff where StaffID='%s' and Visible='%s'"
                argsid=(searchtxt,v)
                self.tableWidget.clear()
                # Setting horizontal header labels
                self.tableWidget.setHorizontalHeaderLabels(["Staff ID","First Name","Last Name","Phone No","Department","No of Books"])
                cursor.execute(sqlstfid%argsid)
                # Fetch the data from the cursor
                rowsstfid=cursor.fetchall()
                # If the cursor is not empty
                if cursor.rowcount>=1:
                    for row in rowsstfid:
                        # Setting data to table widget column one by one
                        self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                        self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))

                        # Increasing row count to move to the next row
                        tablerow+=1
                    # Unhide the label
                    self.searchstfemp.setHidden(False)
                    # Display proper message
                    self.searchstfemp.setStyleSheet("color: rgb(2, 170, 27);")
                    self.searchstfemp.setText("Search Successfull")
                else:
                    self.searchstfemp.setStyleSheet("color: rgb(232, 0, 0);")
                    self.searchstfemp.setHidden(False)
                    # If the cursor is empty display staff not exist
                    self.searchstfemp.setText("Staff does not exist")   

            # if the combobox index is 1 ie..First Name
            elif self.searchstfcombo.currentIndex()==1:
                self.searchstftxt.clear()
                # Get the staff detail where First Name=given input
                sqlstfname="Select * from staff where FName='%s' and Visible='%s'"
                argfname=(searchtxt,v)
                self.tableWidget.clear()
                # Setting horizontal header labels
                self.tableWidget.setHorizontalHeaderLabels(["Staff ID","First Name","Last Name","Phone No","Department","No of Books"])
                cursor.execute(sqlstfname%argfname)
                rowsstfname=cursor.fetchall()
                if cursor.rowcount>=1:
                    for row in rowsstfname:
                        # Setting data to table widget column one by one
                        self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                        self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))

                        # Increasing row count to move to the next row
                        tablerow+=1
                    self.searchstfemp.setHidden(False)
                    self.searchstfemp.setStyleSheet("color: rgb(2, 170, 27);")
                    self.searchstfemp.setText("Search Successfull")
                else:
                    self.searchstfemp.setHidden(False)
                    self.searchstfemp.setStyleSheet("color: rgb(232, 0, 0);")
                    self.searchstfemp.setText("Staff does not exist")           
        else:
            # Display proper message if the input is empty
            self.searchstfemp.setText("Input cannot be empty")  
            self.searchstfemp.setStyleSheet("color: rgb(232, 0, 0);")   
            self.searchstfemp.setHidden(False)

        # if the combobox index is 2 ie..Department
        if self.searchstfcombo.currentIndex()==2:
            self.searchstftxt.clear()
            # Get the input from the input combobox(Another combobox which will be visible when searchstfcombo box index=2)
            searchcombo=self.searchstftxtcombo.currentText()
            # Get Staff detail where Department=given input
            sqlbdpt="Select * from staff where Dept='%s' and Visible='%s'"
            argdpt=(searchcombo,v)
            self.tableWidget.clear()
            # Setting horizontal header labels
            self.tableWidget.setHorizontalHeaderLabels(["Staff ID","First Name","Last Name","Phone No","Department","No of Books"])
            cursor.execute(sqlbdpt%argdpt)
            rowsstddpt=cursor.fetchall()
            if cursor.rowcount>=1:
                for row in rowsstddpt:
                    # Setting data to table widget column one by one
                    self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                    self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                    self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                    self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                    self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))

                    # Increasing row count to move to the next row
                    tablerow+=1
                self.searchstfemp.setHidden(False)
                self.searchstfemp.setStyleSheet("color: rgb(2, 170, 27);")
                self.searchstfemp.setText("Search Successfull")
            else:
                self.searchstfemp.setHidden(False)
                self.searchstfemp.setStyleSheet("color: rgb(232, 0, 0);")
                self.searchstfemp.setText("Staff does not exist")    
            


 
        