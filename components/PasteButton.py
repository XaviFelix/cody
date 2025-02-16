from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from .InputBox import InputBox
import sys

class PasteButton(QPushButton):
    def __init__(self, label: str, inputBox: InputBox, parent=None):
        super().__init__(label, parent)

        self.setToolTip("Paste")
        self.clicked.connect(self.pasteInput)

    def handlePaste(self): 
        print("Pasting from clipboard")



# Just to test the individual object:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("GeneralButton Demo")
    layout = QVBoxLayout(window)
    
    btn = PasteButton("Paste")
    layout.addWidget(btn)
    
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())
