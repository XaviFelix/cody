# frontend/main_window.py
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from components import ClearButton, EnterButton, InputBox


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
        self.input_field.setPlaceholderText("Enter some text here...") # Keep an eye here
        
        # This needs to be its own class
        self.enter_button = EnterButton("Enter") 
        self.clear_button = ClearButton("Clear")

        # Set up the horizontal Layout
        horizontal_layout.addWidget(self.enter_button)
        horizontal_layout.addWidget(self.clear_button)
   

        # Add widgets to the layout
        vertical_layout.addWidget(self.input_field)
        vertical_layout.addLayout(horizontal_layout)

        central_widget.setLayout(vertical_layout)

        # Set the central widget of the window
        self.setCentralWidget(central_widget)
