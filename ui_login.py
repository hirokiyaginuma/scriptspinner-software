# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(640, 486)
        Login.setStyleSheet(u"QWidget#Login{\n"
"background-color: rgb(178, 190, 195);\n"
"}")
        self.verticalLayout = QVBoxLayout(Login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"Roboto Light")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QSize(178, 0))
        self.frame_6.setMaximumSize(QSize(178, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Roboto Light")
        font1.setPointSize(13)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 120, -1)
        self.email_line = QLineEdit(self.frame_7)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.email_line)


        self.horizontalLayout.addWidget(self.frame_7)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(Login)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(178, 0))
        self.frame_9.setMaximumSize(QSize(178, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, -1, -1, -1)
        self.label_2 = QLabel(self.frame_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_2)


        self.horizontalLayout_6.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, 120, -1)
        self.password_line = QLineEdit(self.frame_8)
        self.password_line.setObjectName(u"password_line")
        self.password_line.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.password_line.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_4.addWidget(self.password_line)


        self.horizontalLayout_6.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(Login)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setLayoutDirection(Qt.LeftToRight)
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.check_remember = QCheckBox(self.frame_4)
        self.check_remember.setObjectName(u"check_remember")
        font2 = QFont()
        font2.setFamily(u"Roboto Light")
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setWeight(50)
        self.check_remember.setFont(font2)
        self.check_remember.setLayoutDirection(Qt.LeftToRight)
        self.check_remember.setStyleSheet(u"margin-left:50%; margin-right:50%;")
        self.check_remember.setIconSize(QSize(12, 12))
        self.check_remember.setTristate(False)

        self.horizontalLayout_7.addWidget(self.check_remember)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(Login)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(200, -1, 200, -1)
        self.login_btn = QPushButton(self.frame_5)
        self.login_btn.setObjectName(u"login_btn")
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setFont(font1)
        self.login_btn.setStyleSheet(u"\\QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {	\n"
"	background-color: rgba(255, 255, 255, 150);\n"
"}")
        self.login_btn.setIconSize(QSize(16, 16))
        self.login_btn.setAutoDefault(False)
        self.login_btn.setFlat(False)

        self.horizontalLayout_8.addWidget(self.login_btn)


        self.verticalLayout.addWidget(self.frame_5)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Script Spinner - Log in", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"Script Spinner - Log in", None))
        self.label.setText(QCoreApplication.translate("Login", u"Email:", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"Password:", None))
        self.check_remember.setText(QCoreApplication.translate("Login", u"Remember me", None))
        self.login_btn.setText(QCoreApplication.translate("Login", u"Log in", None))
    # retranslateUi

