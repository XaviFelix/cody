from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from components import ClearButton, EnterButton, InputBox, DisplayBox, CopyButton

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

        # I need to pass the input_field here to the buttons so that 
        # THey can refernce it and do their respective methods
        self.enter_button = EnterButton("Enter", self.input_field)
        self.clear_button = ClearButton("Clear", self.input_field)
        # self.paste_button = PasteButton("Paste", self.input_field)
        self.copy_button = CopyButton("Copy", self.input_field)

        # horizontal layout 
        horizontal_layout = QHBoxLayout()
        horizontal_layout.addWidget(self.enter_button)
        horizontal_layout.addWidget(self.clear_button)
        horizontal_layout.addWidget(self.copy_button)

        # add widgets to the main layout
        self.vertical_layout.addWidget(self.display_field)
        self.vertical_layout.addWidget(self.input_field)
        self.vertical_layout.addLayout(horizontal_layout)
        self.setLayout(self.vertical_layout)

        # connect signals
        self.enter_button.clicked.connect(self.enter_button.handleEnter)
        self.clear_button.clicked.connect(self.clear_button.handleClear)
        # self.paste_button.clicked.connect(self.paste_button.handlePaste)
        self.copy_button.clicked.connect(self.copy_button.handleCopy)

    # def handleEnter(self):
    #     text = self.input_field.toPlainText()
    #     self.display_field.setText(text)

    # def handleClear(self):
    #     self.display_field.clear()
    #     self.input_field.clear()
    
    # def handlePaste(self):
    #     print("Finish this method")

    # def handleCopy(self):
    #     print("Finish this method")