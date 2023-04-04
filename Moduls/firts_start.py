from PySide6 import QtCore, QtGui, QtWidgets


class FirtsInitialize(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = parent
        
        
        self.setup_icon()
        self.setup_combobox()
        self.set_tool_tips()
        self.set_visible()
        
    
    def set_visible(self):
        self.ui.lineEdit_2.setVisible(False)
        self.ui.comboBox_2.setVisible(False)
        
        self.ui.lineEdit_3.setVisible(False)
        self.ui.comboBox_3.setVisible(False)    
        
        self.ui.lineEdit_8.setVisible(False)
        self.ui.comboBox_8.setVisible(False)
        
        self.ui.lineEdit_9.setVisible(False)
        self.ui.comboBox_9.setVisible(False)  
        
        
    
    def setup_icon(self):
        self.ui.pushButton.setIcon(QtGui.QIcon(r'Icons\full_info_icon.png'))
        self.ui.pushButton_2.setIcon(QtGui.QIcon(r'Icons\find_icon.png'))
        
        
        self.ui.pushButton_12.setIcon(QtGui.QIcon(r'Icons\add_icon.png'))
        self.ui.pushButton_13.setIcon(QtGui.QIcon(r'Icons\replace_icon.png'))
        self.ui.pushButton_14.setIcon(QtGui.QIcon(r'Icons\delete_icon.png'))
        self.ui.pushButton_5.setIcon(QtGui.QIcon(r'Icons\full_info_icon.png'))
        self.ui.pushButton_6.setIcon(QtGui.QIcon(r'Icons\find_icon.png'))
        self.ui.pushButton_7.setIcon(QtGui.QIcon(r'Icons\add_icon.png'))
        self.ui.pushButton_8.setIcon(QtGui.QIcon(r'Icons\replace_icon.png'))
        self.ui.pushButton_9.setIcon(QtGui.QIcon(r'Icons\delete_icon.png'))
    
    
    def setup_combobox(self):
        self.ui.comboBox.addItems(["<--Не выбрана-->", "Специальности", "Группы",
                                   "Студенты", "Приказы", "Архив",
                                   "Преподаватели", "Дисциплины", "Загрузка преподавателей",
                                   "Учебный график", "Сессионная ведомость",
                                   "Квалификационный экзамен", "Сессия квалификационный экзамен"])
        self.ui.comboBox_7.addItems(["<--Не выбрана-->", "Специальности", "Группы",
                                     "Студенты", "Приказы", "Архив",
                                     "Преподаватели", "Дисциплины", "Загрузка преподавателей",
                                     "Учебный график", "Сессионная ведомость",
                                     "Квалификационный экзамен", "Сессия квалификационный экзамен"])
        
        
    def set_tool_tips(self):
        self.ui.pushButton.setToolTip("Более подробная информация")
        self.ui.pushButton.setToolTipDuration(-1)
        self.ui.pushButton_5.setToolTip("Более подробная информация")
        self.ui.pushButton_5.setToolTipDuration(-1)
        
        self.ui.pushButton_2.setToolTip("Поиск")
        self.ui.pushButton_2.setToolTipDuration(-1)
        self.ui.pushButton_6.setToolTip("Поиск")
        self.ui.pushButton_6.setToolTipDuration(-1)
        
        self.ui.pushButton_7.setToolTip("Добавить запись")
        self.ui.pushButton_7.setToolTipDuration(-1)
        
        self.ui.pushButton_8.setToolTip("Применить изменение")
        self.ui.pushButton_8.setToolTipDuration(-1)
        
        self.ui.pushButton_9.setToolTip("Удалить запись")
        self.ui.pushButton_9.setToolTipDuration(-1)