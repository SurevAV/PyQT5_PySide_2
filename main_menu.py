from PySide2 import QtCore, QtGui, QtWidgets
from Class_filtr import *
from Class_directory import *
from Class_request import *
import win32clipboard
import json
import os

class Menu_list():
    def menu_list(self):
        menulist = self.menuBar()
        menu = QtWidgets.QMenu('Меню', self)
        
        
        menu_directory = QtWidgets.QAction("Таблицы из json", self) 
        menu_directory.triggered.connect(self.directory_table)

        menu_open = QtWidgets.QAction("Таблицы из sql", self) 
        menu_open.triggered.connect(self.request_open)

        

        
        menu.addAction(menu_directory)
        menu.addAction(menu_open)
        menulist.addMenu(menu)

    def directory_table(self):
        report = class_directory_table()
        self.mdiArea.addSubWindow(report)
        report.show()

    def request_open(self):
        report = class_request()
        self.mdiArea.addSubWindow(report)
        report.show()
        
        
        

class MainWindow(QtWidgets.QMainWindow,Menu_list):
    def __init__(self):
        super().__init__()


        app.setStyle("fusion")
        palette = QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(180,180,140))#
        palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Base, QtGui.QColor(190,180,150))
        palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Text,QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.Button, QtGui.QColor(190,180,150))
        palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(0,0,0))
        palette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(255,0,0))
        palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(140,130,100))#.lighter()
        palette.setColor(QtGui.QPalette.HighlightedText, QtCore.Qt.black)
        app.setPalette(palette)
        
 
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(QtWidgets.QVBoxLayout(self.centralwidget))
        
        self.mdiArea = QtWidgets.QMdiArea()

      
        
        self.centralwidget.layout().addWidget(self.mdiArea)
        self.menu_list()

            


            
        

#if __name__ == '__main__':
import sys
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())
