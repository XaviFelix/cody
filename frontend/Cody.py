from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from components import ClearButton, EnterButton, InputBox, DisplayBox, CopyButton, PasteButton

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

        # TODO: Now i need to pass a ref to the display so that i can display the 
        #       information
        self.enter_button = EnterButton("Enter", self.input_field, self.display_field)
        self.clear_button = ClearButton("Clear", self.input_field)
        self.paste_button = PasteButton("Paste", self.input_field)
        self.copy_button = CopyButton("Copy", self.input_field)

        # horizontal layout 
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.enter_button)
        horizontal_layout.addWidget(self.clear_button)
        horizontal_layout.addWidget(self.copy_button)
        horizontal_layout.addWidget(self.paste_button)

        # add widgets to the main layout
        self.vertical_layout.addWidget(self.display_field)
        self.vertical_layout.addWidget(self.input_field)
        self.vertical_layout.addLayout(horizontal_layout)
        self.setLayout(self.vertical_layout)