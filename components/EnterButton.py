from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from .InputBox import InputBox
import sys

class EnterButton(QPushButton):
    def __init__(self, label: str, inputBox: InputBox, parent=None):
        super().__init__(label, parent)

        self.input_field = inputBox

        self.setToolTip("press enter")
        self.clicked.connect(self.handleEnter)

        # Test later:
        # self.setStyleSheet("""
        #     QPushButton {
        #         background-color: #4CAF50;
        #         color: white;              
        #         font-size: 16px;
        #         padding: 10px;
        #         border: none;
        #         border-radius: 5px;
        #     }
        #     QPushButton:hover {
        #         background-color: #45a049;  
        #     }
        #     QPushButton:pressed {
        #         background-color: #3e8e41; 
        #     }
        # """)

    def handleEnter(self):
        text = self.input_field.toPlainText()
        print("This is the text:")
        print(text)