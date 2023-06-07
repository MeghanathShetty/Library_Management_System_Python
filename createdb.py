from sys import argv
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from mainui2 import Ui_MainWindow
import mysql.connector 


class Createdb():

    def createdbs(self):
        ck=None
        s=2
        try:
            # Create connection
            conn=mysql.connector.connect(host='localhost',user='root',password='',buffered=True)
            cursorr=conn.cursor()
            sql=("SHOW DATABASES LIKE 'lms'")
            cursorr.execute(sql)
            c=cursorr.fetchone()
            # print(cursorr.fetchone())

            # Check if database already exists
            # if it does not exists
            if c==ck:
                # Create database
                cursorr.execute("CREATE DATABASE lms")

                # create connection and cursor to the new database
                con=mysql.connector.connect(host='localhost',database='lms',user='root',password='',buffered=True)
                cursor=con.cursor()

                # Create book table
                cursor.execute("CREATE TABLE book(BookID varchar(20),Name text,Author varchar(50),Dept text,shelf varchar(15),Avail text,Visible varchar(15))")
                
                # Create issuestaff table
                cursor.execute("CREATE TABLE issuestaff(IssueID varchar(20) PRIMARY KEY,Issuedstaff varchar(20),IssuedBID varchar(20),IssuedDate varchar(25),ReturnDate varchar(25),returned varchar(15) DEFAULT 'no',returneddt varchar(25))")            
                
                # Create issuestud table
                cursor.execute("CREATE TABLE issuestud(IssueID varchar(20) PRIMARY KEY,Issuedstud varchar(20),IssuedBID varchar(20),IssuedDate varchar(25),ReturnDate varchar(25),Fine varchar(20) NOT NULL,Renewals varchar(10),returned varchar(15) DEFAULT 'no',returneddt varchar(25))")

                # Create student table
                cursor.execute("CREATE TABLE student(rollno varchar(20),Fname text,Lname text,course text,Phoneno varchar(15),totalbk varchar(5) DEFAULT '2',Visible varchar(10))")

                # Create staff table
                cursor.execute("CREATE TABLE staff(StaffID varchar(20),Fname text,Lname text,PhoneNo varchar(15),Dept text,totalbk varchar(5) DEFAULT '10',Visible varchar(10))")
                
                con.commit()

            # if database exists
            else:    
                # print("exists")
                pass
        except:
            print("Check if you have installed mysql properly")
