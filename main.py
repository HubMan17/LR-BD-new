from PySide6 import QtCore, QtGui, QtWidgets
import sys
import os
from matplotlib import pyplot as plt
from datetime import datetime
from UI.ui import Ui_Form

from Moduls.auth import *
from Moduls.firts_start import *
from Moduls.show_page1 import *
from Moduls.change_page2 import *
from Moduls.create_start_db import create_start_db
from Moduls.settings import Settig
from Moduls.stats_page import StatPage
from Moduls.FAQ_page import FAQPage


prisds

class ui_Interface(QtWidgets.QWidget, Ui_Form):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.page0 = Auth(self)
        self.page1 = ShowPage1(self)
        self.page2 = ChangePage2(self)
        self.page4 = Settig(self)
        self.page5 = StatPage(self)
        self.pageFAQ = FAQPage(self)
        
        self.page4
        self.page5
        
        self.first_start()
        self.auth()


        
        # self.textBrowser.document().setHtml(r"""My image :<br /><img src="pngwing.png"/>""")

        
        

        # self.mytext.moveCursor(QtGui.QTextCursor.End)
        # self.textEdit.setText(self.textEdit.toPlainText() + "{datetime.now()} start2\n")
        
        self.tabWidget.connect(QtCore.SIGNAL("currentChanged(int)"), self.select_page)
    
    
    
    
    def auth(self):
        self.page0
    

    def select_page(self):
        if self.tabWidget.currentWidget().objectName() == "view":
            
            self.view_page1()
        
        elif self.tabWidget.currentWidget().objectName() == "change":
            
            self.change_page2()
            
        elif self.tabWidget.currentWidget().objectName() == "stats":
            
            self.page5
                

    def first_start(self):
        self.tabWidget.setTabEnabled(2, True) # view tables
        self.tabWidget.setTabEnabled(3, True) # change tables
        self.tabWidget.setTabEnabled(4, False)
        self.tabWidget.setTabEnabled(5, False) # !!!!!!!!!!!
        self.tabWidget.setTabEnabled(6, False)
        self.tabWidget.setTabEnabled(7, False)
        self.textEdit.setText(f"{datetime.datetime.now()}\tСтарт программы. Начало логирования\n")
        FirtsInitialize(self)
        self.textEdit.setText(self.textEdit.toPlainText() + f"{datetime.datetime.now()}\tУспешная инициализация интерфейса!\n")
        
        
    def view_page1(self):
        self.page1

    def change_page2(self):
        self.page2
    
    

def main():
    
    # if "Database.db" not in os.listdir():
    #     create_start_db()
        
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()    
    
    window = ui_Interface()
    # window.showMaximized()
    window.show()
    app.exec_()
    

if __name__ == "__main__":
    main()
