import sys
from PyQt6.QtWidgets import QApplication
from frontend import MainWindow 

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(500, 700)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
