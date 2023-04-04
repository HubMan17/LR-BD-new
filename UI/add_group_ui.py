# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_group_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(404, 215)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 401, 211))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 101, 22))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 20, 271, 22))
        self.lineEdit_2.setFont(font)
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 50, 101, 22))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setReadOnly(True)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 150, 131, 51))
        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(120, 80, 271, 22))
        self.lineEdit_6.setFont(font)
        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(10, 110, 101, 22))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(10, 80, 101, 22))
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setReadOnly(True)
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 110, 270, 22))
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(120, 50, 270, 22))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.groupBox.setTitle("")
        self.lineEdit.setText(QCoreApplication.translate("Form", u"name", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"course", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"specName", None))
        self.lineEdit_8.setText(QCoreApplication.translate("Form", u"curator", None))
    # retranslateUi

