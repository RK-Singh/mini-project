from src.codes.AddEntryWindow import AddEntryWindow
from src.codes.MainWindow import  MainWindow
from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5.QtGui import QPalette, QColor
import sqlite3
import os

def setFusionTheme(myQApplication):
    myQApplication.setStyle(QStyleFactory.create("Fusion"))
    p = myQApplication.palette()
    p.setColor(QPalette.Window, QColor(52, 73, 94))
    p.setColor(QPalette.Button, QColor(52, 73, 94))
    p.setColor(QPalette.Highlight, QColor(0, 0, 255))
    p.setColor(QPalette.ButtonText, QColor(255, 255, 255))
    p.setColor(QPalette.WindowText, QColor(255, 255, 255))
    myQApplication.setPalette(p)


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    mainWindow = MainWindow()
    setFusionTheme(application)
    mainWindow.show()
    sys.exit(application.exec_())