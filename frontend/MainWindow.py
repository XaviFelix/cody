from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from components import ClearButton, EnterButton, InputBox, DisplayBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cody")
        self.createUI()

    def createUI(self):
        # Create a central widget and set a vertical layout
        central_widget = QWidget()
        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()

        # This needs to be its own class
        # Create the input field, button, and output label
        self.input_field = InputBox() # 
        self.input_field.setPlaceholderText("Enter some text here...")
        self.display_field = DisplayBox()
        
        # Buttons
        self.enter_button = EnterButton("Enter") 
        self.clear_button = ClearButton("Clear")

        # Set up the horizontal Layout
        horizontal_layout.addWidget(self.enter_button)
        horizontal_layout.addWidget(self.clear_button)
   

        # Add widgets to the main layout (vertical layout)
        vertical_layout.addWidget(self.display_field)
        vertical_layout.addWidget(self.input_field)
        vertical_layout.addLayout(horizontal_layout)
        central_widget.setLayout(vertical_layout)

        # Set the central widget of the window
        self.setCentralWidget(central_widget)

        # Signals go here:
        self.enter_button.clicked.connect(self.handleEnter)
        self.clear_button.clicked.connect(self.handleClear)


    def handleEnter(self):
        text = self.input_field.toPlainText()
        self.display_field.setText(text)

    def handleClear(self):
        self.display_field.clear()
        self.input_field.clear()

        # Display the text onto the display widget
