import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(445, 147)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl1.setGeometry(QtCore.QRect(40, 40, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.lbl1.setFont(font)
        self.lbl1.setStyleSheet("background-color: rgba(255, 255, 255, 0.5);\n"
"border:none")
        self.lbl1.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl1.setLineWidth(1)
        self.lbl1.setText("")
        self.lbl1.setObjectName("lbl1")
        self.btngen = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.gen())
        self.btngen.setGeometry(QtCore.QRect(330, 30, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btngen.setFont(font)
        self.btngen.setStyleSheet("*{background-color:rgba(0, 0, 0, 0.2);\n"
"}\n"
":hover{\n"
"background-color:rgba(0, 0, 0, 0.4);\n"
"}\n"
"\n"
":pushed{\n"
"    background-color:rgba(0, 0, 0, 0.6);\n"
"}")
        self.btngen.setObjectName("btngen")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(-10, 0, 461, 151))
        self.textEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(92, 142, 181, 167));")
        self.textEdit.setObjectName("textEdit")
        self.btncopy = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.copy())
        self.btncopy.setGeometry(QtCore.QRect(330, 60, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.btncopy.setFont(font)
        self.btncopy.setStyleSheet("*{background-color:rgba(0, 0, 0, 0.2);\n"
"}\n"
":hover{\n"
"background-color:rgba(0, 0, 0, 0.4);\n"
"}\n"
"\n"
":pushed{\n"
"    background-color:rgba(0, 0, 0, 0.6);\n"
"}")
        self.btncopy.setObjectName("btncopy")
        self.textEdit.raise_()
        self.lbl1.raise_()
        self.btngen.raise_()
        self.btncopy.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PasswordGen"))
        self.btngen.setText(_translate("MainWindow", "Generate"))
        self.btncopy.setText(_translate("MainWindow", "Copy"))

    def gen(self):
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"
        password = ""
        password_length = random.randint(8, 16)

        for x in range(password_length):
            char = random.choice(chars)
            password = password + char
        
        self.lbl1.setText(password)

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.clear(mode=clipboard.Clipboard )
        try:
            clipboard.text = self.lbl1.text().encode('utf-8').decode('utf-8') 
            clip = str(clipboard.text)
            clipboard.setText(clip, mode=clipboard.Clipboard)
        except:
            self.lbl1.setText(("ERROR"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




'''
while 1:
    password_len = int(input("Password length:"))
    password_count = int(input("How many passwords:"))
    for x in range(0,password_count):
        password = ""
        for x in range(0, password_len):
            password_char = random.choice(chars)
            password = password + password_char
        print("Password is:", password)



characters = string.ascii_letters + string.punctuation  + string.digits

password = ""
password_length = random.randint(8, 16)

for x in range(password_length):
    char = random.choice(characters)
    password = password + char
'''