from PySide2 import QtCore, QtGui, QtWidgets

class class_for_request_directory():
    #-----------------------------------------------------------------------------------------------------------------------------------
    def write_table(self):
        for i in self.dict_table:
            self.dict_table[i] = QtWidgets.QTableWidget(self)
            self.dict_table[i].setColumnCount(0)
            self.dict_table[i].setRowCount(0)
            
            self.table_of_contents = self.dict_table[i].horizontalHeader()
            self.table_of_contents.sectionClicked.connect(self.click_table_of_contents)
            self.tab.addTab(self.dict_table[i], i)
    
    def write_list(self, i, insert_list):
        self.dict_table[i].setColumnCount(len(insert_list[0]))
        self.dict_table[i].setRowCount(len(insert_list)-1)
        for row in range(1,len(insert_list)):
            for column in range(len(insert_list[0])):
                self.dict_table[i].setItem(row-1, column, QtWidgets.QTableWidgetItem( self.non_none(insert_list[row][column]) ))
        table_of_contents = []
        for j in range(len(insert_list[0])):
            table_of_contents.append(insert_list[0][j]+'_'+str(j))
            self.dict_table[i].setColumnWidth(j, len(table_of_contents[-1])*10)
        self.dict_table[i].setHorizontalHeaderLabels(table_of_contents)
        
    def non_none(self,item):
        if item == None:
            return ''
        else:
            return item

    def len_string(self,x):
        for i in range(20-len(x)):
            x += ' '
        return x

    def cell_calculating(self, event):
        for i in self.dict_table:
            if self.dict_table[i].isVisible():
                self.table_clicked = self.dict_table[i]

                if len(self.table_clicked.selectedIndexes())>1:
                    summ = 0
                    for ix in self.table_clicked.selectedIndexes():
                        try:
                            summ += float(self.table_clicked.item(ix.row(), ix.column()).text().replace(',','.'))
                        except:pass
                    self.string_row.setText(self.len_string(str( round(summ,2)))+'|'+
                                           self.len_string(str(round(summ/len(self.table_clicked.selectedIndexes()),2)))+'|'+
                                           self.len_string(str(len(self.table_clicked.selectedIndexes()))))

    #-----------------------------------------------------------------------------------------------------------------------------------
