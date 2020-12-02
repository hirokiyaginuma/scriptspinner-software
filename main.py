import sys, pickle
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_main import Ui_Main

class Main(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_Main()
        self.ui.setupUi(self)

        self.filename = ""
        self.is_change_saved = True

        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionSave.triggered.connect(self.save)
        self.ui.actionKey_Time_Line.triggered.connect(self.toggle_left)
        self.ui.actionTime.triggered.connect(self.toggle_time)
        self.ui.actionWord_Count.triggered.connect(self.toggle_word_count)
        self.ui.actionSide_Notes.triggered.connect(self.toggle_side_notes)
        self.ui.actionAbout_Qt_lisence.triggered.connect(self.aboutQt)

    def new(self):
        self.ui.textEdit_Script.clear()
        self.ui.textEdit_Sidenotes.clear()

    def save(self):
        timelist = [str(self.ui.TimeList.item(i).text()) for i in range(self.ui.TimeList.count())]
        script = self.ui.textEdit_Script.toHtml()
        sidenotes = self.ui.textEdit_Sidenotes.toHtml()

        print(timelist)
        print()
        print(script)
        print()
        print(sidenotes)
        print()
        
        if not self.filename:
            self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save', None, "Script Spinner File (.ssp)")[0]

        print(self.filename)

        if self.filename:
            if not self.filename.endswith(".ssp"):
                self.filename += ".ssp"
            
            with open(self.filename, 'wb') as f:
                pickle.dump([timelist, script, sidenotes], f)


    def toggle_left(self):
        if self.ui.Left_widget.isVisible():
            self.ui.Left_widget.hide()
        else:
            self.ui.Left_widget.show()

    def toggle_right(self):
        if not self.ui.Right_widget.isVisible():
            self.ui.Right_widget.show()
        
        if not (self.ui.time.isVisible() or self.ui.word_count.isVisible()
            or self.ui.sidenotes.isVisible()):
            self.ui.Right_widget.hide()

    def toggle_time(self):
        if self.ui.time.isVisible():
            self.ui.time.hide()
        else:
            self.ui.time.show()

        self.toggle_right()

    def toggle_word_count(self):
        if self.ui.word_count.isVisible():
            self.ui.word_count.hide()
        else:
            self.ui.word_count.show()

        self.toggle_right()

    def toggle_side_notes(self):
        if self.ui.sidenotes.isVisible():
            self.ui.sidenotes.hide()
        else:
            self.ui.sidenotes.show()

        self.toggle_right()

    def aboutQt(self):
        QApplication.instance().aboutQt()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())