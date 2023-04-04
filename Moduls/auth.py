import pickle
import configparser
from datetime import datetime
from PySide6 import QtCore, QtGui, QtWidgets


import UI.auth_ui


class Auth(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = parent
        
        self.ui.tabWidget.connect(QtCore.SIGNAL("currentChanged(int)"), self.select_page)
        self.ui.pushButton_3.clicked.connect(self.cheak)
        
        self.ui.pushButton_12.clicked.connect(self.append_file)
        self.ui.pushButton_13.clicked.connect(self.change_file)
        self.ui.pushButton_14.clicked.connect(self.delete_file)
        
    
    def show_table(self):
        data = self.open_file()
        
        self.ui.tableWidget_2.setColumnCount(3)
        self.ui.tableWidget_2.setRowCount(len(data)-1)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(
                ["Логин", "Пароль", "Статус"]
        )
            
        count = 0
        for i in data:
            
            if i == "DEFAULT":
                continue
            
            self.ui.tableWidget_2.setItem(count, 0, QtWidgets.QTableWidgetItem(str(i)))
            self.ui.tableWidget_2.setItem(count, 1, QtWidgets.QTableWidgetItem(str(data[i]["password"])))
            self.ui.tableWidget_2.setItem(count, 2, QtWidgets.QTableWidgetItem(str(data[i]["status"])))
            count += 1    
    
        
    def select_page(self):
        if self.ui.tabWidget.currentWidget().objectName() == "admin":
            self.show_table()
        
        
    def cheak(self):
        login = self.ui.lineEdit_12.text()
        password = self.ui.lineEdit_13.text()
        
        config = self.open_file()
        
        data = []
        for i in config:
            data.append(i)
        
        if login in data:
            
            if password == config[login]["password"]:
                
                self.ui.lineEdit_15.setText(config[login]["status"])
                self.ui.tabWidget.setTabEnabled(2, True)
                self.ui.tabWidget.setTabEnabled(3, True)
                
                if config[login]["status"] == "Owner":
                    self.ui.tabWidget.setTabEnabled(4, True)
                    self.ui.tabWidget.setTabEnabled(5, True)
                    self.ui.tabWidget.setTabEnabled(6, True)
                    self.ui.tabWidget.setTabEnabled(7, True)
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.now()}\tВы имеете доступ Owner!\n")
                
                elif config[login]["status"] == "Full":
                    self.ui.tabWidget.setTabEnabled(4, False)
                    self.ui.tabWidget.setTabEnabled(5, True)
                    self.ui.tabWidget.setTabEnabled(6, True)
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.now()}\tВы имеете полный Full!\n")
                    
                elif config[login]["status"] == "Limited":
                    self.ui.tabWidget.setTabEnabled(3, False)
                    self.ui.tabWidget.setTabEnabled(4, False)
                    self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.now()}\tВы имеете ограниченный Limited!\n")
    
            else:
                self.ui.tabWidget.setTabEnabled(2, False)
                self.ui.tabWidget.setTabEnabled(3, False)
                self.ui.tabWidget.setTabEnabled(4, False)
                self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.now()}\tОшибка доступа! Неверный логин или пароль\n")
        
        else:
            self.ui.tabWidget.setTabEnabled(2, False)
            self.ui.tabWidget.setTabEnabled(3, False)
            self.ui.tabWidget.setTabEnabled(4, False)
            self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.now()}\tОшибка доступа! Неверный логин или пароль\n")
        
        
        login = self.ui.lineEdit_12.setText("")
        password = self.ui.lineEdit_13.setText("")
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
        
        
    def open_file(self):
        config = configparser.ConfigParser()  # создаём объекта парсера
        config.read(r"\LR-BD-new\Settings\user_db.ini")
        return config
    
    
    def delete_section(self, key):
        config = configparser.ConfigParser()  # создаём объекта парсера
        with open(r"\LR-BD-new\Settings\user_db.ini", 'r+') as s:
            config.read_file(s)  # File position changed (it's at the end of the file)
            config.remove_section(key)
            s.seek(0)  # <-- Change the file position to the beginning of the file
            config.write(s)
            s.truncate()
    
    
    def write_file(self, data):
        with open(r"\LR-BD-new\Settings\user_db.ini", 'a') as f:
            f.writelines(data)
            
            
    def change_data(self, data):
        with open(r"\LR-BD-new\Settings\user_db.ini", 'w') as configfile:
            data.write(configfile)
            
    
    def append_file(self):
        def bp():
            login = self.ui_add.lineEdit_2.text()
            password = self.ui_add.lineEdit_4.text()
            status = self.ui_add.comboBox.currentText()
            
            data = f"\n[{login}]\npassword = {password}\nstatus = {status}\n"
            self.write_file(data)
                
            self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.now()}\tНовая запись успешно добавлена!\n")
            self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
            
            self.add_data_window.close()
            self.show_table()
            
        self.add_data_window = QtWidgets.QWidget()
        self.ui_add = UI.auth_ui.Ui_Form()
        self.ui_add.setupUi(self.add_data_window)
        self.add_data_window.show() 
        
        self.ui_add.comboBox.addItems(["<--Не выбрано-->", "Owner", "Full", "Limited"])
        self.ui_add.pushButton.clicked.connect(bp)
    
    
    def change_file(self):
        key = self.ui.tableWidget_2.item(self.ui.tableWidget_2.currentRow(), 0).text()
        id_change_data = self.ui.tableWidget_2.currentColumn()
        new_data = self.ui.tableWidget_2.item(self.ui.tableWidget_2.currentRow(), id_change_data).text()
        
        data = self.open_file()
        
        if id_change_data == 1:
            data[key]["password"] = new_data
        
        elif id_change_data == 2:
            data[key]["status"] = new_data.capitalize()
            
        self.change_data(data)
            
        self.show_table()
        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.now()}\tДанные успешно изменены!\n")
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)
        
    
    def delete_file(self):
        key = self.ui.tableWidget_2.item(self.ui.tableWidget_2.currentRow(), 0).text()
        
        self.delete_section(key=key)
        
        self.show_table()
        self.ui.textEdit.setText(self.ui.textEdit.toPlainText() + f"{datetime.now()}\tЗапись успешно удалена!\n")
        self.ui.textEdit.moveCursor(QtGui.QTextCursor.End)