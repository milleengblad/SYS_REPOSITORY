

from PyQt6 import QtCore, QtGui, QtWidgets
from GUIvindue4 import Ui_Window4


class Ui_Vindue3_2(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window4()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Vindue3_2):
        Vindue3_2.setObjectName("Vindue3_2")
        Vindue3_2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Vindue3_2)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, -10, 801, 561))
        self.textEdit.setObjectName("textEdit")
        self.Vindue3 = QtWidgets.QTextEdit(self.centralwidget)
        self.Vindue3.setGeometry(QtCore.QRect(0, 0, 801, 121))
        self.Vindue3.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.Vindue3.setObjectName("Vindue3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 470, 801, 91))
        self.textEdit_3.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(10, 130, 121, 31))
        self.textEdit_6.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(150, 170, 401, 31))
        self.textEdit_7.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(150, 200, 401, 111))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(160, 220, 291, 71))
        self.textEdit_9.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.textEdit_9.setObjectName("textEdit_9")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(420, 220, 31, 31))
        self.commandLinkButton.setText("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.textEdit_10 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(150, 130, 401, 31))
        self.textEdit_10.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(560, 170, 231, 31))
        self.textEdit_11.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(560, 200, 231, 251))
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_13.setGeometry(QtCore.QRect(150, 320, 401, 31))
        self.textEdit_13.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_14.setGeometry(QtCore.QRect(150, 350, 401, 61))
        self.textEdit_14.setObjectName("textEdit_14")


        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())


        self.pushButton_1.setGeometry(QtCore.QRect(10, 160, 121, 31))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 190, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 220, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 250, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 280, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 310, 121, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 340, 121, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 370, 121, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 400, 121, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(670, 130, 121, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        Vindue3_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Vindue3_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Vindue3_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Vindue3_2)
        self.statusbar.setObjectName("statusbar")
        Vindue3_2.setStatusBar(self.statusbar)

        self.retranslateUi(Vindue3_2)
        QtCore.QMetaObject.connectSlotsByName(Vindue3_2)

    def retranslateUi(self, Vindue3_2):
        _translate = QtCore.QCoreApplication.translate
        Vindue3_2.setWindowTitle(_translate("Vindue3_2", "MainWindow"))
        self.Vindue3.setHtml(_translate("Vindue3_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:24pt; font-weight:700; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">BestBooking</span></p></body></html>"))
        self.textEdit_6.setHtml(_translate("Vindue3_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Søg...</p></body></html>"))
        self.textEdit_7.setHtml(_translate("Vindue3_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Mine Portaler</span></p></body></html>"))
        self.textEdit_9.setHtml(_translate("Vindue3_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">BACHELOR I SUNDHED OG INFORMATIK                 </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">                </span></p></body></html>"))
        self.textEdit_10.setHtml(_translate("Vindue3_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Du er her:   Forside   &gt;   BestBooking</p></body></html>"))
        self.textEdit_11.setHtml(_translate("Vindue3_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">NYHEDER</span></p></body></html>"))
        self.textEdit_12.setHtml(_translate("Vindue3_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Dato: 09.03.2022</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">KU-astronomer har fundet 6 fjerne galakser, som er døde på mystisk vis </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Astronomer fra bl.a. Københavns Universitet og DTU har kigget 10-12 milliarder år ud i universet og...</p></body></html>"))
        self.textEdit_13.setHtml(_translate("Vindue3_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">STUDIEBESKEDER</span></p></body></html>"))
        self.textEdit_14.setHtml(_translate("Vindue3_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Uddannelser og studerende / 09-03-2022</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SU-aktivitetskontrol i marts - forstå reglerne</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_1.setText(_translate("Vindue3_2", "Skema"))
        self.pushButton_2.setText(_translate("Vindue3_2", "Kurser"))
        self.pushButton_3.setText(_translate("Vindue3_2", "Eksamen"))
        self.pushButton_4.setText(_translate("Vindue3_2", "KU/DTU mail"))
        self.pushButton_5.setText(_translate("Vindue3_2", "Selvbetjening"))
        self.pushButton_6.setText(_translate("Vindue3_2", "Studieinformation"))
        self.pushButton_7.setText(_translate("Vindue3_2", "Hjælp"))
        self.pushButton_8.setText(_translate("Vindue3_2", "Om KU"))
        self.pushButton_9.setText(_translate("Vindue3_2", "Om DTU"))
        self.pushButton_10.setText(_translate("Vindue3_2", "Log af"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Vindue3_2 = QtWidgets.QMainWindow()
    ui = Ui_Vindue3_2()
    ui.setupUi(Vindue3_2)
    Vindue3_2.show()
    sys.exit(app.exec())
