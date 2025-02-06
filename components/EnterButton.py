from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys

class EnterButton(QPushButton):
    def __init__(self, label: str, parent=None):
        super().__init__(label, parent)

        self.setToolTip("press enter")
        self.clicked.connect(self.displayMessage)
        self.clicked.connect(self.handleEnter)


    def displayMessage(self):
        print("Enter button has been pressed")

    def handleEnter(self):
        print("random")
        # Here i need to get the data from the QLineEdit object


# Just to test the individual object:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("GeneralButton Demo")
    layout = QVBoxLayout(window)
    
    # Create an instance of GeneralButton with your custom text
    btn = EnterButton("Enter")
    layout.addWidget(btn)
    
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())