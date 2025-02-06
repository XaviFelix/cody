from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys

class ClearButton(QPushButton):
    def __init__(self, label: str, parent=None):
        super().__init__(label, parent)

        self.setToolTip("Clear Input")
        self.clicked.connect(self.clearInput)

    def clearInput(self):
        print("Clearing Input")


# Just to test the individual object:
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("GeneralButton Demo")
    layout = QVBoxLayout(window)
    
    # Create an instance of GeneralButton with your custom text
    btn = ClearButton("Clear")
    layout.addWidget(btn)
    
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec())
