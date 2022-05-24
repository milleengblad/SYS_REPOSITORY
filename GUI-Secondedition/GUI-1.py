import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QDialog, QApplication, QWidget, QMainWindow

class GUIvindue1(QMainWindow):
    def __init__(self):
        super(GUIvindue1, self).__init__()
        loadUi("GUIvindue1.ui", self)