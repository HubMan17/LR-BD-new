# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth_ui.ui'
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
        Form.resize(400, 192)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 401, 191))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 20, 113, 22))
        font = QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(130, 20, 251, 22))
        self.lineEdit_2.setFont(font)
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 50, 113, 22))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(130, 50, 251, 22))
        self.lineEdit_4.setFont(font)
        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 80, 113, 22))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setReadOnly(True)
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(130, 80, 251, 22))
        self.comboBox.setFont(font)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 120, 171, 51))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.groupBox.setTitle("")
        self.lineEdit.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

