from PyQt6.QtWidgets import QApplication, QTextEdit 
from PyQt6.QtGui import QFont

class DisplayBox(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Display text example")
        self.setReadOnly(True)
        self.font = QFont("Arial", 16)
        self.setFont(self.font)

    def updateDisplay(self, completion):
        self.setText(completion)