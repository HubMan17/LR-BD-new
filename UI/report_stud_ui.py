# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_stud_ui.ui'
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
        Form.resize(715, 217)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(440, 10, 241, 181))
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 10, 161, 20))
        font = QFont()
        font.setPointSize(11)
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
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 401, 181))
        self.comboBox_5 = QComboBox(self.groupBox)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setGeometry(QRect(130, 20, 261, 22))
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(250, 130, 131, 41))
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 20, 113, 22))
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit_5.setFont(font1)
        self.lineEdit_5.setReadOnly(True)
        self.comboBox_6 = QComboBox(self.groupBox)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(130, 60, 261, 22))
        self.lineEdit_6 = QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(10, 60, 113, 22))
        self.lineEdit_6.setFont(font1)
        self.lineEdit_6.setReadOnly(True)
        self.comboBox_7 = QComboBox(self.groupBox)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(130, 100, 261, 22))
        self.lineEdit_7 = QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(10, 100, 113, 22))
        self.lineEdit_7.setFont(font1)
        self.lineEdit_7.setReadOnly(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0451\u0442 \u043f\u043e \u0441\u0442\u0443\u0434\u0435\u043d\u0442\u0443", None))
        self.groupBox_2.setTitle("")
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u043a\u0440\u044b\u0442\u044c \u043e\u0442\u0447\u0451\u0442", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u0447\u0451\u0442 \u043d\u0430 \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u0441\u043e\u0437\u0434\u0430\u0442\u044c PDF", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u043f\u043e\u0447\u0442\u0443", None))
        self.groupBox.setTitle("")
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"\u0413\u0440\u0443\u043f\u043f\u0430", None))
        self.lineEdit_6.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0443\u0434\u0435\u043d\u0442", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0451\u0442", None))
    # retranslateUi

