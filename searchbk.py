import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from mainui2 import Ui_MainWindow
from viewexe import ViewBook
import mysql.connector

class SearchBook():

    def searchbkfun(self):
        v='yes'
        # Set Quantity label 0
        self.qtylb.setText("0")
        # Clear the table
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
        self.tableWidget.setHorizontalHeaderLabels(["BookID","Title","Author","Department","Shelf No","Availability"])
        
        # Initializing table row to 0
        tablerow=0
        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        # Get the input
        searchtxt=self.searchbktxt.text()

        # If the input is not empty
        if searchtxt!="":
            # if the combobox index is 0 ie..BookID
            if self.searchbkcombo.currentIndex()==0:
                self.searchbktxt.clear()
                # Get the book detail where BookID=given input
                sqlbkid="Select * from book where BookID='%s' and Visible='%s'"
                argsid=(searchtxt,v)
                self.tableWidget.clear()
                # Setting horizontal header labels
                self.tableWidget.setHorizontalHeaderLabels(["BookID","Title","Author","Department","Shelf No","Availability"])
                cursor.execute(sqlbkid%argsid)
                # Fetch the data from the cursor
                rowsbkid=cursor.fetchall()
                # If the cursor is not empty
                if cursor.rowcount>=1:
                    for row in rowsbkid:
                        # Setting data to table widget column one by one
                        self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                        self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
                        # Increasing row count to move to the next row
                        tablerow+=1
                    self.searchbkemp.setStyleSheet("color: rgb(2, 170, 27);")
                    # Display proper message
                    self.searchbkemp.setText("Search Successfull")
                    # Unhide the labels
                    self.searchbkemp.setHidden(False)  

                    # Get quantity
                    rc=str(cursor.rowcount)
                    # display the quantity in label
                    self.qtylb.setText(rc)

                else:
                    # If the cursor is empty display staff not exist
                    self.searchbkemp.setText("Book does not exist")
                    self.searchbkemp.setStyleSheet("color: rgb(232, 0, 0);")
                    self.searchbkemp.setHidden(False)   
                    # Set Quantity label 0
                    self.qtylb.setText("0")     

            # if the combobox index is 1 ie..Book Name
            elif self.searchbkcombo.currentIndex()==1:
                self.searchbktxt.clear()
                # Get the Book detail where Book Name=given input
                sqlbname="Select * from book where Name='%s' and Visible='%s'"
                argname=(searchtxt,v)
                self.tableWidget.clear()
                # Setting horizontal header labels
                self.tableWidget.setHorizontalHeaderLabels(["BookID","Title","Author","Department","Shelf No","Availability"])
                cursor.execute(sqlbname%argname)
                rowsbkname=cursor.fetchall()
                if cursor.rowcount>=1:
                    for row in rowsbkname:
                        # Setting data to table widget column one by one
                        self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                        self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))

                        # Increasing row count to move to the next row
                        tablerow+=1
                    self.searchbkemp.setStyleSheet("color: rgb(2, 170, 27);")
                    self.searchbkemp.setText("Search Successfull")
                    self.searchbkemp.setHidden(False)
                
                    # Get quantity
                    rc=str(cursor.rowcount)
                    # display the quantity in label
                    self.qtylb.setText(rc)

                else:
                    self.searchbkemp.setStyleSheet("color: rgb(232, 0, 0);")
                    self.searchbkemp.setText("Book does not exist")
                    self.searchbkemp.setHidden(False)  
                    # Set Quantity label 0
                    self.qtylb.setText("0")      

            # if the combobox index is 2 ie..Author
            elif self.searchbkcombo.currentIndex()==2:
                self.searchbktxt.clear()
                # Get book detail where Author=given input(any one author is enough)
                sql="SELECT * from book WHERE FIND_IN_SET('%s',Author) > 0 and Visible='%s'"
                arg=(searchtxt,v)
                self.tableWidget.clear()
                # Setting horizontal header labels
                self.tableWidget.setHorizontalHeaderLabels(["BookID","Title","Author","Department","Shelf No","Availability"])
                cursor.execute(sql%arg)
                rowsbkname=cursor.fetchall()
                if cursor.rowcount>=1:
                    for row in rowsbkname:
                        # Setting data to table widget column one by one
                        self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                        self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))

                        # Increasing row count to move to the next row
                        tablerow+=1
                    self.searchbkemp.setStyleSheet("color: rgb(2, 170, 27);")
                    self.searchbkemp.setText("Search Successfull")
                    self.searchbkemp.setHidden(False)

                    # Get quantity
                    rc=str(cursor.rowcount)
                    # display the quantity in label
                    self.qtylb.setText(rc)

                else:
                    self.searchbkemp.setStyleSheet("color: rgb(232, 0, 0);")
                    self.searchbkemp.setText("Book does not exist")
                    self.searchbkemp.setHidden(False)
                    # Set Quantity label 0
                    self.qtylb.setText("0") 

        else:
            # Display proper message if the input is empty
            self.searchbkemp.setText("Input cannot be empty")  
            self.searchbkemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.searchbkemp.setHidden(False)
            # Set Quantity label 0
            self.qtylb.setText("0") 

        # if the combobox index is 3 ie..Department
        if self.searchbkcombo.currentIndex()==3:
            self.searchbktxt.clear()
            # Get the input from the input combobox(Another combobox which will be visible when searchbkcombo box index=3)
            searchcombo=self.searchbktxtcombo.currentText()
            # Get Book detail where Department=given input
            sqlbdpt="Select * from book where Dept='%s' and Visible='%s'"
            argdpt=(searchcombo,v)
            self.tableWidget.clear()
            # Setting horizontal header labels
            self.tableWidget.setHorizontalHeaderLabels(["BookID","Title","Author","Department","Shelf No","Availability"])
            cursor.execute(sqlbdpt%argdpt)
            rowsbkdpt=cursor.fetchall()
            if cursor.rowcount>=1:
                for row in rowsbkdpt:
                    # Setting data to table widget column one by one
                    self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                    self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                    self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                    self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                    self.tableWidget.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))

                    # Increasing row count to move to the next row
                    tablerow+=1
                self.searchbkemp.setStyleSheet("color: rgb(2, 170, 27);")
                self.searchbkemp.setText("Search Successfull")
                self.searchbkemp.setHidden(False)

                # Get quantity
                rc=str(cursor.rowcount)
                # display the quantity in label
                self.qtylb.setText(rc)
            else:
                self.searchbkemp.setText("Book does not exist")
                self.searchbkemp.setStyleSheet("color: rgb(232, 0, 0);")
                self.searchbkemp.setHidden(False) 
                # Set Quantity label 0
                self.qtylb.setText("0")        

    def memsearchbkfun(self):
        v='yes'
        # Set Quantity label 0
        self.qtylb.setText("0")
        # Clear the table
        self.tableWidget.clear()
        # Setting table widget column count to 5
        self.tableWidget.setColumnCount(5)
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

        # Setting horizontal header labels
        self.tableWidget.setHorizontalHeaderLabels(["BookID","Title","Author","Department","Availability"])
        
        # Initializing table row to 0
        tablerow=0
        con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
        cursor=con.cursor()
        # Get the input
        searchtxt=self.searchbktxt.text()

        # If the input is not empty
        if searchtxt!="":
            # if the combobox index is 0 ie..BookID
            if self.searchbkcombo.currentIndex()==0:
                self.searchbktxt.clear()
                # Get the book detail where BookID=given input
                sqlbkid="Select BookID,Name,Author,Dept,Avail from book where BookID='%s' and Visible='%s'"
                argsid=(searchtxt,v)
                self.tableWidget.clear()
                # Setting horizontal header labels
                self.tableWidget.setHorizontalHeaderLabels(["BookID","Title","Author","Department","Availability"])
                cursor.execute(sqlbkid%argsid)
                # Fetch the data from the cursor
                rowsbkid=cursor.fetchall()
                # If the cursor is not empty
                if cursor.rowcount>=1:
                    for row in rowsbkid:
                        # Setting data to table widget column one by one
                        self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                        # Increasing row count to move to the next row
                        tablerow+=1
                    self.searchbkemp.setStyleSheet("color: rgb(2, 170, 27);")
                    # Display proper message
                    self.searchbkemp.setText("Search Successfull")
                    # Unhide the labels
                    self.searchbkemp.setHidden(False)  

                    # Get quantity
                    rc=str(cursor.rowcount)
                    # display the quantity in label
                    self.qtylb.setText(rc)

                else:
                    # If the cursor is empty display staff not exist
                    self.searchbkemp.setText("Book does not exist")
                    self.searchbkemp.setStyleSheet("color: rgb(232, 0, 0);")
                    self.searchbkemp.setHidden(False)   
                    # Set Quantity label 0
                    self.qtylb.setText("0")     

            # if the combobox index is 1 ie..Book Name
            elif self.searchbkcombo.currentIndex()==1:
                self.searchbktxt.clear()
                # Get the Book detail where Book Name=given input
                sqlbname="Select BookID,Name,Author,Dept,Avail from book where Name='%s' and Visible='%s'"
                argname=(searchtxt,v)
                self.tableWidget.clear()
                # Setting horizontal header labels
                self.tableWidget.setHorizontalHeaderLabels(["BookID","Title","Author","Department","Availability"])
                cursor.execute(sqlbname%argname)
                rowsbkname=cursor.fetchall()
                if cursor.rowcount>=1:
                    for row in rowsbkname:
                        # Setting data to table widget column one by one
                        self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                        # Increasing row count to move to the next row
                        tablerow+=1
                    self.searchbkemp.setStyleSheet("color: rgb(2, 170, 27);")
                    self.searchbkemp.setText("Search Successfull")
                    self.searchbkemp.setHidden(False)
                
                    # Get quantity
                    rc=str(cursor.rowcount)
                    # display the quantity in label
                    self.qtylb.setText(rc)

                else:
                    self.searchbkemp.setStyleSheet("color: rgb(232, 0, 0);")
                    self.searchbkemp.setText("Book does not exist")
                    self.searchbkemp.setHidden(False)  
                    # Set Quantity label 0
                    self.qtylb.setText("0")      

            # if the combobox index is 2 ie..Author
            elif self.searchbkcombo.currentIndex()==2:
                self.searchbktxt.clear()
                # Get book detail where Author=given input(any one author is enough)
                sql="SELECT BookID,Name,Author,Dept,Avail from book WHERE FIND_IN_SET('%s',Author) > 0 and Visible='%s'"
                arg=(searchtxt,v)
                self.tableWidget.clear()
                # Setting horizontal header labels
                self.tableWidget.setHorizontalHeaderLabels(["BookID","Title","Author","Department","Availability"])
                cursor.execute(sql%arg)
                rowsbkname=cursor.fetchall()
                if cursor.rowcount>=1:
                    for row in rowsbkname:
                        # Setting data to table widget column one by one
                        self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                        self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                        self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                        self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                        self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                        # Increasing row count to move to the next row
                        tablerow+=1
                    self.searchbkemp.setStyleSheet("color: rgb(2, 170, 27);")
                    self.searchbkemp.setText("Search Successfull")
                    self.searchbkemp.setHidden(False)

                    # Get quantity
                    rc=str(cursor.rowcount)
                    # display the quantity in label
                    self.qtylb.setText(rc)

                else:
                    self.searchbkemp.setStyleSheet("color: rgb(232, 0, 0);")
                    self.searchbkemp.setText("Book does not exist")
                    self.searchbkemp.setHidden(False)
                    # Set Quantity label 0
                    self.qtylb.setText("0") 

        else:
            # Display proper message if the input is empty
            self.searchbkemp.setText("Input cannot be empty")  
            self.searchbkemp.setStyleSheet("color: rgb(232, 0, 0);")
            self.searchbkemp.setHidden(False)
            # Set Quantity label 0
            self.qtylb.setText("0") 

        # if the combobox index is 3 ie..Department
        if self.searchbkcombo.currentIndex()==3:
            self.searchbktxt.clear()
            # Get the input from the input combobox(Another combobox which will be visible when searchbkcombo box index=3)
            searchcombo=self.searchbktxtcombo.currentText()
            # Get Book detail where Department=given input
            sqlbdpt="Select BookID,Name,Author,Dept,Avail from book where Dept='%s' and Visible='%s'"
            argdpt=(searchcombo,v)
            self.tableWidget.clear()
            # Setting horizontal header labels
            self.tableWidget.setHorizontalHeaderLabels(["BookID","Title","Author","Department","Availability"])
            cursor.execute(sqlbdpt%argdpt)
            rowsbkdpt=cursor.fetchall()
            if cursor.rowcount>=1:
                for row in rowsbkdpt:
                    # Setting data to table widget column one by one
                    self.tableWidget.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                    self.tableWidget.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                    self.tableWidget.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                    self.tableWidget.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                    self.tableWidget.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                    # Increasing row count to move to the next row
                    tablerow+=1
                self.searchbkemp.setStyleSheet("color: rgb(2, 170, 27);")
                self.searchbkemp.setText("Search Successfull")
                self.searchbkemp.setHidden(False)

                # Get quantity
                rc=str(cursor.rowcount)
                # display the quantity in label
                self.qtylb.setText(rc)
            else:
                self.searchbkemp.setText("Book does not exist")
                self.searchbkemp.setStyleSheet("color: rgb(232, 0, 0);")
                self.searchbkemp.setHidden(False) 
                # Set Quantity label 0
                self.qtylb.setText("0")
                






            
