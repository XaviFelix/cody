from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QFont

class InputBox(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setLineWrapMode(self.LineWrapMode.WidgetWidth)

        self.font = QFont("Arial", 16)
        self.setFont(self.font)
    
    def getInput(self):
        return self.toPlainText()