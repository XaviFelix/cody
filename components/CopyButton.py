from PyQt6.QtWidgets import QApplication, QPushButton
from .InputBox import InputBox
import sys

class CopyButton(QPushButton):
    def __init__(self, label: str, inputBox: InputBox, parent=None):
        super().__init__(label, inputBox)

        self.inputBox = inputBox

        self.setToolTip("Copy Text")
        self.clicked.connect(self.handleCopy) # I don't really need this unless i am testing here


    # Test this behavior
    def handleCopy(self):
        # Add a functionality to where if the text is empty
        # Then it won't copy to the clipboard
        clipboard= QApplication.clipboard()
        clipboard.setText(self.inputBox.toPlainText())
