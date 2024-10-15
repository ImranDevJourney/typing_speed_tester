# src/app.py

import sys
from PyQt5.QtWidgets import QApplication
from src.base_typing_test import BaseTypingTestWindow  # Import the base class

class MainWindow(BaseTypingTestWindow):
    pass  # Inherits all functionality from BaseTypingTestWindow

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()