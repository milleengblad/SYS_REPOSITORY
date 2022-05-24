

from PyQt6 import QtCore, QtGui, QtWidgets
from GUIvindue2 import Ui_Window2_2


class Ui_Window1_2(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window2_2()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Window1_2):
        Window1_2.setObjectName("Window1_2")
        Window1_2.resize(804, 510)
        self.centralwidget = QtWidgets.QWidget(Window1_2)
        self.centralwidget.setObjectName("centralwidget")
        self.Window1 = QtWidgets.QGraphicsView(self.centralwidget)
        self.Window1.setGeometry(QtCore.QRect(-110, -40, 1101, 881))
        self.Window1.setObjectName("Window1")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 801, 111))
        self.textBrowser.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.textBrowser.setObjectName("textBrowser")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(670, 450, 61, 31))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(730, 450, 71, 31))
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 450, 131, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 480, 801, 71))
        self.textEdit.setStyleSheet("background-color: rgb(148, 17, 0);")
        self.textEdit.setObjectName("textEdit")


        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openWindow())


        self.pushButton_4.setGeometry(QtCore.QRect(350, 310, 141, 31))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 270, 141, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(350, 230, 141, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 350, 221, 31))
        self.label.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 370, 331, 61))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(300, 180, 231, 31))
        self.textBrowser_2.setStyleSheet("background-color: rgb(169, 169, 169);")
        self.textBrowser_2.setObjectName("textBrowser_2")
        Window1_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window1_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        Window1_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window1_2)
        self.statusbar.setObjectName("statusbar")
        Window1_2.setStatusBar(self.statusbar)

        self.retranslateUi(Window1_2)
        QtCore.QMetaObject.connectSlotsByName(Window1_2)

    def retranslateUi(self, Window1_2):
        _translate = QtCore.QCoreApplication.translate
        Window1_2.setWindowTitle(_translate("Window1_2", "MainWindow"))
        self.textBrowser.setHtml(_translate("Window1_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">BestBooking</span></p></body></html>"))
        self.commandLinkButton.setText(_translate("Window1_2", "Gæst  "))
        self.commandLinkButton_2.setText(_translate("Window1_2", "Hjælp"))
        self.pushButton_5.setText(_translate("Window1_2", "Select Language"))
        self.pushButton_4.setText(_translate("Window1_2", "Underviser"))
        self.pushButton_6.setText(_translate("Window1_2", "Administrativ"))
        self.pushButton_7.setText(_translate("Window1_2", "Studerende"))
        self.textBrowser_2.setHtml(_translate("Window1_2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Vælg login metode </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window1_2 = QtWidgets.QMainWindow()
    ui = Ui_Window1_2()
    ui.setupUi(Window1_2)
    Window1_2.show()
    sys.exit(app.exec())
