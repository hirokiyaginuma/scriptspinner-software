import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from splash_screen import Ui_Splash_Screen
from login import Ui_Login
from test_screen import Ui_MainWindow

counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Login(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)

class Splash_Screen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Splash_Screen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(18)

        self.show()

    def progress(self):
        global counter

        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.login = Login()
            self.login.show()
            self.close()

        counter += 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Splash_Screen()
    sys.exit(app.exec_())