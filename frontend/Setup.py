import sys
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout

class Setup(QWidget):
    def __init__(self):
        super().__init__()
        self.comboBox = QComboBox()
        self.comboBox.addItems(["Java", "Python", "Go", "Rust", "C"])

        vLayout = QVBoxLayout()
        vLayout.addWidget(self.comboBox)
        self.setLayout(vLayout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Setup()
    window.show()
    sys.exit(app.exec())