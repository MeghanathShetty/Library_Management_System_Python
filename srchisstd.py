import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from datetime import date
from dateutil import parser
import mysql.connector

class Searchisstd():
# Search Student Issued Details Function
    def searchisstdfun(self):
        
    
        # Get input
        isstdid=self.rtnstudtxt.text()
        self.tableWidget.clear()
        # Setting table widget column count to 9
        self.tableWidget.setColumnCount(9)
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
        header.setSectionResizeMode(7,QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(8,QtWidgets.QHeaderView.Stretch)

        # # Setting horizontal header labels
        # self.tableWidget.setHorizontalHeaderLabels(["IssueID","StudentID","BookID","IssuedDate","ReturnDate","Renewals"])
        # Initializing table row to 0
        tablerow=0
        # Creating connection
        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        sqlbkid="Select * from issuestud where Issuedstud='%s'"
        argsid=(isstdid)
        cursor.execute(sqlbkid%argsid)
        # If cursor is not empty
        if cursor.rowcount>=1:
            
            # Get the details from issuestud table
            sqlbkid="Select IssueID,Issuedstud,IssuedBID,IssuedDate,ReturnDate,Fine,Renewals,returneddt,returned from issuestud where Issuedstud='%s'"
            argsid=(isstdid)
            # Setting horizontal header labels
            self.tableWidget.setHorizontalHeaderLabels(["IssueID","StudentID","BookID","IssuedDate","ExpectedReturnDate","Fine","Renewals","ReturnDate","Returned",])
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
                self.tableWidget.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[7]))
                self.tableWidget.setItem(tablerow,8,QtWidgets.QTableWidgetItem(row[8]))


                # Increasing row count to move to the next row
                tablerow+=1
            # self.rtnstudtxt.clear()
            self.returnstudemp.setHidden(False)
            self.returnstudemp.setStyleSheet("color: rgb(2, 170, 27);")
            self.returnstudemp.setText("Search Succesfull")
                 
