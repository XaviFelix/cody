from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget
from .Cody import Cody
from .Setup import Setup

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cody")

        self.tabs = QTabWidget()
        self.cody_tab = Cody()
        self.setup = Setup()

        self.tabs.addTab(self.cody_tab, "Cody")
        self.tabs.addTab(self.setup, "Setup")
        self.setCentralWidget(self.tabs)