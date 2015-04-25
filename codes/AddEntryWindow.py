from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class AddEntryWindow(QDialog):
    def __init__(self,parent=None):
        super(AddEntryWindow, self).__init__(parent)
        self.addRollNoArea()
        self.addDetailsArea()
        self.addMarksArea()
        self.addButtons()
        self.addBtnActions()
    #
    def addRollNoArea(self):
        leftSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        rightSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
               
        self.lblRollNo = QLabel("Roll No:")
        self.txtRollNo = QLineEdit()
        self.txtRollNo.setText("")
        self.setLayout(QVBoxLayout())
        hLayout = QHBoxLayout()
        hLayout.addSpacerItem(leftSpacer)
        hLayout.addWidget(self.lblRollNo)
        hLayout.addWidget(self.txtRollNo)
        hLayout.addSpacerItem(rightSpacer)
        self.layout().addLayout(hLayout)
        
    def addBtnActions(self):
        self.btn_Clear.clicked.connect(self.clearBtnClicked)
        #self.btn_Submit.clicked.connect(self.submitBtnClicked)
        
    def addDetailsArea(self):
        self.detailsLayout = QGridLayout()
        self.addStudentDetailsArea()
        self.addDateOfBirth()
        self.addFathersDetailArea()
        self.addAddressDetailsArea()
        
    def addStudentDetailsArea(self):
        # components for student name
        self.lbl_studentName = QLabel("Name")
        self.detailsLayout.addWidget(
            self.lbl_studentName, 0, 0, 1, 1, Qt.AlignRight)
        self.txt_studentName = QLineEdit()
        self.detailsLayout.addWidget(self.txt_studentName, 0, 1, 1, 1)
        self.lbl_studentMobile = QLabel("Mobile")
        self.detailsLayout.addWidget(
            self.lbl_studentMobile, 0, 3, 1, 1, Qt.AlignRight)
        self.txt_studentMobile = QLineEdit()
        self.txt_studentMobile.setText("")
        self.detailsLayout.addWidget(self.txt_studentMobile, 0, 4, 1, 1)
        # components for student email
        self.lbl_studentEmail =  QLabel("Email")
        self.detailsLayout.addWidget(
            self.lbl_studentEmail, 1, 0, 1, 1, Qt.AlignRight)
        self.txt_studentEmail =  QLineEdit()
        self.detailsLayout.addWidget(self.txt_studentEmail, 1, 1, 1, 1)
        # components for date of birth
     
    def addDateOfBirth(self):
        self.lbl_studentDob =  QLabel("Date of birth")
        self.detailsLayout.addWidget(
            self.lbl_studentDob, 1, 3, 1, 1, Qt.AlignRight)
        # dobLayout holds 3 comboboxes each for dd mm yyyy
    
        self.dobLayout =  QHBoxLayout()
        self.dobDD =  QComboBox()
        self.dobLayout.addWidget(self.dobDD)
        self.dobMM =  QComboBox()
        self.dobLayout.addWidget(self.dobMM)
        self.dobYYYY =  QComboBox()
        self.dobLayout.addWidget(self.dobYYYY)
        
        self.generateDob()
        
    def generateDob(self):
        # generating and adding items to combobox components
        self.dobDD.addItems(map(str, range(1, 32)))
        self.dobMM.addItems(map(str, range(1, 13)))
        self.dobYYYY.addItems(map(str, range(1970, 2000)))
        dobLayoutSpacer =  QSpacerItem(
            40, 20,  QSizePolicy.Expanding,  QSizePolicy.Minimum)
        self.dobLayout.addItem(dobLayoutSpacer)
        self.detailsLayout.addLayout(self.dobLayout, 1, 4, 1, 1)
        
    def addFathersDetailArea(self):
        # components for father's name
        self.lbl_fatherName =  QLabel("Father\'s Name")
        self.detailsLayout.addWidget(
            self.lbl_fatherName, 2, 0, 1, 1, Qt.AlignRight)
        self.txt_fatherName =  QLineEdit()
        self.detailsLayout.addWidget(self.txt_fatherName, 2, 1, 1, 1)
        # components for father's mobile
        self.lbl_fatherMobile =  QLabel("Father\'s Mobile")
        self.detailsLayout.addWidget(
            self.lbl_fatherMobile, 2, 3, 1, 1, Qt.AlignRight)
        self.txt_fatherMobile =  QLineEdit()
        self.detailsLayout.addWidget(self.txt_fatherMobile, 2, 4, 1, 1)

        # components for father's email
        self.lbl_fatherEmail =  QLabel("Father\'s Email")
        self.txt_fatherEmail =  QLineEdit()
        self.detailsLayout.addWidget(
            self.lbl_fatherEmail, 3, 0, 1, 1, Qt.AlignRight)
        self.detailsLayout.addWidget(self.txt_fatherEmail, 3, 1, 1, 1)
    
    def addAddressDetailsArea(self):
        # components for current address
        self.lbl_currAddress =  QLabel("Current Address")
        self.detailsLayout.addWidget(self.lbl_currAddress, 4, 0, 1, 2)
        self.txt_currAddress =  QTextEdit()
        self.detailsLayout.addWidget(self.txt_currAddress, 5, 1, 1, 1)

        # components for permanent address
        self.lbl_permAddress =  QLabel("Permanent Address")
        self.detailsLayout.addWidget(self.lbl_permAddress, 4, 3, 1, 2)
        self.txt_permAddress =  QTextEdit()
        self.detailsLayout.addWidget(self.txt_permAddress, 5, 4, 1, 1)
        self.layout().addLayout(self.detailsLayout)

    def addMarksArea(self):
        self.marksLayout = QGridLayout()
        self.add10thMarksArea()
        self.add12thMarksArea()
        self.addBtechMarksArea()
        
    def add10thMarksArea(self):
        # components for 10th exam PC, Board and year of passing
        self.lbl_10Pc = QLabel("10th %")
        self.marksLayout.addWidget(self.lbl_10Pc, 0, 0, 1, 1)
        self.txt_10Pc = QComboBox()
        self.marksLayout.addWidget(self.txt_10Pc, 0, 1, 1, 1)

        self.lbl_10Board = QLabel("Board")
        self.marksLayout.addWidget(self.lbl_10Board, 0, 3, 1, 1)
        self.txt_10Board = QLineEdit()
        self.marksLayout.addWidget(self.txt_10Board, 0, 4, 1, 1)

        self.lbl_10Year = QLabel("passing year")
        self.marksLayout.addWidget(self.lbl_10Year, 0, 6, 1, 1)
        self.txt_10Year = QComboBox()
        self.marksLayout.addWidget(self.txt_10Year, 0, 7, 1, 1)

    def add12thMarksArea(self):
        # components for 12th exam
        self.lbl_12Pc = QLabel("12th %")
        self.marksLayout.addWidget(self.lbl_12Pc, 1, 0, 1, 1)
        self.txt_12Pc = QComboBox()
        self.marksLayout.addWidget(self.txt_12Pc, 1, 1, 1, 1)

        self.lbl_12Board = QLabel("Board")
        self.marksLayout.addWidget(self.lbl_12Board, 1, 3, 1, 1)
        self.txt_12Board = QLineEdit()
        self.marksLayout.addWidget(self.txt_12Board, 1, 4, 1, 1)

        self.lbl_12Year = QLabel("passing year")
        self.marksLayout.addWidget(self.lbl_12Year, 1, 6, 1, 1)
        self.txt_12Year = QComboBox()
        self.marksLayout.addWidget(self.txt_12Year, 1, 7, 1, 1)
    
    def addBtechMarksArea(self):
        # components for B.Tech
        self.lbl_BtechPc = QLabel("B.Tech %")
        self.marksLayout.addWidget(self.lbl_BtechPc, 2, 0, 1, 1)
        self.txt_BtechPc = QComboBox()
        self.marksLayout.addWidget(self.txt_BtechPc, 2, 1, 1, 1)

        marksLayoutPcBoardSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.marksLayout.addItem(marksLayoutPcBoardSpacer, 0, 2, 1, 1)
        marksLayoutBoardYearSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.marksLayout.addItem(marksLayoutBoardYearSpacer, 0, 5, 1, 1)
        self.generateMarksComboBoxData()
        
        self.detailsLayout.addLayout(self.marksLayout, 7, 0, 1, 5)
        
    def generateMarksComboBoxData(self):
        # generating and adding items for comboboxes
        self.txt_10Pc.addItems(map(str, range(30, 101)))
        self.txt_10Year.addItems(map(str, range(2000, 2017)))
        self.txt_12Pc.addItems(map(str, range(30, 101)))
        self.txt_12Year.addItems(map(str, range(2000, 2017)))
        self.txt_BtechPc.addItems(map(str, range(30, 101)))

    def addButtons(self):
        # bottomLayout holds btn_Clear and btn_submit
        self.bottomLayout = QHBoxLayout()
        bottomLayoutSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.bottomLayout.addItem(bottomLayoutSpacer)
        self.btn_Clear = QPushButton("Clear")
        self.bottomLayout.addWidget(self.btn_Clear)
        self.btn_Submit = QPushButton("Submit")
        self.bottomLayout.addWidget(self.btn_Submit)
        self.layout().addLayout(self.bottomLayout)
    
    def clearBtnClicked(self):
        self.txtRollNo.setText("")
        self.txt_studentName.setText("")
        self.txt_studentMobile.setText("")
        self.txt_studentEmail.setText("")
        self.txt_fatherName.setText("")
        self.txt_fatherMobile.setText("")
        self.txt_fatherEmail.setText("")
        self.txt_currAddress.setText("")
        self.txt_permAddress.setText("")
        self.txt_10Pc.setCurrentIndex(0)
        self.txt_10Board.setText("")
        self.txt_10Year.setCurrentIndex(0)
        self.txt_12Pc.setCurrentIndex(0)
        self.txt_12Board.setText("")
        self.txt_12Year.setCurrentIndex(0)
        self.txt_BtechPc.setCurrentIndex(0)
        self.dobDD.setCurrentIndex(0)
        self.dobMM.setCurrentIndex(0)
        self.dobYYYY.setCurrentIndex(0)
