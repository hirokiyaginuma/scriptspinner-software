import sys, pickle
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_splash_screen import Ui_Splash_Screen
from ui_login import Ui_Login
from ui_test_screen import Ui_MainWindow
from main import Main
from user import User

splash_counter = 0

class MainWindow(QMainWindow):
    def __init__(self, email):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if email != "":
            self.ui.label_2.setText(str("Username: " + email))

class Login(QWidget):
    def __init__(self, user):
        QWidget.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.user = user

        self.ui.login_btn.clicked.connect(self.login_click)

    def login_click(self):
        email = self.ui.email_line.text()
        password = self.ui.password_line.text()
        remember = self.ui.check_remember.isChecked()

        self.user.login(email, password, remember)

        if self.user.is_logged_in:
            self.main = Main(self.user)
            self.main.show()
            self.close()
        else:
            QMessageBox.warning(self,"Login failed", 
                "The email and password you entered did not match our records. Please double-check and try again.")

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

            user = User()
            if user.is_logged_in:
                self.main = Main(user)
                self.main.show()
                self.close()
            else:
                self.login = Login(user)
                self.login.show()
                self.close()

        splash_counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Splash_Screen()
    sys.exit(app.exec_())