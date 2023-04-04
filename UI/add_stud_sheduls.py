# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_stud_sheduls.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(505, 447)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 501, 441))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 482, 909))
        self.scrollAreaWidgetContents.setStyleSheet(u"QLineEdit {\n"
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
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setContentsMargins(-1, 5, -1, -1)
        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 0))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.lineEdit)

        self.lineEdit_5 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMinimumSize(QSize(200, 0))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setReadOnly(True)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.lineEdit_5)

        self.lineEdit_6 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferLatin)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.lineEdit_6)

        self.lineEdit_7 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(200, 0))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setReadOnly(True)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.lineEdit_7)

        self.lineEdit_8 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferLatin)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.lineEdit_8)

        self.lineEdit_9 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(200, 0))
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setReadOnly(True)

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.lineEdit_9)

        self.lineEdit_11 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(200, 0))
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setReadOnly(True)

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.lineEdit_11)

        self.lineEdit_13 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setMinimumSize(QSize(200, 0))
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setReadOnly(True)

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.lineEdit_13)

        self.lineEdit_15 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_15.setObjectName(u"lineEdit_15")
        self.lineEdit_15.setMinimumSize(QSize(200, 0))
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setReadOnly(True)

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.lineEdit_15)

        self.lineEdit_17 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMinimumSize(QSize(200, 0))
        self.lineEdit_17.setFont(font)
        self.lineEdit_17.setReadOnly(True)

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.lineEdit_17)

        self.lineEdit_19 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setMinimumSize(QSize(200, 0))
        self.lineEdit_19.setFont(font)
        self.lineEdit_19.setReadOnly(True)

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.lineEdit_19)

        self.lineEdit_21 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setMinimumSize(QSize(200, 0))
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setReadOnly(True)

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.lineEdit_21)

        self.lineEdit_23 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setMinimumSize(QSize(200, 0))
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setReadOnly(True)

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.lineEdit_23)

        self.lineEdit_25 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setMinimumSize(QSize(200, 0))
        self.lineEdit_25.setFont(font)
        self.lineEdit_25.setReadOnly(True)

        self.formLayout_3.setWidget(14, QFormLayout.LabelRole, self.lineEdit_25)

        self.lineEdit_27 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setMinimumSize(QSize(200, 0))
        self.lineEdit_27.setFont(font)
        self.lineEdit_27.setReadOnly(True)

        self.formLayout_3.setWidget(15, QFormLayout.LabelRole, self.lineEdit_27)

        self.lineEdit_34 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setMinimumSize(QSize(200, 0))
        self.lineEdit_34.setFont(font)
        self.lineEdit_34.setReadOnly(True)

        self.formLayout_3.setWidget(16, QFormLayout.LabelRole, self.lineEdit_34)

        self.lineEdit_29 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setMinimumSize(QSize(200, 0))
        self.lineEdit_29.setFont(font)
        self.lineEdit_29.setReadOnly(True)

        self.formLayout_3.setWidget(17, QFormLayout.LabelRole, self.lineEdit_29)

        self.lineEdit_31 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setMinimumSize(QSize(200, 0))
        self.lineEdit_31.setFont(font)
        self.lineEdit_31.setReadOnly(True)

        self.formLayout_3.setWidget(18, QFormLayout.LabelRole, self.lineEdit_31)

        self.lineEdit_35 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setMinimumSize(QSize(200, 0))
        self.lineEdit_35.setFont(font)
        self.lineEdit_35.setReadOnly(True)

        self.formLayout_3.setWidget(19, QFormLayout.LabelRole, self.lineEdit_35)

        self.lineEdit_38 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setMinimumSize(QSize(200, 0))
        self.lineEdit_38.setFont(font)
        self.lineEdit_38.setReadOnly(True)

        self.formLayout_3.setWidget(20, QFormLayout.LabelRole, self.lineEdit_38)

        self.lineEdit_42 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setMinimumSize(QSize(200, 0))
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setReadOnly(True)

        self.formLayout_3.setWidget(21, QFormLayout.LabelRole, self.lineEdit_42)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 45))
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

        self.formLayout_3.setWidget(23, QFormLayout.FieldRole, self.pushButton)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setFont(font)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.comboBox)

        self.comboBox_2 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setFont(font)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.comboBox_2)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setFont(font)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.comboBox_3)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_4.setObjectName(u"comboBox_4")
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setFont(font)

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.comboBox_4)

        self.comboBox_5 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_5.setObjectName(u"comboBox_5")
        sizePolicy.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy)
        self.comboBox_5.setFont(font)

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.comboBox_5)

        self.comboBox_6 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_6.setObjectName(u"comboBox_6")
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.comboBox_6.setFont(font)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.comboBox_6)

        self.comboBox_7 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_7.setObjectName(u"comboBox_7")
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.comboBox_7.setFont(font)

        self.formLayout_3.setWidget(12, QFormLayout.FieldRole, self.comboBox_7)

        self.comboBox_8 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_8.setObjectName(u"comboBox_8")
        sizePolicy.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy)
        self.comboBox_8.setFont(font)

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.comboBox_8)

        self.comboBox_9 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_9.setObjectName(u"comboBox_9")
        sizePolicy.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy)
        self.comboBox_9.setFont(font)

        self.formLayout_3.setWidget(14, QFormLayout.FieldRole, self.comboBox_9)

        self.comboBox_10 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_10.setObjectName(u"comboBox_10")
        sizePolicy.setHeightForWidth(self.comboBox_10.sizePolicy().hasHeightForWidth())
        self.comboBox_10.setSizePolicy(sizePolicy)
        self.comboBox_10.setFont(font)

        self.formLayout_3.setWidget(15, QFormLayout.FieldRole, self.comboBox_10)

        self.comboBox_11 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_11.setObjectName(u"comboBox_11")
        sizePolicy.setHeightForWidth(self.comboBox_11.sizePolicy().hasHeightForWidth())
        self.comboBox_11.setSizePolicy(sizePolicy)
        self.comboBox_11.setFont(font)

        self.formLayout_3.setWidget(16, QFormLayout.FieldRole, self.comboBox_11)

        self.comboBox_12 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_12.setObjectName(u"comboBox_12")
        sizePolicy.setHeightForWidth(self.comboBox_12.sizePolicy().hasHeightForWidth())
        self.comboBox_12.setSizePolicy(sizePolicy)
        self.comboBox_12.setFont(font)

        self.formLayout_3.setWidget(17, QFormLayout.FieldRole, self.comboBox_12)

        self.comboBox_13 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_13.setObjectName(u"comboBox_13")
        sizePolicy.setHeightForWidth(self.comboBox_13.sizePolicy().hasHeightForWidth())
        self.comboBox_13.setSizePolicy(sizePolicy)
        self.comboBox_13.setFont(font)

        self.formLayout_3.setWidget(18, QFormLayout.FieldRole, self.comboBox_13)

        self.comboBox_14 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_14.setObjectName(u"comboBox_14")
        sizePolicy.setHeightForWidth(self.comboBox_14.sizePolicy().hasHeightForWidth())
        self.comboBox_14.setSizePolicy(sizePolicy)
        self.comboBox_14.setFont(font)

        self.formLayout_3.setWidget(19, QFormLayout.FieldRole, self.comboBox_14)

        self.comboBox_15 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_15.setObjectName(u"comboBox_15")
        sizePolicy.setHeightForWidth(self.comboBox_15.sizePolicy().hasHeightForWidth())
        self.comboBox_15.setSizePolicy(sizePolicy)
        self.comboBox_15.setFont(font)

        self.formLayout_3.setWidget(20, QFormLayout.FieldRole, self.comboBox_15)

        self.comboBox_16 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_16.setObjectName(u"comboBox_16")
        sizePolicy.setHeightForWidth(self.comboBox_16.sizePolicy().hasHeightForWidth())
        self.comboBox_16.setSizePolicy(sizePolicy)
        self.comboBox_16.setFont(font)

        self.formLayout_3.setWidget(21, QFormLayout.FieldRole, self.comboBox_16)

        self.lineEdit_3 = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(200, 0))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.lineEdit_3)

        self.comboBox_17 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_17.setObjectName(u"comboBox_17")
        sizePolicy.setHeightForWidth(self.comboBox_17.sizePolicy().hasHeightForWidth())
        self.comboBox_17.setSizePolicy(sizePolicy)
        self.comboBox_17.setFont(font)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.comboBox_17)

        self.comboBox_18 = QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_18.setObjectName(u"comboBox_18")
        sizePolicy.setHeightForWidth(self.comboBox_18.sizePolicy().hasHeightForWidth())
        self.comboBox_18.setSizePolicy(sizePolicy)
        self.comboBox_18.setFont(font)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.comboBox_18)


        self.gridLayout.addLayout(self.formLayout_3, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0438\u043d\u0430", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0439 \u0441\u0435\u043c\u0435\u0441\u0442\u0440", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043d\u0435\u0447\u043d\u044b\u0439 \u0441\u0435\u043c\u0435\u0441\u0442\u0440", None))
        self.lineEdit_9.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21161 \u0437\u0430\u0447\u0451\u0442", None))
        self.lineEdit_11.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21161 \u044d\u043a\u0437\u0430\u043c\u0435\u043d", None))
        self.lineEdit_13.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21162 \u0437\u0430\u0447\u0451\u0442", None))
        self.lineEdit_15.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21162 \u044d\u043a\u0437\u0430\u043c\u0435\u043d", None))
        self.lineEdit_17.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21163 \u0437\u0430\u0447\u0451\u0442", None))
        self.lineEdit_19.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21163 \u044d\u043a\u0437\u0430\u043c\u0435\u043d", None))
        self.lineEdit_21.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21164 \u0437\u0430\u0447\u0451\u0442", None))
        self.lineEdit_23.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21164 \u044d\u043a\u0437\u0430\u043c\u0435\u043d", None))
        self.lineEdit_25.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21165 \u0437\u0430\u0447\u0451\u0442", None))
        self.lineEdit_27.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21165 \u044d\u043a\u0437\u0430\u043c\u0435\u043d", None))
        self.lineEdit_34.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21166 \u0437\u0430\u0447\u0451\u0442", None))
        self.lineEdit_29.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21166 \u044d\u043a\u0437\u0430\u043c\u0435\u043d", None))
        self.lineEdit_31.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21167 \u0437\u0430\u0447\u0451\u0442", None))
        self.lineEdit_35.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21167 \u044d\u043a\u0437\u0430\u043c\u0435\u043d", None))
        self.lineEdit_38.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21168 \u0437\u0430\u0447\u0451\u0442", None))
        self.lineEdit_42.setText(QCoreApplication.translate("Form", u"\u0421\u0435\u0441\u0441\u0438\u044f \u21168 \u044d\u043a\u0437\u0430\u043c\u0435\u043d", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c", None))
        self.comboBox.setCurrentText("")
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0435\u0446\u0438\u0430\u043b\u044c\u043d\u043e\u0441\u0442\u044c", None))
        self.comboBox_17.setCurrentText("")
        self.comboBox_18.setCurrentText("")
    # retranslateUi

