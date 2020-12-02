import sys, pickle
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_main import Ui_Main

class Main(QMainWindow):
    def __init__(self, user):
        QMainWindow.__init__(self)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.user = user

        self.filename = ""
        self.is_change_saved = True

        self.ui.actionNew.triggered.connect(self.new)
        self.ui.actionOpen.triggered.connect(self.open)
        self.ui.actionSave.triggered.connect(self.save)
        #self.ui.actionSave_as.triggered.connect(self)
        #self.ui.actionExit.triggered.connect(self)

        #self.ui.actionUndo.triggered.connect(self)
        #self.ui.actionRedo.triggered.connect(self)
        #self.ui.actionCopy.triggered.connect(self)
        #self.ui.actionCut.triggered.connect(self)
        #self.ui.actionPaste.triggered.connect(self)
        #self.ui.actionFont.triggered.connect(self)
        #self.ui.actionColor.triggered.connect(self)
        #self.ui.actionBold.triggered.connect(self)
        #self.ui.actionItalic.triggered.connect(self)
        #self.ui.actionUnderline.triggered.connect(self)

        self.ui.actionKey_Time_Line.triggered.connect(self.toggle_left)
        self.ui.actionTime.triggered.connect(self.toggle_time)
        self.ui.actionWord_Count.triggered.connect(self.toggle_word_count)
        self.ui.actionSide_Notes.triggered.connect(self.toggle_side_notes)
        #self.ui.actionYour_Account.triggered.connect(self)
        self.ui.actionLogout.triggered.connect(self.logout)

        #self.ui.actionAbout.triggered.connect(self)
        self.ui.actionAbout_Qt_lisence.triggered.connect(self.aboutQt)

    def new(self):
        self.ui.textEdit_Script.clear()
        self.ui.textEdit_Sidenotes.clear()

    def open(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open',".","Script Spinner File (*.ssp)")[0]

        if self.filename:
            with open(self.filename, 'rb') as f:
                timelist, script, sidenotes = pickle.load(f)
                # [str(self.ui.TimeList.item(i).text()) for i in range(timelist])
                self.ui.textEdit_Script.setText(script)
                self.ui.textEdit_Sidenotes.setText(sidenotes)

    def save(self):
        timelist = [str(self.ui.TimeList.item(i).text()) for i in range(self.ui.TimeList.count())]
        script = self.ui.textEdit_Script.toHtml()
        sidenotes = self.ui.textEdit_Sidenotes.toHtml()
        
        if not self.filename:
            self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save', None, "Script Spinner File (*.ssp)")[0]

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

    def logout(self):
        self.user.logout()
        self.close()

    def aboutQt(self):
        QApplication.instance().aboutQt()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main(None)
    win.show()
    sys.exit(app.exec_())