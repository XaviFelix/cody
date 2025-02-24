from PyQt6.QtWidgets import QPushButton
from .InputBox import InputBox
from .DisplayBox import DisplayBox
from dotenv import load_dotenv
from backend import callLLM
import os

class EnterButton(QPushButton):
    def __init__(self, label: str, inputBox: InputBox, displayBox: DisplayBox):
        super().__init__(label)
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = os.getenv("BASE_URL")
        self.prime = os.getenv("PROMPT_PRIME")

        # Get ref to input field and create message history
        self.input_field = inputBox
        self.messages = [
            {"role": "system", "content": self.prime}
        ]

        # Get ref to display field and display it
        self.displayBox = displayBox

        # set up connection
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
        user_input = self.input_field.getInput()
        callLLM(user_input, self.messages, self.api_key, self.base_url, self.displayBox)


   