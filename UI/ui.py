# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QGroupBox, QHeaderView, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1546, 843)
        Form.setStyleSheet(u"QGroupBox {\n"
"	border-color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 248, 219);\n"
"	\n"
"	gridline-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(-2, 0, 1511, 681))
        self.tabWidget.setStyleSheet(u"")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 103, 61, 461))
        self.groupBox_3.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox_3.setStyleSheet(u"groupBox {\n"
"	\n"
"	background-color: rgb(171, 166, 115);\n"
"}")
        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(-3, -7, 1360, 111))
        self.lineEdit_6 = QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(120, 30, 211, 51))
        font = QFont()
        font.setPointSize(24)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_6.setCursorPosition(10)
        self.lineEdit_6.setReadOnly(True)
        self.textEdit_2 = QTextEdit(self.tab)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(0, 580, 1360, 111))
        font1 = QFont()
        font1.setPointSize(12)
        self.textEdit_2.setFont(font1)
        self.textEdit_2.setReadOnly(True)
        self.groupBox_7 = QGroupBox(self.tab)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(57, 103, 1300, 461))
        self.lineEdit_11 = QLineEdit(self.groupBox_7)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(90, 80, 121, 41))
        font2 = QFont()
        font2.setPointSize(18)
        self.lineEdit_11.setFont(font2)
        self.lineEdit_11.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_11.setCursorPosition(5)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_12 = QLineEdit(self.groupBox_7)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(230, 80, 261, 41))
        self.lineEdit_12.setFont(font2)
        self.lineEdit_12.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_12.setCursorPosition(0)
        self.lineEdit_12.setReadOnly(False)
        self.lineEdit_13 = QLineEdit(self.groupBox_7)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(230, 150, 261, 41))
        self.lineEdit_13.setFont(font2)
        self.lineEdit_13.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_13.setEchoMode(QLineEdit.NoEcho)
        self.lineEdit_13.setCursorPosition(0)
        self.lineEdit_13.setReadOnly(False)
        self.lineEdit_14 = QLineEdit(self.groupBox_7)
        self.lineEdit_14.setObjectName(u"lineEdit_14")
        self.lineEdit_14.setGeometry(QRect(90, 150, 121, 41))
        self.lineEdit_14.setFont(font2)
        self.lineEdit_14.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_14.setCursorPosition(6)
        self.lineEdit_14.setReadOnly(True)
        self.pushButton_3 = QPushButton(self.groupBox_7)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(240, 240, 231, 61))
        font3 = QFont()
        font3.setFamilies([u"Amazon Ember"])
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 22px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.lineEdit_15 = QLineEdit(self.groupBox_7)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setGeometry(QRect(970, 90, 241, 51))
        self.lineEdit_15.setFont(font2)
        self.lineEdit_15.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_15.setCursorPosition(0)
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_16 = QLineEdit(self.groupBox_7)
        self.lineEdit_16.setObjectName(u"lineEdit_16")
        self.lineEdit_16.setGeometry(QRect(840, 90, 111, 51))
        self.lineEdit_16.setFont(font2)
        self.lineEdit_16.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_16.setCursorPosition(6)
        self.lineEdit_16.setReadOnly(True)
        self.checkBox = QCheckBox(self.groupBox_7)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(350, 200, 141, 21))
        self.checkBox.setFont(font1)
        self.checkBox.setStyleSheet(u"")
        self.tabWidget.addTab(self.tab, "")
        self.groupBox_4.raise_()
        self.textEdit_2.raise_()
        self.groupBox_3.raise_()
        self.groupBox_7.raise_()
        self.view = QWidget()
        self.view.setObjectName(u"view")
        self.view.setStyleSheet(u"tab {\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.tableWidget = QTableWidget(self.view)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(59, 110, 1300, 431))
        self.tableWidget.setStyleSheet(u"")
        self.tableWidget.setSortingEnabled(False)
        self.groupBox = QGroupBox(self.view)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 110, 61, 461))
        self.groupBox.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox.setStyleSheet(u"groupBox {\n"
"	\n"
"	background-color: rgb(171, 166, 115);\n"
"}")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 41, 41))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 70, 41, 41))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.groupBox_2 = QGroupBox(self.view)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 0, 1360, 111))
        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(11, 35, 101, 30))
        font4 = QFont()
        font4.setPointSize(11)
        self.lineEdit.setFont(font4)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit.setReadOnly(True)
        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 40, 191, 22))
        self.comboBox.setStyleSheet(u"")
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setModelColumn(0)
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(517, 34, 191, 22))
        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(400, 30, 101, 30))
        font5 = QFont()
        font5.setPointSize(10)
        self.lineEdit_2.setFont(font5)
        self.lineEdit_2.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(820, 30, 120, 30))
        self.lineEdit_3.setFont(font5)
        self.lineEdit_3.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_3.setReadOnly(True)
        self.comboBox_3 = QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(950, 34, 191, 22))
        self.lineEdit_4 = QLineEdit(self.view)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(60, 540, 1300, 22))
        self.tabWidget.addTab(self.view, "")
        self.change = QWidget()
        self.change.setObjectName(u"change")
        self.change.setStyleSheet(u"QPushButton {\n"
"	height: 50px;\n"
" 	 width: 50px;\n"
"}")
        self.tableWidget_3 = QTableWidget(self.change)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(59, 110, 1300, 430))
        self.groupBox_5 = QGroupBox(self.change)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(0, 110, 61, 461))
        self.groupBox_5.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox_5.setStyleSheet(u"groupBox {\n"
"	\n"
"	background-color: rgb(171, 166, 115);\n"
"}")
        self.pushButton_5 = QPushButton(self.groupBox_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 20, 41, 41))
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.pushButton_6 = QPushButton(self.groupBox_5)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 70, 41, 41))
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.pushButton_7 = QPushButton(self.groupBox_5)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 120, 41, 41))
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.pushButton_8 = QPushButton(self.groupBox_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(10, 170, 41, 41))
        self.pushButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.pushButton_9 = QPushButton(self.groupBox_5)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 220, 41, 41))
        self.pushButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.groupBox_6 = QGroupBox(self.change)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(0, 0, 1360, 111))
        self.lineEdit_7 = QLineEdit(self.groupBox_6)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(10, 36, 101, 30))
        self.lineEdit_7.setFont(font4)
        self.lineEdit_7.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_7.setReadOnly(True)
        self.comboBox_7 = QComboBox(self.groupBox_6)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(120, 40, 191, 22))
        self.comboBox_7.setStyleSheet(u"")
        self.comboBox_8 = QComboBox(self.groupBox_6)
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(510, 30, 191, 22))
        self.lineEdit_8 = QLineEdit(self.groupBox_6)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(350, 26, 150, 30))
        self.lineEdit_8.setFont(font5)
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_9 = QLineEdit(self.groupBox_6)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(350, 66, 150, 30))
        self.lineEdit_9.setFont(font5)
        self.lineEdit_9.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_9.setReadOnly(True)
        self.comboBox_9 = QComboBox(self.groupBox_6)
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(510, 70, 191, 22))
        self.comboBox_10 = QComboBox(self.groupBox_6)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setGeometry(QRect(1100, 20, 241, 22))
        self.lineEdit_10 = QLineEdit(self.groupBox_6)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setGeometry(QRect(1010, 16, 80, 30))
        self.lineEdit_10.setFont(font5)
        self.lineEdit_10.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_10.setReadOnly(True)
        self.pushButton_10 = QPushButton(self.groupBox_6)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(1180, 60, 151, 31))
        self.pushButton_10.setFont(font3)
        self.pushButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 13px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.comboBox_11 = QComboBox(self.groupBox_6)
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setGeometry(QRect(880, 70, 191, 22))
        self.comboBox_11.setEditable(True)
        self.comboBox_11.setInsertPolicy(QComboBox.InsertAtBottom)
        self.lineEdit_17 = QLineEdit(self.groupBox_6)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setGeometry(QRect(720, 66, 150, 30))
        self.lineEdit_17.setFont(font5)
        self.lineEdit_17.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_5 = QLineEdit(self.change)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(60, 540, 1300, 22))
        self.tabWidget.addTab(self.change, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.webEngineView = QWebEngineView(self.tab_2)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(0, 0, 1361, 671))
        self.webEngineView.setUrl(QUrl(u"https://eios.kesip.ru/"))
        self.webEngineView.setZoomFactor(1.000000000000000)
        self.tabWidget.addTab(self.tab_2, "")
        self.stats = QWidget()
        self.stats.setObjectName(u"stats")
        self.groupBox_11 = QGroupBox(self.stats)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(-1, 110, 61, 461))
        self.groupBox_11.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox_11.setStyleSheet(u"groupBox {\n"
"	\n"
"	background-color: rgb(171, 166, 115);\n"
"}")
        self.groupBox_12 = QGroupBox(self.stats)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(-4, 0, 1360, 111))
        self.lineEdit_71 = QLineEdit(self.groupBox_12)
        self.lineEdit_71.setObjectName(u"lineEdit_71")
        self.lineEdit_71.setGeometry(QRect(100, 30, 181, 51))
        font6 = QFont()
        font6.setPointSize(20)
        self.lineEdit_71.setFont(font6)
        self.lineEdit_71.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_71.setReadOnly(True)
        self.scrollArea_2 = QScrollArea(self.stats)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(60, 110, 1241, 451))
        self.scrollArea_2.setStyleSheet(u" QScrollBar:vertical {\n"
"     background: #e1e1e1;\n"
"     border-top-right-radius: 4px;\n"
"     border-bottom-right-radius: 4px;\n"
"     width: 12px;\n"
"     margin: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"    background-color: qlineargradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                    stop: 0 #a1a1a1, stop: 1 #a1a1a1);\n"
"     border-radius: 4px;\n"
"     min-height: 20px;\n"
"     margin: 0px 2px 0px 2px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     background: none;\n"
"     height: 0px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"     background: none;\n"
"     height: 0px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1227, 710))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_23 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_23.setObjectName(u"groupBox_23")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy)
        self.groupBox_23.setMinimumSize(QSize(0, 230))
        self.groupBox_23.setMaximumSize(QSize(16777215, 250))
        self.groupBox_23.setFont(font1)
        self.groupBox_23.setStyleSheet(u"")
        self.groupBox_23.setFlat(True)
        self.formLayout_6 = QFormLayout(self.groupBox_23)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setVerticalSpacing(10)
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_3.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_3.setHorizontalSpacing(6)
        self.formLayout_3.setVerticalSpacing(5)
        self.formLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.lineEdit_55 = QLineEdit(self.groupBox_23)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_55.sizePolicy().hasHeightForWidth())
        self.lineEdit_55.setSizePolicy(sizePolicy1)
        self.lineEdit_55.setMinimumSize(QSize(250, 35))
        self.lineEdit_55.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_55.setBaseSize(QSize(0, 0))
        self.lineEdit_55.setFont(font1)
        self.lineEdit_55.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px; \n"
"  width: 200px;\n"
"  height : 23px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_55.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lineEdit_55)

        self.lineEdit_62 = QLineEdit(self.groupBox_23)
        self.lineEdit_62.setObjectName(u"lineEdit_62")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_62.sizePolicy().hasHeightForWidth())
        self.lineEdit_62.setSizePolicy(sizePolicy2)
        self.lineEdit_62.setMinimumSize(QSize(500, 35))
        self.lineEdit_62.setMaximumSize(QSize(500, 16777215))
        self.lineEdit_62.setFont(font1)
        self.lineEdit_62.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}R")
        self.lineEdit_62.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_62.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_62)

        self.lineEdit_56 = QLineEdit(self.groupBox_23)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setMinimumSize(QSize(250, 35))
        self.lineEdit_56.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_56.setFont(font1)
        self.lineEdit_56.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_56.setReadOnly(True)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lineEdit_56)

        self.lineEdit_57 = QLineEdit(self.groupBox_23)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setMinimumSize(QSize(0, 35))
        self.lineEdit_57.setFont(font1)
        self.lineEdit_57.setReadOnly(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.lineEdit_57)

        self.lineEdit_58 = QLineEdit(self.groupBox_23)
        self.lineEdit_58.setObjectName(u"lineEdit_58")
        self.lineEdit_58.setMinimumSize(QSize(250, 35))
        self.lineEdit_58.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_58.setFont(font1)
        self.lineEdit_58.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_58.setReadOnly(True)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.lineEdit_58)

        self.lineEdit_59 = QLineEdit(self.groupBox_23)
        self.lineEdit_59.setObjectName(u"lineEdit_59")
        self.lineEdit_59.setMinimumSize(QSize(0, 35))
        self.lineEdit_59.setFont(font1)
        self.lineEdit_59.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_59.setReadOnly(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.lineEdit_59)


        self.formLayout_6.setLayout(0, QFormLayout.LabelRole, self.formLayout_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox_23)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy3)
        self.groupBox_10.setFont(font1)
        self.checkBox_2 = QCheckBox(self.groupBox_10)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(20, 40, 111, 20))
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy4)
        self.checkBox_2.setFont(font1)
        self.checkBox_3 = QCheckBox(self.groupBox_10)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(20, 70, 101, 20))
        sizePolicy4.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy4)
        self.checkBox_3.setFont(font1)

        self.gridLayout_2.addWidget(self.groupBox_10, 0, 0, 1, 1)


        self.formLayout_6.setLayout(0, QFormLayout.FieldRole, self.gridLayout_2)

        self.pushButton_35 = QPushButton(self.groupBox_23)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy5)
        self.pushButton_35.setMinimumSize(QSize(0, 35))
        self.pushButton_35.setMaximumSize(QSize(200, 45))
        self.pushButton_35.setFont(font3)
        self.pushButton_35.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 15px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.pushButton_35)


        self.verticalLayout_4.addWidget(self.groupBox_23)

        self.groupBox_24 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_24.setObjectName(u"groupBox_24")
        sizePolicy.setHeightForWidth(self.groupBox_24.sizePolicy().hasHeightForWidth())
        self.groupBox_24.setSizePolicy(sizePolicy)
        self.groupBox_24.setMinimumSize(QSize(0, 230))
        self.groupBox_24.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_24.setFont(font1)
        self.groupBox_24.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px; \n"
"  font: 11pt;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.groupBox_24.setFlat(True)
        self.formLayout_7 = QFormLayout(self.groupBox_24)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setVerticalSpacing(10)
        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_8.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_8.setHorizontalSpacing(6)
        self.formLayout_8.setVerticalSpacing(20)
        self.formLayout_8.setContentsMargins(-1, 10, -1, -1)

        self.formLayout_7.setLayout(0, QFormLayout.LabelRole, self.formLayout_8)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.groupBox_13 = QGroupBox(self.groupBox_24)
        self.groupBox_13.setObjectName(u"groupBox_13")
        sizePolicy.setHeightForWidth(self.groupBox_13.sizePolicy().hasHeightForWidth())
        self.groupBox_13.setSizePolicy(sizePolicy)
        self.groupBox_13.setMinimumSize(QSize(210, 134))
        self.groupBox_13.setMaximumSize(QSize(210, 134))
        self.groupBox_13.setFont(font1)
        self.checkBox_4 = QCheckBox(self.groupBox_13)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(20, 40, 111, 20))
        sizePolicy4.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy4)
        self.checkBox_4.setFont(font1)
        self.checkBox_5 = QCheckBox(self.groupBox_13)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(20, 70, 101, 20))
        sizePolicy4.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy4)
        self.checkBox_5.setFont(font1)

        self.gridLayout_3.addWidget(self.groupBox_13, 0, 0, 1, 1)


        self.formLayout_7.setLayout(0, QFormLayout.FieldRole, self.gridLayout_3)

        self.pushButton_36 = QPushButton(self.groupBox_24)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy5.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy5)
        self.pushButton_36.setMinimumSize(QSize(0, 35))
        self.pushButton_36.setMaximumSize(QSize(200, 45))
        self.pushButton_36.setFont(font3)
        self.pushButton_36.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 15px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.pushButton_36)


        self.verticalLayout_4.addWidget(self.groupBox_24)

        self.groupBox_25 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_25.setObjectName(u"groupBox_25")
        sizePolicy4.setHeightForWidth(self.groupBox_25.sizePolicy().hasHeightForWidth())
        self.groupBox_25.setSizePolicy(sizePolicy4)
        self.groupBox_25.setMinimumSize(QSize(0, 0))
        self.groupBox_25.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_25.setFont(font1)
        self.groupBox_25.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px; \n"
"  font: 11pt;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.groupBox_25.setFlat(True)
        self.formLayout_9 = QFormLayout(self.groupBox_25)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setVerticalSpacing(10)
        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_10.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_10.setHorizontalSpacing(6)
        self.formLayout_10.setVerticalSpacing(5)
        self.formLayout_10.setContentsMargins(-1, 10, -1, -1)

        self.formLayout_9.setLayout(0, QFormLayout.LabelRole, self.formLayout_10)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.groupBox_14 = QGroupBox(self.groupBox_25)
        self.groupBox_14.setObjectName(u"groupBox_14")
        sizePolicy.setHeightForWidth(self.groupBox_14.sizePolicy().hasHeightForWidth())
        self.groupBox_14.setSizePolicy(sizePolicy)
        self.groupBox_14.setMinimumSize(QSize(210, 134))
        self.groupBox_14.setMaximumSize(QSize(210, 134))
        self.groupBox_14.setFont(font1)
        self.checkBox_6 = QCheckBox(self.groupBox_14)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(20, 40, 111, 20))
        sizePolicy4.setHeightForWidth(self.checkBox_6.sizePolicy().hasHeightForWidth())
        self.checkBox_6.setSizePolicy(sizePolicy4)
        self.checkBox_6.setFont(font1)
        self.checkBox_7 = QCheckBox(self.groupBox_14)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(20, 70, 101, 20))
        sizePolicy4.setHeightForWidth(self.checkBox_7.sizePolicy().hasHeightForWidth())
        self.checkBox_7.setSizePolicy(sizePolicy4)
        self.checkBox_7.setFont(font1)

        self.gridLayout_4.addWidget(self.groupBox_14, 0, 0, 1, 1)


        self.formLayout_9.setLayout(0, QFormLayout.FieldRole, self.gridLayout_4)

        self.pushButton_37 = QPushButton(self.groupBox_25)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy5.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy5)
        self.pushButton_37.setMinimumSize(QSize(0, 35))
        self.pushButton_37.setMaximumSize(QSize(200, 45))
        self.pushButton_37.setFont(font3)
        self.pushButton_37.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 15px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.pushButton_37)


        self.verticalLayout_4.addWidget(self.groupBox_25)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.stats, "")
        self.settigs = QWidget()
        self.settigs.setObjectName(u"settigs")
        self.groupBox_19 = QGroupBox(self.settigs)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setGeometry(QRect(-1, 0, 1359, 111))
        self.lineEdit_38 = QLineEdit(self.groupBox_19)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setGeometry(QRect(80, 30, 181, 51))
        self.lineEdit_38.setFont(font6)
        self.lineEdit_38.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_38.setReadOnly(True)
        self.groupBox_20 = QGroupBox(self.settigs)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setGeometry(QRect(-1, 110, 60, 461))
        self.groupBox_20.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox_20.setStyleSheet(u"groupBox {\n"
"	\n"
"	background-color: rgb(171, 166, 115);\n"
"}")
        self.pushButton_28 = QPushButton(self.groupBox_20)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(10, 20, 41, 41))
        self.pushButton_28.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_28.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.scrollArea = QScrollArea(self.settigs)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(57, 110, 1301, 451))
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"     background: #e1e1e1;\n"
"     border-top-right-radius: 4px;\n"
"     border-bottom-right-radius: 4px;\n"
"     width: 12px;\n"
"     margin: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"    background-color: qlineargradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                    stop: 0 #a1a1a1, stop: 1 #a1a1a1);\n"
"     border-radius: 4px;\n"
"     min-height: 20px;\n"
"     margin: 0px 2px 0px 2px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     background: none;\n"
"     height: 0px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"     background: none;\n"
"     height: 0px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1287, 484))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_21 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_21.setObjectName(u"groupBox_21")
        sizePolicy.setHeightForWidth(self.groupBox_21.sizePolicy().hasHeightForWidth())
        self.groupBox_21.setSizePolicy(sizePolicy)
        self.groupBox_21.setMinimumSize(QSize(0, 230))
        self.groupBox_21.setMaximumSize(QSize(16777215, 250))
        self.groupBox_21.setFont(font1)
        self.groupBox_21.setStyleSheet(u"")
        self.groupBox_21.setFlat(True)
        self.formLayout_4 = QFormLayout(self.groupBox_21)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setVerticalSpacing(10)
        self.pushButton_33 = QPushButton(self.groupBox_21)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy5.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy5)
        self.pushButton_33.setMinimumSize(QSize(0, 35))
        self.pushButton_33.setMaximumSize(QSize(200, 45))
        self.pushButton_33.setFont(font3)
        self.pushButton_33.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 15px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.pushButton_33)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.pushButton_29 = QPushButton(self.groupBox_21)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy1.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy1)
        self.pushButton_29.setMinimumSize(QSize(50, 28))
        self.pushButton_29.setMaximumSize(QSize(105, 16777215))
        self.pushButton_29.setFont(font3)
        self.pushButton_29.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 14px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_29)

        self.pushButton_31 = QPushButton(self.groupBox_21)
        self.pushButton_31.setObjectName(u"pushButton_31")
        sizePolicy1.setHeightForWidth(self.pushButton_31.sizePolicy().hasHeightForWidth())
        self.pushButton_31.setSizePolicy(sizePolicy1)
        self.pushButton_31.setMinimumSize(QSize(50, 28))
        self.pushButton_31.setMaximumSize(QSize(105, 16777215))
        self.pushButton_31.setFont(font3)
        self.pushButton_31.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 14px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_31)

        self.pushButton_30 = QPushButton(self.groupBox_21)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy1.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy1)
        self.pushButton_30.setMinimumSize(QSize(50, 28))
        self.pushButton_30.setMaximumSize(QSize(105, 16777215))
        self.pushButton_30.setFont(font3)
        self.pushButton_30.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 14px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_30)

        self.pushButton_32 = QPushButton(self.groupBox_21)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy1.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy1)
        self.pushButton_32.setMinimumSize(QSize(50, 28))
        self.pushButton_32.setMaximumSize(QSize(105, 16777215))
        self.pushButton_32.setFont(font3)
        self.pushButton_32.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 14px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")

        self.verticalLayout_2.addWidget(self.pushButton_32)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setContentsMargins(-1, 10, -1, -1)
        self.lineEdit_41 = QLineEdit(self.groupBox_21)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lineEdit_41.sizePolicy().hasHeightForWidth())
        self.lineEdit_41.setSizePolicy(sizePolicy1)
        self.lineEdit_41.setMinimumSize(QSize(250, 35))
        self.lineEdit_41.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_41.setBaseSize(QSize(0, 0))
        self.lineEdit_41.setFont(font1)
        self.lineEdit_41.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_41.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lineEdit_41)

        self.lineEdit_39 = QLineEdit(self.groupBox_21)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setMinimumSize(QSize(250, 35))
        self.lineEdit_39.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_39.setFont(font1)
        self.lineEdit_39.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_39.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lineEdit_39)

        self.lineEdit_42 = QLineEdit(self.groupBox_21)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setMinimumSize(QSize(0, 35))
        self.lineEdit_42.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_42)

        self.lineEdit_43 = QLineEdit(self.groupBox_21)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setMinimumSize(QSize(250, 35))
        self.lineEdit_43.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_43.setFont(font1)
        self.lineEdit_43.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_43.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lineEdit_43)

        self.lineEdit_44 = QLineEdit(self.groupBox_21)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setMinimumSize(QSize(0, 35))
        self.lineEdit_44.setFont(font1)
        self.lineEdit_44.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineEdit_44)

        self.lineEdit_45 = QLineEdit(self.groupBox_21)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setMinimumSize(QSize(250, 35))
        self.lineEdit_45.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_45.setFont(font1)
        self.lineEdit_45.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_45.setReadOnly(True)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lineEdit_45)

        self.lineEdit_46 = QLineEdit(self.groupBox_21)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setMinimumSize(QSize(0, 35))
        self.lineEdit_46.setFont(font1)
        self.lineEdit_46.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineEdit_46)

        self.lineEdit_40 = QLineEdit(self.groupBox_21)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        sizePolicy2.setHeightForWidth(self.lineEdit_40.sizePolicy().hasHeightForWidth())
        self.lineEdit_40.setSizePolicy(sizePolicy2)
        self.lineEdit_40.setMinimumSize(QSize(500, 35))
        self.lineEdit_40.setMaximumSize(QSize(500, 16777215))
        self.lineEdit_40.setFont(font1)
        self.lineEdit_40.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}R")
        self.lineEdit_40.setInputMethodHints(Qt.ImhNone)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_40)


        self.formLayout_4.setLayout(0, QFormLayout.LabelRole, self.formLayout)


        self.verticalLayout.addWidget(self.groupBox_21)

        self.groupBox_22 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_22.setObjectName(u"groupBox_22")
        sizePolicy.setHeightForWidth(self.groupBox_22.sizePolicy().hasHeightForWidth())
        self.groupBox_22.setSizePolicy(sizePolicy)
        self.groupBox_22.setMinimumSize(QSize(0, 230))
        self.groupBox_22.setMaximumSize(QSize(16777215, 250))
        self.groupBox_22.setFont(font1)
        self.groupBox_22.setStyleSheet(u"")
        self.groupBox_22.setFlat(True)
        self.formLayout_5 = QFormLayout(self.groupBox_22)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setVerticalSpacing(10)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_2.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout_2.setHorizontalSpacing(6)
        self.formLayout_2.setVerticalSpacing(20)
        self.formLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.lineEdit_47 = QLineEdit(self.groupBox_22)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lineEdit_47.sizePolicy().hasHeightForWidth())
        self.lineEdit_47.setSizePolicy(sizePolicy1)
        self.lineEdit_47.setMinimumSize(QSize(250, 35))
        self.lineEdit_47.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_47.setBaseSize(QSize(0, 0))
        self.lineEdit_47.setFont(font1)
        self.lineEdit_47.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_47.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.lineEdit_47)

        self.lineEdit_54 = QLineEdit(self.groupBox_22)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        sizePolicy2.setHeightForWidth(self.lineEdit_54.sizePolicy().hasHeightForWidth())
        self.lineEdit_54.setSizePolicy(sizePolicy2)
        self.lineEdit_54.setMinimumSize(QSize(500, 35))
        self.lineEdit_54.setMaximumSize(QSize(1000, 16777215))
        self.lineEdit_54.setFont(font1)
        self.lineEdit_54.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_54)

        self.lineEdit_48 = QLineEdit(self.groupBox_22)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        sizePolicy1.setHeightForWidth(self.lineEdit_48.sizePolicy().hasHeightForWidth())
        self.lineEdit_48.setSizePolicy(sizePolicy1)
        self.lineEdit_48.setMinimumSize(QSize(250, 35))
        self.lineEdit_48.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_48.setFont(font1)
        self.lineEdit_48.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_48.setReadOnly(True)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.lineEdit_48)

        self.lineEdit_49 = QLineEdit(self.groupBox_22)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setMinimumSize(QSize(0, 35))
        self.lineEdit_49.setFont(font1)
        self.lineEdit_49.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_49)

        self.lineEdit_50 = QLineEdit(self.groupBox_22)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        sizePolicy1.setHeightForWidth(self.lineEdit_50.sizePolicy().hasHeightForWidth())
        self.lineEdit_50.setSizePolicy(sizePolicy1)
        self.lineEdit_50.setMinimumSize(QSize(250, 35))
        self.lineEdit_50.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_50.setFont(font1)
        self.lineEdit_50.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_50.setReadOnly(True)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.lineEdit_50)

        self.lineEdit_51 = QLineEdit(self.groupBox_22)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setMinimumSize(QSize(0, 35))
        self.lineEdit_51.setFont(font1)
        self.lineEdit_51.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_51)

        self.lineEdit_52 = QLineEdit(self.groupBox_22)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        sizePolicy1.setHeightForWidth(self.lineEdit_52.sizePolicy().hasHeightForWidth())
        self.lineEdit_52.setSizePolicy(sizePolicy1)
        self.lineEdit_52.setMinimumSize(QSize(250, 35))
        self.lineEdit_52.setMaximumSize(QSize(300, 16777215))
        self.lineEdit_52.setFont(font1)
        self.lineEdit_52.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_52.setReadOnly(True)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.lineEdit_52)

        self.lineEdit_53 = QLineEdit(self.groupBox_22)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setMinimumSize(QSize(0, 35))
        self.lineEdit_53.setFont(font1)
        self.lineEdit_53.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_53)


        self.formLayout_5.setLayout(0, QFormLayout.LabelRole, self.formLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, -1)

        self.formLayout_5.setLayout(0, QFormLayout.FieldRole, self.verticalLayout_3)

        self.pushButton_34 = QPushButton(self.groupBox_22)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy5.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy5)
        self.pushButton_34.setMinimumSize(QSize(110, 35))
        self.pushButton_34.setMaximumSize(QSize(200, 45))
        self.pushButton_34.setFont(font3)
        self.pushButton_34.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 15px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.pushButton_34)


        self.verticalLayout.addWidget(self.groupBox_22)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.settigs, "")
        self.admin = QWidget()
        self.admin.setObjectName(u"admin")
        self.lineEdit_20 = QLineEdit(self.admin)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setGeometry(QRect(60, 540, 1300, 22))
        self.groupBox_8 = QGroupBox(self.admin)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(0, 0, 1360, 111))
        self.lineEdit_21 = QLineEdit(self.groupBox_8)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setGeometry(QRect(80, 30, 421, 51))
        self.lineEdit_21.setFont(font6)
        self.lineEdit_21.setStyleSheet(u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}")
        self.lineEdit_21.setReadOnly(True)
        self.groupBox_9 = QGroupBox(self.admin)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(0, 110, 61, 461))
        self.groupBox_9.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox_9.setStyleSheet(u"groupBox {\n"
"	\n"
"	background-color: rgb(171, 166, 115);\n"
"}")
        self.pushButton_12 = QPushButton(self.groupBox_9)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(10, 20, 41, 41))
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.pushButton_13 = QPushButton(self.groupBox_9)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(10, 70, 41, 41))
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.pushButton_14 = QPushButton(self.groupBox_9)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(10, 120, 41, 41))
        self.pushButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}")
        self.tableWidget_2 = QTableWidget(self.admin)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(59, 110, 1300, 431))
        self.tableWidget_2.setStyleSheet(u"")
        self.tableWidget_2.setSortingEnabled(False)
        self.tabWidget.addTab(self.admin, "")
        self.groupBox_8.raise_()
        self.tableWidget_2.raise_()
        self.lineEdit_20.raise_()
        self.groupBox_9.raise_()
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.groupBox_15 = QGroupBox(self.tab_4)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(-1, 110, 221, 561))
        self.groupBox_15.setCursor(QCursor(Qt.ArrowCursor))
        self.groupBox_15.setStyleSheet(u"groupBox {\n"
"	\n"
"	background-color: rgb(171, 166, 115);\n"
"}")
        self.treeWidget = QTreeWidget(self.groupBox_15)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(10, 10, 201, 431))
        self.groupBox_16 = QGroupBox(self.tab_4)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(-4, 0, 1360, 111))
        self.groupBox_17 = QGroupBox(self.tab_4)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(215, 110, 1141, 541))
        self.textBrowser = QTextBrowser(self.groupBox_17)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 10, 1121, 431))
        self.tabWidget.addTab(self.tab_4, "")
        self.groupBox_16.raise_()
        self.groupBox_15.raise_()
        self.groupBox_17.raise_()
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(-2, 585, 1360, 111))
        self.textEdit.setFont(font1)
        self.textEdit.setReadOnly(True)

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(8)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0411\u0414 \"\u041a\u041e\u041b\u041b\u0415\u0414\u0416\"", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u044b", None))
        self.groupBox_3.setTitle("")
        self.groupBox_4.setTitle("")
        self.lineEdit_6.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440\u0437\u0430\u0446\u0438\u044f", None))
        self.groupBox_7.setTitle("")
        self.lineEdit_11.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEdit_12.setText("")
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_14.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.lineEdit_15.setText("")
        self.lineEdit_16.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u043c\u0435\u043d\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.groupBox.setTitle("")
        self.pushButton.setText("")
        self.pushButton_2.setStyleSheet(QCoreApplication.translate("Form", u"\n"
"QPushButton {\n"
"  background-color: #fff;\n"
"  border: 1px solid #d5d9d9;\n"
"  border-radius: 8px;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  box-sizing: border-box;\n"
"  color: #0f1111;\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  font-family: \"Amazon Ember\",sans-serif;\n"
"  font-size: 18px;\n"
"  line-height: 29px;\n"
"  padding: 0 10px 0 11px;\n"
"  position: relative;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  -webkit-user-select: none;\n"
"  touch-action: manipulation;\n"
"  vertical-align: middle;\n"
"  width: 100px;\n"
"box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #f7fafa;\n"
"}\n"
"\n"
"QPushButton:focus {\n"
"  border-color: #008296;\n"
"  box-shadow: rgba(213, 217, 217, .5) 0 2px 5px 0;\n"
"  outline: 0;\n"
"}", None))
        self.pushButton_2.setText("")
        self.groupBox_2.setTitle("")
        self.lineEdit.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.comboBox.setCurrentText("")
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0443\u043f\u043f\u044b", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.view), QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440", None))
        self.groupBox_5.setTitle("")
        self.pushButton_5.setText("")
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.pushButton_8.setText("")
        self.pushButton_9.setText("")
        self.groupBox_6.setTitle("")
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.lineEdit_8.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0443\u043f\u043f\u044b", None))
        self.lineEdit_9.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.lineEdit_10.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0451\u0442\u044b", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043e\u0442\u0447\u0451\u0442", None))
        self.lineEdit_17.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.change), QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u042d\u0418\u041e\u0421", None))
        self.groupBox_11.setTitle("")
        self.groupBox_12.setTitle("")
        self.lineEdit_71.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0445\u043e\u0434\u044b", None))
        self.lineEdit_55.setText(QCoreApplication.translate("Form", u"\u041f\u043b\u0430\u043d\u0438\u0440\u0443\u0435\u043c\u044b\u0435", None))
        self.lineEdit_62.setText("")
        self.lineEdit_62.setPlaceholderText("")
        self.lineEdit_56.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u043d\u044b\u0435", None))
        self.lineEdit_57.setStyleSheet(QCoreApplication.translate("Form", u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}R", None))
        self.lineEdit_58.setText(QCoreApplication.translate("Form", u"\u041e\u0436\u0438\u0434\u0430\u044e\u0442\u0441\u044f", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Form", u"\u0422\u0438\u043f", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u043b\u0431\u0447\u0430\u0442\u0430\u044f", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u041a\u0440\u0443\u0433\u043e\u0432\u0430\u044f", None))
        self.pushButton_35.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u0433\u0440\u0430\u0444\u0438\u043a(-\u0438)", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u0435\u0439", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Form", u"\u0422\u0438\u043f", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u043b\u0431\u0447\u0430\u0442\u0430\u044f", None))
        self.checkBox_5.setText(QCoreApplication.translate("Form", u"\u041a\u0440\u0443\u0433\u043e\u0432\u0430\u044f", None))
        self.pushButton_36.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u0433\u0440\u0430\u0444\u0438\u043a(-\u0438)", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0433\u0440\u0443\u043f\u043f", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("Form", u"\u0422\u0438\u043f", None))
        self.checkBox_6.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u043b\u0431\u0447\u0430\u0442\u0430\u044f", None))
        self.checkBox_7.setText(QCoreApplication.translate("Form", u"\u041a\u0440\u0443\u0433\u043e\u0432\u0430\u044f", None))
        self.pushButton_37.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438 \u0433\u0440\u0430\u0444\u0438\u043a(-\u0438)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stats), QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430", None))
        self.groupBox_19.setTitle("")
        self.lineEdit_38.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox_20.setTitle("")
        self.pushButton_28.setText("")
        self.groupBox_21.setTitle(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043f\u0443\u0442\u0435\u0439", None))
        self.pushButton_33.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.pushButton_29.setText(QCoreApplication.translate("Form", u"\u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0443\u0442\u044c", None))
        self.pushButton_31.setText(QCoreApplication.translate("Form", u"\u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0443\u0442\u044c", None))
        self.pushButton_30.setText(QCoreApplication.translate("Form", u"\u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0443\u0442\u044c", None))
        self.pushButton_32.setText(QCoreApplication.translate("Form", u"\u0443\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u0443\u0442\u044c", None))
        self.lineEdit_41.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0434\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.lineEdit_39.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u043a \u0431\u0430\u0437\u0435 \u0434\u0435\u043d\u043d\u044b\u0445", None))
        self.lineEdit_42.setStyleSheet(QCoreApplication.translate("Form", u"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}R", None))
        self.lineEdit_43.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u043a backup \u0431\u0430\u0437\u0435 \u0434\u0435\u043d\u043d\u044b\u0445", None))
        self.lineEdit_45.setText(QCoreApplication.translate("Form", u"\u041f\u0443\u0442\u044c \u043a \u0442\u043e\u043a\u0435\u043d\u0443 \u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.lineEdit_40.setText("")
        self.lineEdit_40.setPlaceholderText("")
        self.groupBox_22.setTitle(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b", None))
        self.lineEdit_47.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0447\u0442\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044f", None))
        self.lineEdit_54.setText("")
        self.lineEdit_48.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c \u043f\u043e\u0447\u0442\u044b \u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044f", None))
        self.lineEdit_50.setText(QCoreApplication.translate("Form", u"\u0422\u043e\u043a\u0435\u043d \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.lineEdit_52.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0447\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0430\u0442\u0435\u043b\u044f", None))
        self.pushButton_34.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settigs), QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.groupBox_8.setTitle("")
        self.lineEdit_21.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u043d\u0435\u043b\u044c \u0443\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0434\u043e\u0441\u0442\u0443\u043f\u043e\u043c", None))
        self.groupBox_9.setTitle("")
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_14.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.admin), QCoreApplication.translate("Form", u"\u0410\u0434\u043c\u0438\u043d \u043f\u0430\u043d\u0435\u043b\u044c", None))
        self.groupBox_15.setTitle("")
        self.groupBox_16.setTitle("")
        self.groupBox_17.setTitle("")
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"FAQ", None))
    # retranslateUi

