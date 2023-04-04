# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_disc_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(690, 273)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 40, 191, 31))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(230, 40, 441, 31))
        self.lineEdit_2.setFont(font)
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 80, 191, 31))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setReadOnly(True)
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(230, 80, 440, 30))
        self.comboBox.setFont(font)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(230, 120, 441, 31))
        self.lineEdit_3.setFont(font)
        self.lineEdit_5 = QLineEdit(Form)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(20, 120, 191, 31))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_6 = QLineEdit(Form)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(230, 160, 441, 31))
        self.lineEdit_6.setFont(font)
        self.lineEdit_7 = QLineEdit(Form)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(20, 160, 191, 31))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setReadOnly(True)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(410, 210, 151, 51))
        self.pushButton.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 (\u043d\u0430\u0447\u0430\u043b\u043e)", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u043c\u0435\u0441\u0442\u0440 (\u043a\u043e\u043d\u0435\u0446)", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
    # retranslateUi

