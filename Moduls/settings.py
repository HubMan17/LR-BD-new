import os
from datetime import datetime
import shutil
from PySide6 import QtCore, QtGui, QtWidgets

from Moduls.work_ini import *
    
class Settig(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = parent
        
        self.config = configparser.ConfigParser()
        self.config.read(r"\LR BD new\Settings\default_settigs.ini")
        
        # self.setup_start_settigs()
        self.create_backup()
        self.initialize()
        
        
    def initialize(self):
        self.ui.lineEdit_40.setText(self.config["links"]["save_link"])
        self.ui.lineEdit_42.setText(self.config["db"]["db_link"])
        self.ui.lineEdit_44.setText(self.config["db"]["backup_db"])
        # self.ui.lineEdit_46.setText(self.config["links"]["save_link"])
        
        self.ui.lineEdit_54.setText(self.config["posts"]["send_email"])
        self.ui.lineEdit_49.setText(self.config["posts"]["send_pass"])
        self.ui.lineEdit_51.setText(self.config["posts"]["token"])
        self.ui.lineEdit_53.setText(self.config["posts"]["to_email"])
        
    
    def create_backup(self):
        now_date = datetime.now().day
        
        if os.path.exists(r"\LR BD new\Backup"):
            pass
        else:
            os.mkdir(r"\LR BD new\Backup")
            
        check_data = get_backup_data()
        if now_date != check_data:
            shutil.copy2(get_db_link(), get_backup_folder())
            
            self.config["db"]["date_backup"] = str(now_date)
            
            with open(r"\LR BD new\Settings\default_settigs.ini", 'w') as configfile:
                self.config.write(configfile)
            
            
    def setup_start_settigs(self):
        
        if os.path.exists(r"C:/Документы/LR BD") or \
            os.path.exists(r"D:/Документы/LR BD"):
            pass
        
        else:
            # D:\Администратор\Documents\
            try:
              os.mkdir(r"C:\Администратор\Документы\LR BD")
            except:
              os.mkdir(r"D:/Администратор/Документы/LR BD")
            # try:
            #   os.mkdir(r"C:/Документы/LR BD")
            # except:
            #   os.mkdir(r"D:/Документы/LR BD")
            