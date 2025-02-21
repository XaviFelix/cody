from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PyQt6.QtGui import QFont
import sys

class InputBox(QTextEdit):
    def __init__(self):
        super().__init__()
        self.setLineWrapMode(self.LineWrapMode.WidgetWidth)

        self.font = QFont("Arial", 16)
        self.setFont(self.font)
    
    def getInput(self):
        return self.toPlainText()




# Demo
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("GeneralButton Demo")
    layout = QVBoxLayout(window)
    
    btn = InputBox()
    layout.addWidget(btn)
    
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())