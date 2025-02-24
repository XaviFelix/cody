from PyQt6.QtWidgets import QApplication, QPushButton
from .InputBox import InputBox

class CopyButton(QPushButton):
    def __init__(self, label: str, inputBox: InputBox, parent=None):
        super().__init__(label, inputBox)

        self.inputBox = inputBox
        self.setToolTip("Copy Text")
        self.clicked.connect(self.handleCopy)

    def handleCopy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.inputBox.toPlainText())