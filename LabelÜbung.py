import PyQt6
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent, QPaintEvent, QPainter
from PyQt6.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit


class EchoMode(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(600, 500)

        layoutWidget = QGridLayout(self)

        self.le1 = QLineEdit()
        self.le1.setEchoMode(QLineEdit.EchoMode.Normal)
        layoutWidget.addWidget(self.le1)

        self.le2 = QLineEdit()
        self.le2.setEchoMode(QLineEdit.EchoMode.NoEcho)
        layoutWidget.addWidget(self.le2)

        self.le3 = QLineEdit()
        self.le3.setEchoMode(QLineEdit.EchoMode.Password)
        layoutWidget.addWidget(self.le3)

        self.le4 = QLineEdit()
        self.le4.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        layoutWidget.addWidget(self.le4)

        self.setLayout(layoutWidget)
