# src/base_typing_test.py

from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog

from src.settings_dialog import SettingsDialog
from ui.main_window import Ui_MainWindow
from src.typing_test import TypingTest
from src.results import Results  # Import results management
from ui.results_window import Ui_ResultsWindow
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve

class BaseTypingTestWindow(QMainWindow):
    def __init__(self):
        super(BaseTypingTestWindow, self).__init__()

        # Set up the UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Call retranslateUi to set button texts
        self.ui.retranslateUi(self)

        # Initialize Typing Test Logic and Results Management
        self.typing_test = TypingTest()
        self.results = Results()

        # Connect buttons to methods
        self.ui.startButton.clicked.connect(self.start_typing_test)
        self.ui.submitButton.clicked.connect(self.submit_typing_test)
        self.ui.inputField.returnPressed.connect(self.submit_typing_test)

        # Connect settings action to method
        self.ui.actionSettings.triggered.connect(self.open_settings_dialog)

        # Set specific styles for buttons
        self.ui.startButton.setStyleSheet("background-color: lightblue; color: black;")
        self.ui.submitButton.setStyleSheet("background-color: lightgreen; color: black;")

        # Connect button animation
        self.ui.startButton.clicked.connect(self.animate_button)

    def animate_button(self):
        animation = QPropertyAnimation(self.ui.startButton, b"geometry")
        animation.setDuration(500)  # Duration in milliseconds
        animation.setStartValue(self.ui.startButton.geometry())
        animation.setEndValue(self.ui.startButton.geometry().adjusted(0, -10, 0, 0))  # Move up by 10 pixels
        animation.setEasingCurve(QEasingCurve.OutBounce)  # Easing curve for a bounce effect
        animation.start()

    def open_settings_dialog(self):
        """Open the settings dialog."""
        settings_dialog = SettingsDialog(self)
        if settings_dialog.exec_() == QDialog.Accepted:
            # Here you can handle any updates based on user settings if needed
            pass

    def start_typing_test(self):
        """Start the typing test."""
        self.typing_test.start_test()
        self.ui.textToType.setText(self.typing_test.current_sentence)
        self.ui.resultLabel.clear()
        self.ui.inputField.clear()
        self.ui.inputField.setFocus()  # Ensure focus is on input field

    def submit_typing_test(self):
        """Submit the typed text and calculate results."""
        user_input = self.ui.inputField.text()

        if user_input:
            wpm, error_message = self.typing_test.check_typing(user_input)

            if wpm is not None:
                self.results.add_result(wpm)  # Add result to Results class

                # Display current speed and average speed
                average_wpm = self.results.get_average_wpm()
                all_results = self.results.display_results()  # Get all results

                # Show results in a dialog
                self.show_results_window(wpm, average_wpm, all_results)
            else:
                self.ui.resultLabel.setText(f"Try again! Errors: {error_message}")
        else:
            QMessageBox.warning(self, "Input Error", "Please type something before submitting.")

    def show_results_window(self, wpm, average_wpm, all_results):
        """Open a dialog to display results."""
        results_dialog = QDialog(self)
        ui_results = Ui_ResultsWindow()
        ui_results.setupUi(results_dialog)

        # Set the results text
        ui_results.resultsLabel.setText(
            f"Your speed: {wpm:.2f} WPM\nAverage speed: {average_wpm:.2f} WPM\n\nAll Results:\n{all_results}"
        )

        # Connect close button
        ui_results.closeButton.clicked.connect(results_dialog.accept)

        results_dialog.exec_()  # Show dialog modally