from PyQt6.QtWidgets import QMainWindow, QTabWidget
from davinci import DaVinci
from LabelÜbung import EchoMode


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Test")

        self.myCentralWidget = EchoMode()
        self.setCentralWidget(self.myCentralWidget)


