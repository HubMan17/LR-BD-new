# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_rep_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(617, 288)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 10, 401, 271))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 40, 101, 22))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 40, 271, 22))
        self.lineEdit_2.setFont(font)
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 70, 101, 22))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(120, 70, 271, 22))
        self.lineEdit_4.setFont(font)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 210, 131, 51))
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(120, 100, 271, 22))
        self.lineEdit_5.setFont(font)
        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(10, 130, 101, 22))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(10, 100, 101, 22))
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setReadOnly(True)
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(120, 130, 270, 22))
        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(120, 10, 271, 22))
        self.lineEdit_7.setFont(font)
        self.lineEdit_9 = QLineEdit(self.groupBox)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setGeometry(QRect(10, 10, 101, 22))
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setReadOnly(True)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(410, 70, 201, 141))
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 10, 161, 20))
        self.checkBox.setFont(font)
        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 40, 161, 20))
        self.checkBox_2.setFont(font)
        self.checkBox_3 = QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(10, 70, 161, 20))
        self.checkBox_3.setFont(font)
        self.checkBox_4 = QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(10, 100, 161, 20))
        self.checkBox_4.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.groupBox.setTitle("")
        self.lineEdit.setText(QCoreApplication.translate("Form", u"name", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"diplom", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.lineEdit_6.setText(QCoreApplication.translate("Form", u"raeson", None))
        self.lineEdit_8.setText(QCoreApplication.translate("Form", u"rep_date", None))
        self.lineEdit_7.setText("")
        self.lineEdit_9.setText(QCoreApplication.translate("Form", u"rep_id", None))
        self.groupBox_2.setTitle("")
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u043a\u0440\u044b\u0442\u044c \u043e\u0442\u0447\u0451\u0442", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u0447\u0451\u0442 \u043d\u0430 \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u0441\u043e\u0437\u0434\u0430\u0442\u044c PDF", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u043f\u043e\u0447\u0442\u0443", None))
    # retranslateUi

