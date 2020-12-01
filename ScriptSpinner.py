import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from splash_screen import Ui_Splash_Screen
from login import Ui_Login
from test_screen import Ui_MainWindow
from main import Ui_Main

splash_counter = 0

class MainWindow(QMainWindow):
    def __init__(self, email):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if email != "":
            self.ui.label_2.setText(str("Username: " + email))

class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.ui.actionKey_Time_Line.triggered.connect(self.toggle_left)

    def toggle_left(self):
        if self.ui.Left_widget.isVisible():
            self.ui.Left_widget.hide()
        else:
            self.ui.Left_widget.show()

class Login(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)

        self.ui.login_btn.clicked.connect(self.login_click)

    def login_click(self):
        email = self.ui.email_line.text()
        password = self.ui.password_line.text()
        remember = self.ui.check_remember.isChecked()

        print(email, password, remember) # print to console

        self.main = Main()
        self.main.show()
        self.close()

class Splash_Screen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Splash_Screen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)

        self.show()

    def progress(self):
        global splash_counter

        self.ui.progressBar.setValue(splash_counter)

        if splash_counter > 100:
            self.timer.stop()
            self.login = Login()
            self.login.show()
            self.close()

        splash_counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Splash_Screen()
    sys.exit(app.exec_())