from PyQt6.QtWidgets import QApplication, QTextEdit 
from PyQt6.QtGui import QFont
import sys

class DisplayBox(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Display text example")
        self.setReadOnly(True)
        self.font = QFont("Arial", 16)
        self.setFont(self.font)



    def updateDisplay(self):
        self.setText("Welcome!")
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DisplayBox()
    demo.show()
    sys.exit(app.exec())