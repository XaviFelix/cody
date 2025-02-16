import sys
from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QGridLayout
from components import GroupCheckBoxes

class Setup(QWidget):
    def __init__(self):
        super().__init__()
        self.comboBox = QComboBox()
        self.comboBox.addItems(["Java", "Python", "Go", "Rust", "C"])

        self.gridLayout = QGridLayout()
        
        #NOTE: Need to update this everytime i create a new group of checkboxes
        # widget, row, column 
        self.gridLayout.addWidget(self.comboBox, 0, 0)

        # This is the default
        self.createJavaPrinciples()

        # comboBox signal
        self.comboBox.activated.connect(self.initLanguagePrinciples)

        self.setLayout(self.gridLayout)


    def initLanguagePrinciples(self):
        index = self.comboBox.currentIndex() 
        currentLanguage = self.comboBox.itemText(index)

        match currentLanguage:
            case "Java":
                self.createJavaPrinciples()
            case "Python":
                self.createPythonPrinciples()
            case "Go":
                self.createGoPrinciples()
            case "Rust":
                self.createRustPrinciples()
            case "C":
                self.createCPrinciples()
            case _:
                print("Something went wrong initalizing principles")
    
    def createPythonPrinciples(self):
        print("Creating Python principles")
        self.clearGridLayout()

        basics = [
            "Syntax and Structure", 
            "Control Flow", 
            "Methods and Functions", 
            "Exception Handling"
        ]

        oop = [
            "Classes and Objects", 
            "Encapsulation", 
            "Inheritance", 
            "Polymorphism",
            "Abstraction"
        ]

        collectionsAndDS= [
            "List & Tuples", 
            "Dictionaries & Sets", 
            "Iterators & Generators", 
            "Built-in Collections"
        ]

        features = [
            "Concurrency & Multithreading", 
            "I/O & Serialization", 
            "Functional Programming", 
            "Typing & Type Hints",
            "Memory Management & Performance"
        ]

        self.gridLayout.addWidget(GroupCheckBoxes(basics, "Core Python Basics"), 1, 0)
        self.gridLayout.addWidget(GroupCheckBoxes(oop, "OOP"), 1, 1)
        self.gridLayout.addWidget(GroupCheckBoxes(collectionsAndDS, "DS & Collections"), 2, 0)
        self.gridLayout.addWidget(GroupCheckBoxes(features, "Python Features"), 2, 1)

    def createJavaPrinciples(self):
        print("Creating Java principles")
        self.clearGridLayout()

        basics = [
            "Syntax and Structure", 
            "Control Flow", 
            "Methods and Functions", 
            "Exception Handling"
        ]

        oop = [
            "Classes and Objects", 
            "Encapsulation", 
            "Inheritance", 
            "Polymorphism",
            "Abstraction"
        ]

        collectionsAndDS= [
            "Arrays", 
            "Collections Framework", 
            "Common Implementations", 
            "Iterators & Streams"
        ]

        features = [
            "Concurrency & Multithreading", 
            "I/O & File Handling", 
            "Lambdas & Functional Programming", 
            "Generics & Type Safety",
            "JVM & Memory Management"
        ]

        self.gridLayout.addWidget(GroupCheckBoxes(basics, "Core Java Basics"), 1, 0)
        self.gridLayout.addWidget(GroupCheckBoxes(oop, "OOP"), 1, 1)
        self.gridLayout.addWidget(GroupCheckBoxes(collectionsAndDS, "DS & Collections"), 2, 0)
        self.gridLayout.addWidget(GroupCheckBoxes(features, "Java Features"), 2, 1)

    def createGoPrinciples(self):
        print("Creating Go principles")

    def createRustPrinciples(self):
        print("Creating Rust principles")
        self.clearGridLayout()

        basics = [
            "Syntax and Structure", 
            "Control Flow", 
            "Functions", 
            "Error Handling"
        ]

        oop = [
            "Ownership Rules", 
            "Borrowing & References", 
            "Lifetimes", 
            "Smart Pointers",
        ]

        collectionsAndDS= [
            "Arrays & Slices", 
            "Tuples & Structs", 
            "Vectors & Hashmaps", 
            "Iterators & Closures"
        ]

        features = [
            "Concurrency & Parallelism", 
            "Traits and Generics", 
            "Macros & Metaprogramming", 
            "Unsafe Rust & Low-Level Control",
            "I/O & File Management"
        ]

        self.gridLayout.addWidget(GroupCheckBoxes(basics, "Core Rust Basics"), 1, 0)
        self.gridLayout.addWidget(GroupCheckBoxes(oop, "Ownership, Borrowing & Lifetimes"), 1, 1)
        self.gridLayout.addWidget(GroupCheckBoxes(collectionsAndDS, "Data Structures & Collections"), 2, 0)
        self.gridLayout.addWidget(GroupCheckBoxes(features, "Rust Features"), 2, 1)

    def createCPrinciples(self):
        print("Creating C principles")


    def clearGridLayout(self):
        for i in reversed(range(self.gridLayout.count())):
            if i == 0:
                break
            self.gridLayout.itemAt(i).widget().setParent(None)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Setup()
    window.show()
    sys.exit(app.exec())