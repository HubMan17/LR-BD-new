from PySide6 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt

from Moduls.models import *

class StatPage(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = parent
        
        self.initialize()
        
        self.ui.pushButton_35.clicked.connect(self.income)
        self.ui.pushButton_36.clicked.connect(self.stats_specs)
        self.ui.pushButton_37.clicked.connect(self.stats_groups)
    
    
    def initialize(self):
        """Инициализация разделов статистики"""
        self.initialize_income()
        self.initialize_specs()
        self.initialize_groups()
        
        
    def initialize_groups(self): 
        """раздел статистика групп"""
        
        
        # all students count
        respond = Student.select()
        student_count = respond.count()
        
        # title: Group name        
        respond = Group.select()
        titles = [i.name for i in respond]
    
        # values: Group count student
        values = []
        respond = Student.select(Student.id).join(Group)
        
        for i in titles:
            values.append(respond.where(Group.name == i).count())
        
        # create fields
        vbox = self.ui.formLayout_10
        
        if not vbox.rowCount():
        
            field_title = QtWidgets.QLineEdit() # create field - all stud
            field_title.setText("Всего студентов")
            field_title.setReadOnly(True)
            field_title.setMinimumWidth(250)
            field_title.setMaximumWidth(250)
            field_title.setMinimumHeight(35)
                
            field_value = QtWidgets.QLineEdit()
            field_value.setText(str(student_count) + " чел.")
            field_value.setReadOnly(True)
            field_value.setMinimumWidth(500)
            field_value.setMaximumWidth(500)
            field_value.setMinimumHeight(35)
            
            vbox.addRow(field_title, field_value)
            
            for i in range(len(titles)):
                
                field_title = QtWidgets.QLineEdit()
                field_title.setText(titles[i])
                field_title.setReadOnly(True)
                field_title.setMinimumWidth(250)
                field_title.setMaximumWidth(250)
                field_title.setMinimumHeight(35)
            
                field_value = QtWidgets.QLineEdit()
                field_value.setText(str(values[i]) + " чел.")
                field_value.setReadOnly(True)
                field_value.setMinimumWidth(500)
                field_value.setMaximumWidth(500)
                field_value.setMinimumHeight(35)
                
                vbox.addRow(field_title, field_value)

        return [titles, values]
        
    
    def stats_groups(self):
        
        data = self.initialize_groups()
        
        titles = data[0]
        values = data[1]
        if self.ui.checkBox_6.isChecked():
            
            plt.bar(titles, values)
            plt.show()
            
        if self.ui.checkBox_7   .isChecked():
            fig, ax = plt.subplots()
            ax.pie(values, labels=titles, autopct='%1.1f%%')
            plt.show()
        
        
    def initialize_specs(self): 
        """раздел статистика специальностей"""
        
        
        # all students count
        respond = Student.select()
        student_count = respond.count()
        
        # title: specs name        
        respond = Spec.select(Spec.name)
        titles = [i.name for i in respond]
    
        # values: specs count student
        spec_count_studs = []
        respond = Student.select(Student.id).join(Group).join(Spec)
        
        for i in titles:
            spec_count_studs.append(respond.where(Spec.name == i).count())
        
        # create fields
        vbox = self.ui.formLayout_8
        
        if not vbox.rowCount():
        
            field_title = QtWidgets.QLineEdit() # create field - all stud
            field_title.setText("Всего студентов")
            field_title.setReadOnly(True)
            field_title.setMinimumWidth(250)
            field_title.setMaximumWidth(250)
            field_title.setMinimumHeight(35)
                
            field_value = QtWidgets.QLineEdit()
            field_value.setText(str(student_count) + " чел.")
            field_value.setReadOnly(True)
            field_value.setMinimumWidth(500)
            field_value.setMaximumWidth(500)
            field_value.setMinimumHeight(35)
            
            vbox.addRow(field_title, field_value)
            
            for i in range(len(titles)):
                
                field_title = QtWidgets.QLineEdit()
                field_title.setText(titles[i])
                field_title.setReadOnly(True)
                field_title.setMinimumWidth(250)
                field_title.setMaximumWidth(250)
                field_title.setMinimumHeight(35)
            
                field_value = QtWidgets.QLineEdit()
                field_value.setText(str(spec_count_studs[i]) + " чел.")
                field_value.setReadOnly(True)
                field_value.setMinimumWidth(500)
                field_value.setMaximumWidth(500)
                field_value.setMinimumHeight(35)
                
                vbox.addRow(field_title, field_value)

        return [titles, spec_count_studs]
        
    
    def stats_specs(self):
        
        data = self.initialize_specs()
        
        titles = data[0]
        spec_count_studs = data[1]
        if self.ui.checkBox_4.isChecked():
            
            plt.bar(titles, spec_count_studs)
            plt.show()
            
        if self.ui.checkBox_5.isChecked():
            fig, ax = plt.subplots()
            ax.pie(spec_count_studs, labels=titles, autopct='%1.1f%%')
            plt.show()
    
    
    def initialize_income(self):
        
        """раздел доходы"""
        # self.ui.lineEdit_55.setText("Планируемые")
        # self.ui.lineEdit_56.setText("Полученные")
        # self.ui.lineEdit_58.setText("Ожидаются")
        
        # planned income
        all_money = 0
        respond = Spec.select()
        
        for i in respond:
            count = Student.select().join(Group).join(Spec).where(
                Spec.id == i.id
                ).count()
            
            price = i.price
            
            all_money += count*price
        
        self.ui.lineEdit_62.setText(f"{str(all_money)} руб.")
        
        # get money
        get_money = 0
        respond = Student.select()
        
        for i in respond:
            get_money += i.paid
        
        self.ui.lineEdit_57.setText(f"{str(get_money)} руб.")
        
        # weit money
        wait_money = all_money - get_money
        self.ui.lineEdit_59.setText(f"{str(wait_money)} руб.")
        
        return [all_money, get_money, wait_money]
        
    
    def income(self):
        
        data = self.initialize_income()
        
        if self.ui.checkBox_2.isChecked():
            groups = ["Полученные", "Ожидаются"]
            counts = [data[1], data[2]]
            plt.bar(groups, counts)
            plt.show()
            
        if self.ui.checkBox_3.isChecked():
            groups = ["Полученные", "Ожидаются"]
            counts = [data[1], data[2]]
            fig, ax = plt.subplots()
            ax.pie(counts, labels=groups, autopct='%1.1f%%')
            plt.show()
            