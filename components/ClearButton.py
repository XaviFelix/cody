from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from .InputBox import InputBox
import sys

class ClearButton(QPushButton):
    def __init__(self, label: str, inputBox: InputBox, parent=None):
        super().__init__(label, inputBox)

        self.inputBox = inputBox

        self.setToolTip("Clear Input")
        self.clicked.connect(self.handleClear)

    def handleClear(self):
        self.inputBox.clear()
        