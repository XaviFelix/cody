from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from components import ClearButton, EnterButton, InputBox, DisplayBox

class Cody(QWidget):
    def __init__(self):
        super().__init__()
        self.createUI()


    def createUI(self):
        # vertical layout
        self.vertical_layout = QVBoxLayout()

        # components
        self.input_field = InputBox()
        self.input_field.setPlaceholderText("Enter some text here...")
        self.display_field = DisplayBox()

        self.enter_button = EnterButton("Enter")
        self.clear_button = ClearButton("Clear")

        # horizontal layout 
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.enter_button)
        horizontal_layout.addWidget(self.clear_button)

        # add widgets to the main layout
        self.vertical_layout.addWidget(self.display_field)
        self.vertical_layout.addWidget(self.input_field)
        self.vertical_layout.addLayout(horizontal_layout)
        self.setLayout(self.vertical_layout)

        # connect signals
        self.enter_button.clicked.connect(self.handleEnter)
        self.clear_button.clicked.connect(self.handleClear)

    def handleEnter(self):
        text = self.input_field.toPlainText()
        self.display_field.setText(text)

    def handleClear(self):
        self.display_field.clear()
        self.input_field.clear()