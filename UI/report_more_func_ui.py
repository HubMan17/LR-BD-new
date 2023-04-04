# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report_more_func_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(225, 217)
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 201, 141))
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
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(80, 160, 131, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0451\u0442", None))
        self.groupBox_2.setTitle("")
        self.checkBox.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u043a\u0440\u044b\u0442\u044c \u043e\u0442\u0447\u0451\u0442", None))
        self.checkBox_2.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u0447\u0451\u0442 \u043d\u0430 \u043f\u0435\u0447\u0430\u0442\u044c", None))
        self.checkBox_3.setText(QCoreApplication.translate("Form", u"\u0441\u043e\u0437\u0434\u0430\u0442\u044c PDF", None))
        self.checkBox_4.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c \u043d\u0430 \u043f\u043e\u0447\u0442\u0443", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
    # retranslateUi

