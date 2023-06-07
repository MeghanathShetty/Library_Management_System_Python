import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
import mysql.connector

class ViewIsstd():
# View All Student Issued Details Function
    def viewisstdfun(self):
        v='no'
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
        self.tableWidget.setHorizontalHeaderLabels(["IssueID","StudentID","BookID","IssuedDate","ReturnDate","Renewals"])
        # Initializing table row to 0
        tablerow=0
        # Creating connection
        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        s="Select IssueID,Issuedstud,IssuedBID,IssuedDate,ReturnDate,Renewals from issuestud where returned='%s'"
        arg=(v)
        cursor.execute(s%v)
        rows=cursor.fetchall()
        for row in rows:
            # Setting data to table widget column one by one
            self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
            # Increasing row count to move to the next row
            tablerow+=1
            
