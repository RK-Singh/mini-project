# this works as a main container
import os
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QMainWindow, QTableWidget, QTableWidgetItem, QAction, QAbstractItemView, QHeaderView , qApp , QMessageBox)
from PyQt5.QtCore import Qt
from src.codes.AddEntryWindow import AddEntryWindow
import sqlite3

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.createActions() 
        self.createMenus()
        self.createToolBar()
        self.createTable()
        self.createStatusBar()
        self.popUpModal = None
        
        self.setWindowTitle("Student Registration Management")
        self.resize(720,350)
    
    def createMenus(self):
        '''
        create the menubar 
        '''
        fileMenu = self.menuBar().addMenu('&File')
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.updateAction)
        fileMenu.addAction(self.deleteAction)
        fileMenu.addAction(self.exportAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
        
        #helpMenu = self.menuBar().addMenu('&Help')
        #helpMenu.addSeparator()
        self.menuBar().setVisible(True)
        
    def createStatusBar(self):
        self.statusBar().showMessage("Ready")

    def createToolBar(self):
        self.toolBar = self.addToolBar("File")
        self.toolBar.addAction(self.newAction)
        self.toolBar.addAction(self.updateAction)
        self.toolBar.addAction(self.deleteAction)
        self.toolBar.addAction(self.exportAction)
    
    def createTable(self):
        '''
        create table to view all the student data
        '''
        
        conn = self.openDatabase()
        result = conn.execute("select * from students;")
              
        r = len(result.fetchall())
        result = conn.execute("select * from students order by roll_no;")
        self.table = QTableWidget(r,17,self.centralWidget())
        self.table.setHorizontalHeaderLabels(self.getHeaderText())
        self.setCentralWidget(self.table)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        i,j=0,0
        for row in result:
            j = 0
            for col in row:
                self.table.setItem(i,j,QTableWidgetItem(str(col)))
                j = j + 1
            i = i + 1
        
        
    def getHeaderText(self):
        return ["Roll No.", "Name","Mobile", "Email", "Date of Birth", "Father\'s Name",
            "Father\'s Mobile", "Father\'s Email", "Current Address","Permanent Address",
            "10th pc" , "10 Board", "10 passing year","12th pc", "12 Board",
             "12 passing year", "B. Tech pc"]
    
    
    ################################################
    # event handling
    ################################################
    
    def newEvent(self):
        self.popUpModal = AddEntryWindow(self)
        self.popUpModal.setModal(True)
        self.popUpModal.setWindowTitle("Add New Student Information")
        self.popUpModal.show()
        self.popUpModal.btn_Submit.clicked.connect(self.submitNew)
        
   
        
    def modifyEvent(self):
        self.popUpModal = AddEntryWindow(self)
        row = self.table.currentRow()
        col = 0
        roll = self.table.item(row, col)
        self.popUpModal.txtRollNo.setText(roll.text())
        self.popUpModal.setModal(True)
        self.popUpModal.txtRollNo.setDisabled(True)
        self.popUpModal.setWindowTitle("Modify Student Information")
        self.popUpModal.show()
        self.popUpModal.btn_Submit.clicked.connect(self.submitModify)
        
    def deleteEvent(self):
        row = self.table.currentRow()
        col = 0
        roll = self.table.item(row, col)
        conn = self.openDatabase()
        conn.execute("DELETE FROM STUDENTS WHERE roll_no = {0};".format(roll.text()))
        conn.commit()
        self.createTable()
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Information")
        msgBox.setText("Selected entry is deleted.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.show()

    def exportEvent(self):
        conn = self.openDatabase()
        data = conn.execute("SELECT * FROM STUDENTS order by roll_no ;")
        import csv
        with open("students.csv",'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Roll NO.','Name','Mobile','Email','Date of birth','Father\'s name',
                             'Father\'s Mobile','Father\'s Email','Current Address','Permanent Address',
                             '10th Pc','10th Board','Year of Passing','12th Pc','12th Board',
                             'Year of Passing','B Tech PC'])
            writer.writerows(data)
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Information")
        msgBox.setText("Data successfully exported to \"students.csv\".")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.show()   
        
    def createActions(self):
        # action for add new
        #root = QFileInfo(__file__).absoluteFilePath()
        self.newAction = QAction(QIcon('icons'+ os.sep + 'appbar.page.add.png'),"&New",self)
        self.newAction.setShortcut('Ctrl+N')
        self.newAction.setStatusTip("Add new student detail")
        self.newAction.triggered.connect(self.newEvent)
        # action for update
        self.updateAction = QAction(QIcon('icons'+ os.sep + 'appbar.page.edit.png'),"&Modify",self)
        self.updateAction.setShortcut('Ctrl+M')
        self.updateAction.setStatusTip("Modify student detail")
        self.updateAction.triggered.connect(self.modifyEvent)
        # action for delete
        self.deleteAction = QAction(QIcon('icons'+ os.sep + 'appbar.delete.png'),"&Delete",self)
        self.deleteAction.setShortcut('Ctrl+D')
        self.deleteAction.setStatusTip("Delete student detail")
        self.deleteAction.triggered.connect(self.deleteEvent)
        # action for export
        self.exportAction = QAction(QIcon('icons'+ os.sep + 'appbar.export.png'),"&Export",self)
        self.exportAction.setShortcut('Ctrl+E')
        self.exportAction.setStatusTip("Export to CSV")
        self.exportAction.triggered.connect(self.exportEvent)
        #action for exit
        self.exitAction = QAction('&Exit', self)        
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(qApp.quit)
            
    
    def openDatabase(self):
        conn = sqlite3.connect("data"+os.sep+"students.db")
        statement = 'CREATE TABLE IF NOT EXISTS STUDENTS(roll_no TEXT UNIQUE, name TEXT,\
        mobile TEXT, email TEXT, dob TEXT, fathers_name TEXT, fathers_mobile TEXT, \
        fathers_email TEXT, curr_addr TEXT, perm_addr TEXT, _10pc TEXT, _10board TEXT, \
        _10year TEXT,_12pc TEXT, _12board TEXT, _12year TEXT, btech_pc TEXT);'        
        conn.execute(statement)  
        conn.commit() 
        return conn
    def submitModify(self):
        # add update sql statement
        row = self.table.currentRow()
        col = 0
        roll = self.table.item(row, col)
        self.popUpModal.txtRollNo.setText(roll.text())
        #print("row = "+str(row)+"col = " + str(col)+ "value ="+str(roll))
        conn = self.openDatabase()
        self.centralWidget().destroy()
        self.createTable()
        print("submitModify is clicked")
        ####################################
        # adding student details to database
        
        name = self.popUpModal.txt_studentName.text()
        mob = self.popUpModal.txt_studentMobile.text()
        email = self.popUpModal.txt_studentEmail.text()
        dob = self.popUpModal.dobDD.currentText()+self.popUpModal.dobMM.currentText()+self.popUpModal.dobYYYY.currentText()
        fname = self.popUpModal.txt_fatherName.text()
        femail = self.popUpModal.txt_fatherEmail.text()
        fmob = self.popUpModal.txt_fatherMobile.text()
        currAddr = self.popUpModal.txt_currAddress.toPlainText()
        permAddr = self.popUpModal.txt_permAddress.toPlainText()
        pc10 = self.popUpModal.txt_10Pc.currentText()
        pc12 = self.popUpModal.txt_12Pc.currentText()
        pcBtech = self.popUpModal.txt_BtechPc.currentText()
        board10 = self.popUpModal.txt_10Board.text()
        board12 = self.popUpModal.txt_12Board.text()
        year10 = self.popUpModal.txt_10Year.currentText()
        year12 = self.popUpModal.txt_12Year.currentText()
        
        data = (name, mob,email, dob, fname, femail, fmob, currAddr, permAddr,pc10, board10, year10,
        pc12, board12, year12, pcBtech)
        conn = self.openDatabase()
        conn.execute("UPDATE STUDENTS SET name = ?,mobile = ?,email = ?, dob = ?, fathers_name = ? \
        ,fathers_mobile = ?, fathers_email = ?, curr_addr = ?, perm_addr = ?, _10pc = ?, _10board = ?, \
        _10year = ?,_12pc = ?, _12board = ?, _12year = ?, btech_pc = ? WHERE roll_no = {0};".format(roll.text()),data)


        conn.commit()
        self.createTable()       
        ###################################
        self.popUpModal.destroy()
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Information")
        msgBox.setText("Database successfully updated.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.show()
        
    def submitNew(self):
        # add insert statement
        self.centralWidget().destroy()
        self.createTable()
        print("submitNew is clicked")
        
        ####################################
        # adding student details to database
        
        name = self.popUpModal.txt_studentName.text()
        roll = self.popUpModal.txtRollNo.text()
        mob = self.popUpModal.txt_studentMobile.text()
        email = self.popUpModal.txt_studentEmail.text()
        dob = self.popUpModal.dobDD.currentText()+self.popUpModal.dobMM.currentText()+self.popUpModal.dobYYYY.currentText()
        fname = self.popUpModal.txt_fatherName.text()
        femail = self.popUpModal.txt_fatherEmail.text()
        fmob = self.popUpModal.txt_fatherMobile.text()
        currAddr = self.popUpModal.txt_currAddress.toPlainText()
        permAddr = self.popUpModal.txt_permAddress.toPlainText()
        pc10 = self.popUpModal.txt_10Pc.currentText()
        pc12 = self.popUpModal.txt_12Pc.currentText()
        pcBtech = self.popUpModal.txt_BtechPc.currentText()
        board10 = self.popUpModal.txt_10Board.text()
        board12 = self.popUpModal.txt_12Board.text()
        year10 = self.popUpModal.txt_10Year.currentText()
        year12 = self.popUpModal.txt_12Year.currentText()
        
        data = (roll, name, mob,email, dob, fname, femail, fmob, currAddr, permAddr,pc10, board10, year10,
        pc12, board12, year12, pcBtech)
        conn = self.openDatabase()
        conn.execute("INSERT INTO STUDENTS(roll_no, name,mobile,email, dob, fathers_name \
        ,fathers_mobile, fathers_email , curr_addr, perm_addr, _10pc, _10board, \
        _10year,_12pc, _12board, _12year, btech_pc) values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",data)


        conn.commit()
        self.createTable()       
                
        self.popUpModal.destroy()
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Information")
        msgBox.setText("Database successfully updated.")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.show()
