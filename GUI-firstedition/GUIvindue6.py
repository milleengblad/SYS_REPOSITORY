

from PyQt6 import QtCore, QtGui, QtWidgets
from GUIvindue7 import Ui_Window7

class Ui_Window6_2(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window7()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Window6_2):
        Window6_2.setObjectName("Window6_2")
        Window6_2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Window6_2)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 801, 111))
        self.textEdit.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 470, 811, 91))
        self.textEdit_2.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.Window6 = QtWidgets.QWidget(self.centralwidget)
        self.Window6.setGeometry(QtCore.QRect(0, 110, 801, 361))
        self.Window6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Window6.setObjectName("Window6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.Window6)
        self.textEdit_7.setGeometry(QtCore.QRect(10, 50, 121, 301))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.Window6)
        self.textEdit_8.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.textEdit_8.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_10 = QtWidgets.QTextEdit(self.Window6)
        self.textEdit_10.setGeometry(QtCore.QRect(160, 20, 401, 31))
        self.textEdit_10.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_4 = QtWidgets.QTextEdit(self.Window6)
        self.textEdit_4.setGeometry(QtCore.QRect(680, 20, 111, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.Window6)
        self.pushButton.setGeometry(QtCore.QRect(410, 230, 80, 26))
        self.pushButton.setObjectName("pushButton")


        self.pushButton_2 = QtWidgets.QPushButton(self.Window6, clicked = lambda: self.openWindow())


        self.pushButton_2.setGeometry(QtCore.QRect(490, 230, 80, 26))
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.Window6)
        self.textEdit_3.setGeometry(QtCore.QRect(160, 80, 391, 101))
        self.textEdit_3.setObjectName("textEdit_3")
        Window6_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window6_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Window6_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window6_2)
        self.statusbar.setObjectName("statusbar")
        Window6_2.setStatusBar(self.statusbar)

        self.retranslateUi(Window6_2)
        QtCore.QMetaObject.connectSlotsByName(Window6_2)

    def retranslateUi(self, Window6_2):
        _translate = QtCore.QCoreApplication.translate
        Window6_2.setWindowTitle(_translate("Window6_2", "MainWindow"))
        self.textEdit.setHtml(_translate("Window6_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">BestBooking</span></p></body></html>"))
        self.textEdit_7.setHtml(_translate("Window6_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Skema</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Kurser</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Eksamen</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">KU/DTU mail</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Selvbetjening</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Studieinformation</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Hjælp</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Om KU</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Om DTU</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Nyhedsrum</p></body></html>"))
        self.textEdit_8.setHtml(_translate("Window6_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Søg...</p></body></html>"))
        self.textEdit_10.setHtml(_translate("Window6_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Du er her:   Skema   -  BestBooking</p></body></html>"))
        self.textEdit_4.setHtml(_translate("Window6_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#000000;\">Log af</span></p></body></html>"))
        self.pushButton.setText(_translate("Window6_2", "Annullér"))
        self.pushButton_2.setText(_translate("Window6_2", "Godkend"))
        self.textEdit_3.setHtml(_translate("Window6_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Du er ved at slette &quot;4, SAU, d. 01-04-2022, 09:15-10:00, KU, 210&quot;</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Er du sikker?</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window6_2 = QtWidgets.QMainWindow()
    ui = Ui_Window6_2()
    ui.setupUi(Window6_2)
    Window6_2.show()
    sys.exit(app.exec())
