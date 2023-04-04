from PySide6 import QtCore, QtGui, QtWidgets
from Moduls.models import *

import UI.more_info_ui
import UI.find_info_ui

class ShowPage1(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = parent
        
        self.more_info_window = QtWidgets.QWidget()
        

        self.ui.comboBox.currentTextChanged.connect(self.show_table)
        self.ui.comboBox.currentTextChanged.connect(self.clear_com)
        self.ui.comboBox_2.currentTextChanged.connect(self.show_table)
        self.ui.comboBox_3.currentTextChanged.connect(self.show_table)
        self.ui.pushButton.clicked.connect(self.more_info)
        self.ui.pushButton_2.clicked.connect(self.find_info)
    
        self.ui.lineEdit_4.textChanged[str].connect(self.dynamic_search)

    
    def dynamic_search(self):
        find_str = self.ui.lineEdit_4.text()
        text = self.ui.tableWidget.findItems(find_str, QtCore.Qt.MatchFlag.MatchFixedString|QtCore.Qt.MatchFlag.MatchContains)
        for i in text:
            self.ui.tableWidget.setCurrentItem(i)
            self.ui.tableWidget.selectRow(self.ui.tableWidget.currentRow())
    
    
    def search(self, fild):
        text = self.ui.tableWidget.findItems(fild, QtCore.Qt.MatchFlag.MatchFixedString)
        
        for i in text:            
            self.ui.tableWidget.setCurrentItem(i)
            self.ui.tableWidget.selectRow(self.ui.tableWidget.currentRow())
    
    
    def find_info(self):
        self.find_info_window = QtWidgets.QWidget()
        self.ui_find = UI.find_info_ui.Ui_Form()
        self.ui_find.setupUi(self.find_info_window)
        self.find_info_window.show()
        
        if self.ui.comboBox.currentText() == "Специальности" or \
            self.ui.comboBox.currentText() == "Группы":
            
            def bp():
                find_id = self.ui_find.lineEdit_2.text()
                find_name = self.ui_find.lineEdit_4.text()
                
                self.search(find_id)
                self.search(find_name)
                self.find_info_window.close()        
                
            
            self.ui_find.lineEdit.setText("id")
            self.ui_find.lineEdit_3.setText("name")
            
            self.ui_find.lineEdit_5.setVisible(False)
            self.ui_find.lineEdit_6.setVisible(False)
            self.ui_find.lineEdit_7.setVisible(False)
            self.ui_find.lineEdit_8.setVisible(False)
        
            self.ui_find.pushButton.clicked.connect(bp)
            
        elif self.ui.comboBox.currentText() == "Студенты" or \
            self.ui.comboBox.currentText() == "Архив" or self.ui.comboBox.currentText() == "Приказы":
            
            def bp():
                find_id = self.ui_find.lineEdit_2.text()
                find_name = self.ui_find.lineEdit_4.text()
                find_diplom = self.ui_find.lineEdit_6.text()
                
                self.search(find_id)
                self.search(find_name)
                self.search(find_diplom)
                self.find_info_window.close()        
                
            
            self.ui_find.lineEdit.setText("id")
            self.ui_find.lineEdit_3.setText("diplom")
            self.ui_find.lineEdit_5.setText("name")
            
            self.ui_find.lineEdit_7.setVisible(False)
            self.ui_find.lineEdit_8.setVisible(False)
        
            self.ui_find.pushButton.clicked.connect(bp)
        
    
    def show_more_info(self, column_list, data):
        """Create table for needed info and column"""
        
        self.ui_ins = UI.more_info_ui.Ui_Form()
        self.ui_ins.setupUi(self.more_info_window)
        self.more_info_window.show()
                
        self.ui_ins.tableWidget.setRowCount(1)
        self.ui_ins.tableWidget.setColumnCount(len(column_list))
        self.ui_ins.tableWidget.setHorizontalHeaderLabels(
            column_list
        )
    
    
    def more_info(self):
        id = int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text())
        
        if self.ui.comboBox.currentText() == "Специальности":
            column_list = ["id", "name", "price", "countGroup", "countStudent"]
            
            with db:
                data = Spec.select().where(Spec.id == id)
                group_count = Group.select(Group.id).join(Spec).where(Spec.id == id).count()
                student_count = Student.select(Student.id).join(Group).join(Spec).where(Spec.id == id).count()
            
            # create needed headers
            self.show_more_info(column_list=column_list, data=data)
            
            # show data in new window      
            for i in data:
                self.ui_ins.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui_ins.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui_ins.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(i.price)))
                self.ui_ins.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(group_count)))
                self.ui_ins.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(student_count)))
                
        elif self.ui.comboBox.currentText() == "Группы":
            column_list = ["id", "name", "course", "curator", "specName", "countStudent"]
            
            with db:
                data = Group.select().where(Group.id == id)
                spec_name = Group.select().join(Spec).where(Group.id == id).get()
                student_count = Student.select(Student.id).join(Group).where(Group.id == id).count()
            
            # create needed headers
            self.show_more_info(column_list=column_list, data=data)
            
            # show data in new window      
            for i in data:
                self.ui_ins.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui_ins.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui_ins.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(i.course)))
                self.ui_ins.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(i.curator)))
                self.ui_ins.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(spec_name.name)))
                self.ui_ins.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(student_count)))
                
        elif self.ui.comboBox.currentText() == "Студенты":
            column_list = ["id", "diplom", "fname", "lname",
                           "enrollment", "status", "paid", "groupName", "specName"]
            
            with db:
                data = Student.select().where(Student.id == id)
                group_name = Student.select().join(Group).where(Student.id == id).get()
                spec_name = Student.select().join(Group).join(Spec).where(Student.id == id).get()
            
            # create needed headers
            self.show_more_info(column_list=column_list, data=data)
            
            # show data in new window      
            for i in data:
                self.ui_ins.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui_ins.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui_ins.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(i.fname)))
                self.ui_ins.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(i.lname)))
                self.ui_ins.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(i.enrollment)))
                self.ui_ins.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(i.status)))
                self.ui_ins.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem(str(i.paid)))
                self.ui_ins.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem(str(group_name.groupid.name)))
                self.ui_ins.tableWidget.setItem(0, 8, QtWidgets.QTableWidgetItem(str(spec_name.groupid.specid.name)))
            
        elif self.ui.comboBox.currentText() == "Приказы":
            column_list = ["id", "lname", "diplom", "rep_date", "reason"]
            
            with db:
                data = Report.select().where(Report.id == id)
            
            # create needed headers
            self.show_more_info(column_list=column_list, data=data)
            
            # show data in new window      
            for i in data:
                self.ui_ins.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui_ins.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.lname)))
                self.ui_ins.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui_ins.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(i.rep_date)))
                self.ui_ins.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(i.reason)))
               
        elif self.ui.comboBox.currentText() == "Архив":
            column_list = ["id", "diplom", "name", "enrollment",
                           "expulsion", "course", "specName", "reason"]
            
            with db:
                data = Archive.select().where(Archive.id == id)
            
            # create needed headers
            self.show_more_info(column_list=column_list, data=data)
            
            # show data in new window      
            for i in data:
                self.ui_ins.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui_ins.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui_ins.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui_ins.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str(i.enrollment)))
                self.ui_ins.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem(str(i.expulsion)))
                self.ui_ins.tableWidget.setItem(0, 5, QtWidgets.QTableWidgetItem(str(i.course)))
                self.ui_ins.tableWidget.setItem(0, 6, QtWidgets.QTableWidgetItem(str(i.specName)))
                self.ui_ins.tableWidget.setItem(0, 7, QtWidgets.QTableWidgetItem(str(i.reason)))
    
    
    def clear_com(self):
        """Clear old data from filter combobox for new data"""
        self.ui.comboBox_2.clear()
        self.ui.comboBox_3.clear()
        
        
    def show_table(self):
        
        if self.ui.comboBox.currentText() == "Специальности":
            self.ui.lineEdit_2.setVisible(False)
            self.ui.comboBox_2.setVisible(False)

            self.ui.lineEdit_3.setVisible(False)
            self.ui.comboBox_3.setVisible(False) 
            
            with db:
                spec = Spec.select()
            column_list = ["id", "name", "price"]
            
            self.ui.tableWidget.setColumnCount(len(column_list))
            self.ui.tableWidget.setRowCount(spec.count())
            self.ui.tableWidget.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in spec:
                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.price)))
                count += 1
                
        elif self.ui.comboBox.currentText() == "Преподаватели":
            self.ui.lineEdit_2.setVisible(False)
            self.ui.comboBox_2.setVisible(False)

            self.ui.lineEdit_3.setVisible(False)
            self.ui.comboBox_3.setVisible(False) 
            
            with db:
                spec = Teacher.select()
            column_list = ["id", "name"]
            
            self.ui.tableWidget.setColumnCount(len(column_list))
            self.ui.tableWidget.setRowCount(spec.count())
            self.ui.tableWidget.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in spec:
                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                count += 1
                
        elif self.ui.comboBox.currentText() == "Дисциплины":
            self.ui.lineEdit_2.setVisible(False)
            self.ui.comboBox_2.setVisible(False)

            self.ui.lineEdit_3.setVisible(False)
            self.ui.comboBox_3.setVisible(False) 
            
            with db:
                disc = Discipline.select()
            column_list = ["id", "name", "specid", "start", "end"]
            
            self.ui.tableWidget.setColumnCount(len(column_list))
            self.ui.tableWidget.setRowCount(disc.count())
            self.ui.tableWidget.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in disc:
                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.specid)))
                self.ui.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.start)))
                self.ui.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.end)))
                count += 1
                
        elif self.ui.comboBox.currentText() == "Загрузка преподавателей":
            self.ui.lineEdit_2.setVisible(False)
            self.ui.comboBox_2.setVisible(False)

            self.ui.lineEdit_3.setVisible(False)
            self.ui.comboBox_3.setVisible(False) 
            
            with db:
                spec = Teacher_discipline.select()
            column_list = ["id", "teachid", "discid"]
            
            self.ui.tableWidget.setColumnCount(len(column_list))
            self.ui.tableWidget.setRowCount(spec.count())
            self.ui.tableWidget.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in spec:
                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.teachid)))
                self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.discid)))
                count += 1
                
        elif self.ui.comboBox.currentText() == "Учебный график":
            """!!!!!!!!!!!!!!"""
            self.ui.lineEdit_2.setVisible(False)
            self.ui.comboBox_2.setVisible(False)

            self.ui.lineEdit_3.setVisible(False)
            self.ui.comboBox_3.setVisible(False) 
            
            with db:
                spec = Study_schedule.select()
            column_list = ["id", "iddisc", "idspec", "start", "end",
                           "sem1_o", "sem1_e", "sem2_o", "sem2_e",
                           "sem3_o", "sem3_e", "sem4_o", "sem4_e",
                           "sem5_o", "sem5_e", "sem6_o", "sem6_e",
                           "sem7_o", "sem7_e", "sem8_o", "sem8_e"]
            
            self.ui.tableWidget.setColumnCount(len(column_list))
            self.ui.tableWidget.setRowCount(spec.count())
            self.ui.tableWidget.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in spec:
                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.iddisc)))
                self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.idspec)))
                self.ui.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.start)))
                self.ui.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.end)))
                self.ui.tableWidget.setItem(count, 5, QtWidgets.QTableWidgetItem(str(i.sem1_o)))
                self.ui.tableWidget.setItem(count, 6, QtWidgets.QTableWidgetItem(str(i.sem1_e)))
                self.ui.tableWidget.setItem(count, 7, QtWidgets.QTableWidgetItem(str(i.sem2_o)))
                self.ui.tableWidget.setItem(count, 8, QtWidgets.QTableWidgetItem(str(i.sem2_e)))
                self.ui.tableWidget.setItem(count, 9, QtWidgets.QTableWidgetItem(str(i.sem3_o)))
                self.ui.tableWidget.setItem(count, 10, QtWidgets.QTableWidgetItem(str(i.sem3_e)))
                self.ui.tableWidget.setItem(count, 11, QtWidgets.QTableWidgetItem(str(i.sem4_o)))
                self.ui.tableWidget.setItem(count, 12, QtWidgets.QTableWidgetItem(str(i.sem4_e)))
                self.ui.tableWidget.setItem(count, 13, QtWidgets.QTableWidgetItem(str(i.sem5_o)))
                self.ui.tableWidget.setItem(count, 14, QtWidgets.QTableWidgetItem(str(i.sem5_e)))
                self.ui.tableWidget.setItem(count, 15, QtWidgets.QTableWidgetItem(str(i.sem6_o)))
                self.ui.tableWidget.setItem(count, 16, QtWidgets.QTableWidgetItem(str(i.sem6_e)))
                self.ui.tableWidget.setItem(count, 17, QtWidgets.QTableWidgetItem(str(i.sem7_o)))
                self.ui.tableWidget.setItem(count, 18, QtWidgets.QTableWidgetItem(str(i.sem7_e)))
                self.ui.tableWidget.setItem(count, 19, QtWidgets.QTableWidgetItem(str(i.sem8_o)))
                self.ui.tableWidget.setItem(count, 20, QtWidgets.QTableWidgetItem(str(i.sem8_e)))
                count += 1
                
        elif self.ui.comboBox.currentText() == "Группы":
            
            self.ui.lineEdit_2.setVisible(True)
            self.ui.lineEdit_2.setText("Специальность")
            self.ui.comboBox_2.setVisible(True)
            
            if not [self.ui.comboBox_2.itemText(i) for i in range(self.ui.comboBox_2.count())]: 
                data = ["<--Не выбран-->"]
                with db:
                    temp = Spec.select()
                    
                for i in temp:
                    data.append(i.name)    
                self.ui.comboBox_2.addItems(data)
            
            self.ui.lineEdit_3.setVisible(True)
            self.ui.lineEdit_3.setText("Курс")
            self.ui.comboBox_3.setVisible(True) 

            if not [self.ui.comboBox_3.itemText(i) for i in range(self.ui.comboBox_3.count())]: 
                self.ui.comboBox_3.addItems(["<--Не выбран-->", "1", "2", "3", "4"])
            
            with db:
                if self.ui.comboBox_2.currentText() != "<--Не выбран-->" and \
                    self.ui.comboBox_3.currentText() != "<--Не выбран-->":
                    groups = Group.select().join(Spec).where(
                        Spec.name == self.ui.comboBox_2.currentText(),
                        Group.course == int(self.ui.comboBox_3.currentText())
                    )
                
                elif self.ui.comboBox_2.currentText() != "<--Не выбран-->":
                    groups = Group.select().join(Spec).where(Spec.name == self.ui.comboBox_2.currentText())
                
                elif self.ui.comboBox_3.currentText() != "<--Не выбран-->":
                    groups = Group.select().where(Group.course == int(self.ui.comboBox_3.currentText()))
                 
                else:
                    groups = Group.select()
                
            column_list = ["id", "name", "course", "curator", "specid"]
            
            self.ui.tableWidget.setColumnCount(len(column_list))
            self.ui.tableWidget.setRowCount(groups.count())
            self.ui.tableWidget.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in groups:
                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.course)))
                self.ui.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.curator)))
                self.ui.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.specid)))
                count += 1
                
        elif self.ui.comboBox.currentText() == "Студенты":
            
            self.ui.lineEdit_2.setVisible(True)
            self.ui.lineEdit_2.setText("Группа")
            self.ui.comboBox_2.setVisible(True)
            
            if not [self.ui.comboBox_2.itemText(i) for i in range(self.ui.comboBox_2.count())]: 
                data = ["<--Не выбран-->"]
                with db:
                    temp = Group.select()
                    
                for i in temp:
                    data.append(i.name)    
                self.ui.comboBox_2.addItems(data)
            
            self.ui.lineEdit_3.setVisible(True)
            self.ui.lineEdit_3.setText("Тип обучения")
            self.ui.comboBox_3.setVisible(True) 
            if not [self.ui.comboBox_3.itemText(i) for i in range(self.ui.comboBox_3.count())]: 
                self.ui.comboBox_3.addItems(["<--Не выбран-->", "Очно", "Заочно"])
            
            with db:
                if self.ui.comboBox_2.currentText() != "<--Не выбран-->" and \
                    self.ui.comboBox_3.currentText() != "<--Не выбран-->":
                    students = Student.select().join(Group).where(
                        Group.name == str(self.ui.comboBox_2.currentText()),
                        Student.status == str(self.ui.comboBox_3.currentText())
                    )
                
                elif self.ui.comboBox_2.currentText() != "<--Не выбран-->":
                    students = Student.select().join(Group).where(Group.name == str(self.ui.comboBox_2.currentText()))
                
                elif self.ui.comboBox_3.currentText() != "<--Не выбран-->":
                    students = Student.select().where(Student.status == self.ui.comboBox_3.currentText())
                 
                else:
                    students = Student.select()
                
            column_list = ["id", "diplom", "fname", "lname", "enrollment",
                           "status", "paid", "groupid"]
            
            self.ui.tableWidget.setColumnCount(len(column_list))
            self.ui.tableWidget.setRowCount(students.count())
            self.ui.tableWidget.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in students:
                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.fname)))
                self.ui.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.lname)))
                self.ui.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.enrollment)))
                self.ui.tableWidget.setItem(count, 5, QtWidgets.QTableWidgetItem(str(i.status)))
                self.ui.tableWidget.setItem(count, 6, QtWidgets.QTableWidgetItem(str(i.paid)))
                self.ui.tableWidget.setItem(count, 7, QtWidgets.QTableWidgetItem(str(i.groupid)))
                count += 1
                
        elif self.ui.comboBox.currentText() == "Приказы":
            self.ui.lineEdit_2.setVisible(True)
            self.ui.lineEdit_2.setText("Причина")
            self.ui.comboBox_2.setVisible(True)
            
            if not [self.ui.comboBox_2.itemText(i) for i in range(self.ui.comboBox_2.count())]: 
                data = ["<--Не выбран-->", "Зачисление", "Перевод", "Отчисление"]
                self.ui.comboBox_2.addItems(data)
            
            self.ui.lineEdit_3.setVisible(False)
            self.ui.comboBox_3.setVisible(False) 
            
            with db:
                if self.ui.comboBox_2.currentText() != "<--Не выбран-->":
                    reports = Report.select().where(Report.reason == str(self.ui.comboBox_2.currentText()))
                
                else:
                    reports = Report.select()
                
            column_list = ["id", "lname", "diplom", "rep_date", "reason"]
            
            self.ui.tableWidget.setColumnCount(len(column_list))
            self.ui.tableWidget.setRowCount(reports.count())
            self.ui.tableWidget.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in reports:
                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.lname)))
                self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.rep_date)))
                self.ui.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.reason)))
                count += 1
                
        elif self.ui.comboBox.currentText() == "Архив":
            
            self.ui.lineEdit_2.setVisible(True)
            self.ui.lineEdit_2.setText("Специальность")
            self.ui.comboBox_2.setVisible(True)
            
            if not [self.ui.comboBox_2.itemText(i) for i in range(self.ui.comboBox_2.count())]: 
                data = ["<--Не выбран-->"]
                with db:
                    temp = Spec.select()
                    
                for i in temp:
                    data.append(i.name)    
                self.ui.comboBox_2.addItems(data)
            
            self.ui.lineEdit_3.setVisible(True)
            self.ui.lineEdit_3.setText("Причина")
            self.ui.comboBox_3.setVisible(True) 
            if not [self.ui.comboBox_3.itemText(i) for i in range(self.ui.comboBox_3.count())]: 
                self.ui.comboBox_3.addItems(["<--Не выбран-->", "Отчисление", "Академ. отпуск", "Перевод"])
            
            with db:
                if self.ui.comboBox_2.currentText() != "<--Не выбран-->" and \
                    self.ui.comboBox_3.currentText() != "<--Не выбран-->":
                    archives = Archive.select().where(
                        Archive.specName == str(self.ui.comboBox_2.currentText()),
                        Archive.reason == self.ui.comboBox_3.currentText()
                    )
                
                elif self.ui.comboBox_2.currentText() != "<--Не выбран-->":
                    archives = Archive.select().where(Archive.specName == str(self.ui.comboBox_2.currentText()))
                
                elif self.ui.comboBox_3.currentText() != "<--Не выбран-->":
                    archives = Archive.select().where(Archive.reason == self.ui.comboBox_3.currentText())
                 
                else:
                    archives = Archive.select()
                
            column_list = ["id", "diplom", "name", "enrollment", "expulsion",
                           "course", "specName", "reason"]
            
            self.ui.tableWidget.setColumnCount(len(column_list))
            self.ui.tableWidget.setRowCount(archives.count())
            self.ui.tableWidget.setHorizontalHeaderLabels(
                column_list
            )
            
            count = 0
            for i in archives:
                self.ui.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i.id)))
                self.ui.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(i.diplom)))
                self.ui.tableWidget.setItem(count, 2, QtWidgets.QTableWidgetItem(str(i.name)))
                self.ui.tableWidget.setItem(count, 3, QtWidgets.QTableWidgetItem(str(i.enrollment)))
                self.ui.tableWidget.setItem(count, 4, QtWidgets.QTableWidgetItem(str(i.expulsion)))
                self.ui.tableWidget.setItem(count, 5, QtWidgets.QTableWidgetItem(str(i.course)))
                self.ui.tableWidget.setItem(count, 6, QtWidgets.QTableWidgetItem(str(i.specName)))
                self.ui.tableWidget.setItem(count, 7, QtWidgets.QTableWidgetItem(str(i.reason)))
                count += 1