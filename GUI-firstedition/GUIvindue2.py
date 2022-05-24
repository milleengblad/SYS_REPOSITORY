

from PyQt6 import QtCore, QtGui, QtWidgets
from GUIvindue3 import Ui_Vindue3_2
#from qtwidgets import PasswordEdit

class Ui_Window2_2(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Vindue3_2()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Window2_2):
        Window2_2.setObjectName("Window2_2")
        Window2_2.resize(802, 595)
        self.centralwidget = QtWidgets.QWidget(Window2_2)
        self.centralwidget.setObjectName("centralwidget")
        self.Window2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Window2.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.Window2.setObjectName("Window2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 0, 801, 121))
        self.textEdit_2.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.textEdit_2.setObjectName("textEdit_2")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())


        self.pushButton_2.setGeometry(QtCore.QRect(350, 420, 80, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(260, 170, 261, 61))
        self.textEdit_4.setStyleSheet("background-color: rgb(146, 146, 146);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(330, 250, 111, 31))
        self.textBrowser.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(330, 330, 111, 31))
        self.textBrowser_2.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 290, 351, 31))
        self.lineEdit.setObjectName("lineEdit")

        #Password
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 380, 351, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
       # print(type(self.lineEdit_2))
       # self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 470, 491, 41))
        self.label.setText("")
        self.label.setObjectName("label")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 520, 141, 31))
        self.textEdit_5.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_5.setObjectName("textEdit_5")
        Window2_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window2_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 21))
        self.menubar.setObjectName("menubar")
        Window2_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window2_2)
        self.statusbar.setObjectName("statusbar")
        Window2_2.setStatusBar(self.statusbar)

        self.retranslateUi(Window2_2)
        QtCore.QMetaObject.connectSlotsByName(Window2_2)

    def retranslateUi(self, Window2_2):
        _translate = QtCore.QCoreApplication.translate
        Window2_2.setWindowTitle(_translate("Window2_2", "MainWindow"))
        self.textEdit_2.setHtml(_translate("Window2_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:24pt; font-weight:700; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">BestBooking</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Window2_2", "LOGIN"))
        self.textEdit_4.setHtml(_translate("Window2_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Velkommen til BestBooking </span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-weight:700;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Fortsæt ved at logge ind</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Window2_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Brugernavn </p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Window2_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kodeord</p></body></html>"))
        self.textEdit_5.setHtml(_translate("Window2_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select Language</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window2_2 = QtWidgets.QMainWindow()
    ui = Ui_Window2_2()
    ui.setupUi(Window2_2)
    Window2_2.show()
    sys.exit(app.exec())

