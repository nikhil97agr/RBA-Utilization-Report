# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import shutil
import re
from typing import final
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import extract_data
import extract_filename
import EWSmailer
import logging

class Ui_MainWindow(object):
    globalFilename=""
    pu_du_list=[]
    def __init__(self):
        self.logFile = None
        #Create and configure logger
        logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')
    
        #Creating an object
        self.logger=logging.getLogger()

        self.logger.setLevel(logging.DEBUG)


    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setFixedSize(739, 431)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setStyleSheet("background-color:rgb(80, 147, 255)")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 41))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("padding-left : 5px;\n"
"background-color:gold;\n"
"color:black;\n"
"border: 2px solid white;\n"
"border-radius : 5px")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.puList = QtWidgets.QComboBox(self.centralwidget)
        self.puList.setGeometry(QtCore.QRect(70, 70, 171, 21))
        self.puList.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border : 2px solid white;\n"
"border-radius : 3px\n"
"")
        self.puList.setCurrentText("")
        self.puList.setObjectName("puList")
        self.duList = QtWidgets.QComboBox(self.centralwidget)
        self.duList.setGeometry(QtCore.QRect(300, 70, 171, 21))
        self.duList.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border : 2px solid white;\n"
"border-radius : 3px\n"
"")
        self.duList.setCurrentText("")
        self.duList.setObjectName("duList")
        self.accountsList = QtWidgets.QComboBox(self.centralwidget)
        self.accountsList.setGeometry(QtCore.QRect(530, 70, 171, 21))
        self.accountsList.setStyleSheet("background-color:white;\n"
"color:black;\n"
"border : 2px solid white;\n"
"border-radius : 3px\n"
"")
        self.accountsList.setObjectName("accountsList")
        self.fileLocation = QtWidgets.QLineEdit(self.centralwidget)
        self.fileLocation.setGeometry(QtCore.QRect(70, 140, 401, 31))
        self.fileLocation.setStyleSheet("padding-left : 5px;\n"
"background-color:white;\n"
"color:black;\n"
"border: 2px solid white;\n"
"border-radius : 5px")
        self.fileLocation.setText("")
        self.fileLocation.setReadOnly(True)
        self.fileLocation.setObjectName("fileLocation")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(530, 140, 171, 31))
        self.browseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browseButton.setStyleSheet("padding-left : 5px;\n"
"background-color:gold;\n"
"color:black;\n"
"border: 2px solid white;\n"
"border-radius : 5px")
        self.browseButton.setObjectName("browseButton")
        self.generateReportButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateReportButton.setGeometry(QtCore.QRect(260, 200, 291, 31))
        self.generateReportButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generateReportButton.setStyleSheet("padding-left : 5px;\n"
"background-color:gold;\n"
"color:black;\n"
"border: 2px solid white;\n"
"border-radius : 5px")
        self.generateReportButton.setObjectName("generateReportButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.reportFileName = QtWidgets.QLineEdit(self.centralwidget)
        self.reportFileName.setGeometry(QtCore.QRect(200, 270, 401, 31))
        self.reportFileName.setStyleSheet("padding-left : 5px;\n"
"background-color:white;\n"
"color:black;\n"
"border: 2px solid white;\n"
"border-radius : 5px")
        self.reportFileName.setText("")
        self.reportFileName.setAlignment(QtCore.Qt.AlignCenter)
        self.reportFileName.setReadOnly(True)
        self.reportFileName.setObjectName("reportFileName")
        self.downloadReport = QtWidgets.QRadioButton(self.centralwidget)
        self.downloadReport.setGeometry(QtCore.QRect(190, 330, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.downloadReport.setFont(font)
        self.downloadReport.setChecked(True)
        self.downloadReport.setObjectName("downloadReport")
        self.emailReport = QtWidgets.QRadioButton(self.centralwidget)
        self.emailReport.setGeometry(QtCore.QRect(390, 330, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.emailReport.setFont(font)
        self.emailReport.setObjectName("emailReport")
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setGeometry(QtCore.QRect(540, 382, 171, 31))
        self.downloadButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.downloadButton.setStyleSheet("padding-left : 5px;\n"
"background-color:gold;\n"
"color:black;\n"
"border: 2px solid white;\n"
"border-radius : 5px")
        self.downloadButton.setObjectName("downloadButton")
        self.emailInput = QtWidgets.QLineEdit(self.centralwidget)
        self.emailInput.setGeometry(QtCore.QRect(80, 379, 401, 31))
        self.emailInput.setToolTip("")
        self.emailInput.setStyleSheet("padding-left : 5px;\n"
"background-color:white;\n"
"color:black;\n"
"border: 2px solid white;\n"
"border-radius : 5px")
        self.emailInput.setText("")
        self.emailInput.setReadOnly(True)
        self.emailInput.setObjectName("emailInput")
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MainWindow)
        self.duList.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.populateList()

        self.emailReport.setEnabled(False)
        self.downloadReport.setEnabled(False)
        self.downloadButton.setEnabled(False)

        self.setupClicks()


    #click events for all the buttons
    def setupClicks(self):

        self.browseButton.clicked.connect(self.browse)
        self.generateReportButton.clicked.connect(self.generateReport)
        self.emailReport.toggled.connect(self.email)
        self.downloadReport.toggled.connect(self.download)
        self.downloadButton.clicked.connect(self.downloadOrSend)

    #function to either email or download report  
    def downloadOrSend(self):
        try:
            popup = QMessageBox()
            if self.downloadButton.text() == "Send":
                self.emailId = self.emailInput.text()
                regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
                #check for valid email id
                if(len(self.emailId) == 0):
                    popup.setIcon(QMessageBox.Critical)
                    popup.setWindowTitle("RBA Generator")
                    popup.setText("Please enter an Email")
                    popup.exec()
                    return
                if(re.search(regex, self.emailId)):
                    EWSmailer.ews_smailer(self.emailId,Ui_MainWindow.globalFilename,Ui_MainWindow.pu_du_list)
                    popup.setIcon(QMessageBox.Information)
                    popup.setWindowTitle("RBA Generator")
                    popup.setText("Email sent successfully")
                    popup.exec()
                    sys.exit()
                else:
                    popup.setIcon(QMessageBox.Critical)
                    popup.setWindowTitle("RBA Generator")
                    popup.setText("Invalid email")
                    popup.exec()
                    return
            else:
                #file to download in particular directory
                dialog = QFileDialog()
                dir = dialog.getExistingDirectory()
                if(len(dir)!=0):
                    # print(dir)
                    xl_loc=self.finalFileName+".xlsx"
                    shutil.copy(xl_loc,dir)
                    self.emailInput.setText(dir+"/"+xl_loc)
                    self.logger.info("File has downloaded at "+dir)

                    popup.setIcon(QMessageBox.Information)
                    popup.setWindowTitle("RBA Generator")
                    popup.setText("Download successful")
                    popup.exec()

                    sys.exit()
        except Exception as ex:
            self.logger.error(str(ex))

        
    #function to setup fields to email the report
    def email(self):
        if  not self.emailReport.isChecked:
            return
        
        self.emailInput.setPlaceholderText("Enter your email")
        self.emailInput.setReadOnly(False)
        self.emailInput.setText("")

        self.downloadButton.setText("Send")


    #function to setup fields to download the report
    def download(self):
        if not self.downloadReport.isChecked:
            return
        
        self.emailInput.setPlaceholderText("File location")
        self.emailInput.setReadOnly(True)
        
        self.downloadButton.setText("Download")
        
    #browse the file log file from file explorer
    def browse(self):
        dialog = QFileDialog()
        
        fname = dialog.getOpenFileName(None, "Select File", "", "Log files (*.log)")

        if len(fname[0]) != 0:
            self.logFile = fname[0]
            self.fileLocation.setText(self.logFile)     
            self.logger.info("Selected log file: "+fname[0]) 

    #function to generate the report 
    def generateReport(self):

        popup = QMessageBox()
        popup.setIcon(QMessageBox.Critical)
        popup.setWindowTitle("RBA Generator")
        
        if self.logFile == None:
            popup.setText("Select a file")
            popup.exec()
            return
        
        if self.puList.currentIndex()==0:
            popup.setText("Select valid PU")
            popup.exec()
            return
        
        if self.duList.currentIndex()==0:
            popup.setText("Select valid DU")
            popup.exec()
            return
        
        if self.accountsList.currentIndex()==0:
            popup.setText("Select valid Account")
            popup.exec()
            return

        #call function to generate report of the file and get the file name
        name_list=[self.puList.currentText(),self.duList.currentText(),self.accountsList.currentText()]
        Ui_MainWindow.pu_du_list=name_list
        self.finalFileName=extract_filename.extract_filename(self.logFile)
        self.finalFileName=self.finalFileName+"_utilization_report_"
        self.finalFileName=extract_data.extract_data(name_list,self.logFile,self.finalFileName)
        Ui_MainWindow.globalFilename=self.finalFileName
        self.reportFileName.setText(self.finalFileName)

        self.downloadReport.setEnabled(True)
        self.emailReport.setEnabled(True)
        self.downloadButton.setEnabled(True)

    #function to fill the drop downs
    def populateList(self):

        self.puList.addItems(["Select PU","AEG","AEG2"])
        self.duList.addItems(["Select DU", "CMT", "MFG", "INS", "BFS", "NOR", "EUR"])
        self.accountsList.addItems(['Select Accounts', "Honda", "Fox", "Viacom"])


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "RBA"))
        self.label.setText(_translate("MainWindow", "RBA Report Generator"))
        self.fileLocation.setPlaceholderText(_translate("MainWindow", "Browse log file......"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.generateReportButton.setText(_translate("MainWindow", "Generate Report"))
        self.label_2.setText(_translate("MainWindow", "Utilization Report"))
        self.reportFileName.setPlaceholderText(_translate("MainWindow", "File name here"))
        self.downloadReport.setText(_translate("MainWindow", "Download Report"))
        self.emailReport.setText(_translate("MainWindow", "Email Report"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.emailInput.setPlaceholderText(_translate("MainWindow", "File Location"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.MainWindow.show()
    sys.exit(app.exec_())