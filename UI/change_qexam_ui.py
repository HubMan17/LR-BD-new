# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_qexam_ui.ui'
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
    QScrollArea, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(650, 375)
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(190, 40, 290, 22))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(330, 130, 291, 141))
        self.scrollArea.setMinimumSize(QSize(0, 141))
        self.scrollArea.setMaximumSize(QSize(16777215, 141))
        self.scrollArea.setBaseSize(QSize(0, 141))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 289, 139))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.lineEdit_4 = QLineEdit(Form)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 100, 291, 22))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setReadOnly(True)
        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 130, 290, 141))
        self.textEdit.setFont(font)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(22, 40, 160, 22))
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit_3 = QLineEdit(Form)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(22, 70, 160, 22))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setReadOnly(True)
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(190, 70, 290, 22))
        self.comboBox.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(440, 290, 141, 51))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442\u044b \u044d\u043a\u0437\u0430\u043c\u0435\u043d\u0430", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"\u042d\u043a\u0437\u0430\u043c\u0435\u043d", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
    # retranslateUi

