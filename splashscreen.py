# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashscreen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Splash_Screen(object):
    def setupUi(self, Splash_Screen):
        if not Splash_Screen.objectName():
            Splash_Screen.setObjectName(u"Splash_Screen")
        Splash_Screen.resize(720, 425)
        self.centralwidget = QWidget(Splash_Screen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 720, 425))
        self.label.setLineWidth(0)
        self.label.setPixmap(QPixmap(u"img/SS_logo.jpg"))
        self.label.setIndent(0)
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(70, 330, 591, 41))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(98, 114, 164);\n"
"	color:rgb(200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"	border-radius: 10px;\n"
"	bavkground_color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(210, 157, 255, 255), stop:1 rgba(156, 69, 255, 255));\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.frame)

        Splash_Screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(Splash_Screen)

        QMetaObject.connectSlotsByName(Splash_Screen)
    # setupUi

    def retranslateUi(self, Splash_Screen):
        Splash_Screen.setWindowTitle(QCoreApplication.translate("Splash_Screen", u"MainWindow", None))
        self.label.setText("")
    # retranslateUi

