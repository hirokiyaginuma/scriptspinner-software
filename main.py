import sys, time, pickle
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
        self.goaltime = 300

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
        self.ui.actionSet_Time.triggered.connect(self.dialog_settime)
        #self.ui.actionFont.triggered.connect(self)
        #self.ui.actionColor.triggered.connect(self)
        #self.ui.actionBold.triggered.connect(self)
        #self.ui.actionItalic.triggered.connect(self)
        #self.ui.actionUnderline.triggered.connect(self)
        self.ui.actionKey_Time_Line.triggered.connect(self.toggle_left)
        self.ui.actionTime.triggered.connect(self.toggle_time)
        self.ui.actionWord_Count.triggered.connect(self.toggle_word_count)
        self.ui.actionSide_Notes.triggered.connect(self.toggle_side_notes)
        self.ui.actionYour_Account.triggered.connect(self.yourAccount)
        self.ui.actionLogout.triggered.connect(self.logout)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionAbout_Qt_lisence.triggered.connect(self.aboutQt)

        self.ui.btn_plus.clicked.connect(self.addlist)
        self.ui.btn_minus.clicked.connect(self.deletelist)

        self.ui.textEdit_Script.textChanged.connect(self.updateInfo)

        self.ui.current_time_label.setText("00:00")
        self.ui.word_count_label.setText(str(self.secondToWord(self.goaltime)) + 
            " words to " + str(self.secondToTime(self.goaltime)))

    def new(self):
        self.ui.textEdit_Script.clear()
        self.ui.textEdit_Sidenotes.clear()
        self.filename = ""

    def open(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open',".","Script Spinner File (*.ssp)")[0]

        if self.filename:
            with open(self.filename, 'rb') as f:
                timelist, script, sidenotes = pickle.load(f)
                self.ui.TimeList.clear()
                [self.ui.TimeList.addItem(timelist[i]) for i in range(0, len(timelist))]
                for index in range(self.ui.TimeList.count()):
                    item = self.ui.TimeList.item(index)
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
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
    
    def yourAccount(self):
        QDesktopServices.openUrl(QUrl("https://scriptspinner.com/account/"))

    def about(self):
        QMessageBox.information(self,"About", 
            "Script Spinner is simple and complete software solution for your presentation needs\nCOPYRIGHT 2020 Script Spinner. All rights reserved")

    def aboutQt(self):
        QApplication.instance().aboutQt()

    def addlist(self):
        text, ok = QInputDialog.getText(self, 'Add New Time Line', 'Enter the name:')
        if ok:
            self.ui.TimeList.addItem(text)
            for index in range(self.ui.TimeList.count()):
                    item = self.ui.TimeList.item(index)
                    item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

    def deletelist(self):
        listItems = self.ui.TimeList.selectedItems()
        if not listItems:
            return        
        for item in listItems:
            self.ui.TimeList.takeItem(self.ui.TimeList.row(item))

    def dialog_settime(self):
        sec, ok = QInputDialog.getInt(self, "Set Time", "Enter a goal time in seconds")
        if ok:
            self.goaltime = sec
        self.updateInfo()

    def wordcount(self):
        text = self.ui.textEdit_Script.toPlainText()
        words = len(text.split())
        return words

    def howManyWord(self, word, second, wpm=130):
        self.secondToWord(word, wpm)

    def wordToSecond(self, word, wpm=130, base=15):
        return base * round((word / wpm * 60 ) / base)

    def secondToWord(self, second, wpm=130, base=15):
        return base * round((second * wpm / 60) / base)

    def secondToTime(self, second):
        if second > 3600:
            sec = time.strftime("%H:%M:%S", time.gmtime(second))
        else:
            sec = time.strftime("%M:%S", time.gmtime(second))
        return sec

    def updateInfo(self):
        wc_sec = self.wordToSecond(self.wordcount())
        wc_time = self.secondToTime(wc_sec)
        self.ui.current_time_label.setText(str(wc_time))

        goal_word = self.secondToWord(self.goaltime)
        rm_word = goal_word - self.wordcount()

        self.ui.word_count_label.setText(str(rm_word) + " words to " + str(self.secondToTime(self.goaltime)))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Main(None)
    win.show()
    sys.exit(app.exec_())