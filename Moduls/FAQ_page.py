from PySide6 import QtCore, QtGui, QtWidgets

from Moduls.models import *

class FAQPage(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = parent
        
        self.initilize()
                
                
    def change_func(self, item, column):
        
            if item.text(column) in ["1. Введение", "1.1 Общее"]:
                with open(r"\LR BD new\FAQ\Introduction\article_1.html", encoding="UTF-8") as f:
                    page = f.read()
                
                self.ui.textBrowser.document().setHtml(page)
                
            # elif item.text(column) == "title 1":
            #     with open(r"\LR BD new\FAQ\title 2\page.html") as f:
            #         page = f.read()
                
            #     self.ui.textBrowser.document().setHtml(page)
        
            # else:
            #     with open(r"\LR BD new\FAQ\Introduction\article_1.html", encoding="UTF-8") as f:
            #         page = f.read()
                
            #     self.ui.textBrowser.document().setHtml(page)
            print(column, item.text(column))
            
            
    def initilize(self):
        with open(r"\LR BD new\FAQ\Introduction\article_1.html", encoding="UTF-8") as f:
                page = f.read()
                self.ui.textBrowser.document().setHtml(page)
        
        self.ui.treeWidget.setColumnCount(1)
        self.ui.treeWidget.setHeaderLabels(["Содержание"])
        self.ui.treeWidget.itemClicked.connect(self.change_func)

        titles = ["1. Введение", "2. Просмотр", "3. Редактирование",
                 "4. Отчёты", "5. Электронная среда", "6. Статистика",
                 "7. Настройки", "8. Уровни доступа"]
        
        sub_titles = {
            "1. Введение": ["1.1 Общее"],
            "2. Просмотр":["2.1 Общее", "2.2 Просмотр таблиц"],
            "3. Редактирование": ["3.1 Общее", "3.2 Редактирование таблиц"],
            "4. Отчёты": ["4.1 Общее", "4.2 Создание отчётов", "4.3 Авто отчёты", "4.4 Дополнительные функции"],
            "5. Электронная среда": ["5.1 Общее", "5.2 Инструкция"],
            "6. Статистика": ["6.1 Общее", "6.2 Просмотр статистики", "6.3 Показ графиков"],
            "7. Настройки": ["7.1 Общее", "7.2 Инструкция"],
            "8. Уровни доступа": ["8.1 Общее", "8.2 Создание профиля"]
        }
        
        for title in titles:
            preview = QtWidgets.QTreeWidgetItem(self.ui.treeWidget) 
            self.ui.treeWidget.addTopLevelItem(preview)
            preview.setText(0, title)
            
            for sub_title in sub_titles[title]:
                title = QtWidgets.QTreeWidgetItem()
                preview.addChild(title)
                title.setText(0, sub_title)