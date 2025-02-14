import sys
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QGridLayout
from components import GroupCheckBoxes

class Setup(QWidget):
    def __init__(self):
        super().__init__()
        self.comboBox = QComboBox()
        self.comboBox.addItems(["Java", "Python", "Go", "Rust", "C"])

        # List of programming language topics (general),
        #TODO: curate topics specific to PL
        self.topics = [
            "Syntax and Semantics", 
            "Datatypes and Semantics", 
            "Control Flow", 
            "Functions and Scope"
        ]
        self.checkBoxes = GroupCheckBoxes(self.topics)
        self.checkBoxes2 = GroupCheckBoxes(self.topics)
        self.checkBoxes3 = GroupCheckBoxes(self.topics)
        self.checkBoxes4 = GroupCheckBoxes(self.topics)

        gridLayout = QGridLayout()
        
        # widget, row, column 
        gridLayout.addWidget(self.comboBox, 0, 0)
        gridLayout.addWidget(self.checkBoxes, 1, 0)
        gridLayout.addWidget(self.checkBoxes2, 1, 1)
        gridLayout.addWidget(self.checkBoxes3, 2, 0)
        gridLayout.addWidget(self.checkBoxes4, 2, 1)

        self.setLayout(gridLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Setup()
    window.show()
    sys.exit(app.exec())