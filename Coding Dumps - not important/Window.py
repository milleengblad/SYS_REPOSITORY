from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import sys
from PyQt6.QtGui import QIcon, QFont

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BestBooking")
        self.setWindowIcon(QIcon("qt.png"))

        self.setGeometry(500, 300, 400, 300)
        self.setStyleSheet('background-color:blue')

        self.create_widgets()


    def create_widgets(self):
        btn = QPushButton("Login", self)
        btn.setGeometry(100,100,100,100)
        btn.setStyleSheet('background-color:white')
        btn.setIcon(QIcon('football.png'))
        btn.clicked.connect(self.clicked_btn)

        self.label = QLabel("My Label", self)
        self.label.move(100,200)
        self.label.setStyleSheet('color:green')
        self.label.setFont(QFont("Times New Roman", 15))

    def clicked_btn(self):
        self.label.setText("Text is changed")
        self.label.setStyleSheet('background-color:red')


app = QApplication([])
window = window()
window.show()
sys.exit(app.exec())