from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit
from PyQt6.QtGui import QFont
import sys

class InputBox(QTextEdit):
    def __init__(self):
        super().__init__()

        # Figure out if this works
        self.setLineWrapMode(self.LineWrapMode.WidgetWidth)

        # Set up the font here:
        self.font = QFont("Arial", 16)
        self.setFont(self.font)


# Demo
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("GeneralButton Demo")
    layout = QVBoxLayout(window)
    
    # Create an instance of GeneralButton with your custom text
    btn = InputBox()
    layout.addWidget(btn)
    
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())