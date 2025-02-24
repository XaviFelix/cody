from PyQt6.QtWidgets import QApplication, QPushButton
from .InputBox import InputBox

class PasteButton(QPushButton):
    def __init__(self, label: str, inputBox: InputBox, parent=None):
        super().__init__(label, inputBox)

        self.inputBox = inputBox
        self.setToolTip("Paste")

        self.clicked.connect(self.handlePaste)

    def handlePaste(self): 
        print("Pasting from clipboard")

        clipboard = QApplication.clipboard()
        self.inputBox.insertPlainText(clipboard.text())