from PySide2 import QtCore, QtGui, QtWidgets
from Class_filtr import *
from Class_for_request_directory import *
import win32clipboard
import json


class class_directory_table(QtWidgets.QWidget,class_filtr, class_for_request_directory):
    def __init__(self):
        super().__init__()


        self.string_row = QtWidgets.QLineEdit(self)
        self.string_row.setText('')
        
        self.btn_insert      = QtWidgets.QPushButton('Вставить', self)
        self.btn_insert.clicked.connect(self.insert_from)
        
        self.btn_record      = QtWidgets.QPushButton('Записать', self)
        self.btn_record.clicked.connect(self.write)
        
        self.btn_update      = QtWidgets.QPushButton('Обновить', self)
        self.btn_update.clicked.connect(self.open_dict)

        self.dict_table = {'Спр 1':None,'Спр 2':None,'Спр 3':None,'Спр 4':None}
        self.tab = QtWidgets.QTabWidget()
        self.write_table()

        self.grid = QtWidgets.QGridLayout()
        

        self.grid.addWidget(self.string_row, 1,1)
        self.grid.addWidget(self.btn_insert, 1,2)
        self.grid.addWidget(self.btn_record, 1,3)
        self.grid.addWidget(self.btn_update, 1,4)
        self.grid.addWidget(self.tab, 2,1,1,4)

        self.setLayout(self.grid)



    def insert_from(self):
        win32clipboard.OpenClipboard() 
        insert_list= [i[:-1].upper().split('\t') for i in win32clipboard.GetClipboardData().split('\n')][:-1]
        win32clipboard.CloseClipboard()
        for i in self.dict_table:
            if self.dict_table[i].isVisible():
                self.write_list(i, insert_list)

 


    def write(self):
        dict_write = {}
        for i in self.dict_table:
            dict_write[i] = {}
            for j in range(self.dict_table[i].columnCount()):
                try:
                    column = self.dict_table[i].horizontalHeaderItem(j).text()
                    dict_write[i][column] = []
                    for row in range(self.dict_table[i].rowCount()):
                        dict_write[i][column].append(self.dict_table[i].item(row, j).text())
                except:pass
      

        with open('source.json', 'w') as file:
            json.dump(dict_write, file)



    def open_dict(self):
        with open('source.json') as file:
            dict_open = json.load(file)

        for i in dict_open:
            insert_list = []
            for j in dict_open[i]:
                column_list = [j] 
                for row in dict_open[i][j]: 
                    column_list.append(row)
                insert_list.append(column_list)
            insert_list = [list(j) for j in zip(*insert_list)]

            if len(insert_list)>0:
                self.write_list(i, insert_list)
                self.dict_table[i].cellPressed.connect(self.cell_calculating)
          
        

