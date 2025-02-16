import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QCheckBox, QGroupBox

class GroupCheckBoxes(QGroupBox):
    def __init__(self, listOfCheckBoxNames, principles): # pass a string named, principle
        super().__init__(principles) # We need to let this be passed by the instance creation
        self.setCheckable(True)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(1)
        self.layout.setContentsMargins(5, 5, 5, 5)

        self.check_boxes = []
        for name in listOfCheckBoxNames:
            checkbox = QCheckBox(name)
            checkbox.stateChanged.connect(self.on_checkbox_state_changed)
            self.layout.addWidget(checkbox)
            self.check_boxes.append(checkbox)

        self.setLayout(self.layout)

    #TODO These checkboxes will trigger the backend 
    def on_checkbox_state_changed(self, state):
        selected_options = [cb.text() for cb in self.check_boxes if cb.isChecked()]
        if selected_options:
            print("Hello there")
        else:
            print("No options selected")

        
# using for testing this component
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GroupCheckBoxes(["Syntax and Semantics", "Datatypes and Semantics", "Control Flow", "Functions and Scope"], "Hello")
    window.show()
    sys.exit(app.exec())