import sys
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QMenuBar
from src.base_typing_test import BaseTypingTestWindow  # Import the base class
from ui.dialogs.settings_dialog import Ui_SettingsDialog


class MainWindow(BaseTypingTestWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Initialize QSettings for saving user preferences
        self.settings = QSettings("YourCompany", "TypingSpeedTester")

        # Load previously saved settings
        self.load_settings()

        # Create a menu bar and add settings action
        menubar = QMenuBar(self)
        settings_menu = menubar.addMenu("Settings")

        action_settings = settings_menu.addAction("Open Settings")
        action_settings.triggered.connect(self.open_settings_dialog)

        self.setMenuBar(menubar)  # Set the menu bar

    def load_settings(self):
        """Load settings from QSettings."""
        font_size = self.settings.value("fontSize", "Medium")  # Default to Medium
        difficulty_level = self.settings.value("difficultyLevel", "Easy")  # Default to Easy

        # Set UI elements according to loaded settings
        self.apply_font_size(font_size)

    def apply_font_size(self, font_size):
        """Apply font size to relevant UI elements."""
        font_size_map = {
            "Small": 10,
            "Medium": 14,
            "Large": 18
        }

        selected_font_size = font_size_map.get(font_size, 14)  # Default to Medium if not found
        new_font = self.ui.textToType.font()
        new_font.setPointSize(selected_font_size)

        # Apply the new font size to relevant UI elements
        self.ui.textToType.setFont(new_font)
        self.ui.inputField.setFont(new_font)
        self.ui.resultLabel.setFont(new_font)

    def open_settings_dialog(self):
        """Open the settings dialog."""
        settings_dialog = QDialog(self)  # Create a QDialog instance
        ui_settings = Ui_SettingsDialog()  # Create the UI instance
        ui_settings.setupUi(settings_dialog)  # Set up the UI on the dialog

        # Connect signals for save and cancel actions
        ui_settings.saveButton.clicked.connect(lambda: self.save_settings(ui_settings, settings_dialog))
        ui_settings.cancelButton.clicked.connect(settings_dialog.reject)  # Connect cancel button

        settings_dialog.exec_()  # Show dialog modally

    def save_settings(self, ui_settings, dialog):
        """Save settings from the dialog."""
        try:
            font_size = ui_settings.fontSizeComboBox.currentText()  # Access combo box from ui_settings
            difficulty_level = ui_settings.difficultyComboBox.currentText()  # Get difficulty level

            # Save settings using QSettings
            self.settings.setValue("fontSize", font_size)
            self.settings.setValue("difficultyLevel", difficulty_level)

            QMessageBox.information(self, "Settings Saved", f"Font Size: {font_size}, Difficulty: {difficulty_level}")

            dialog.accept()  # Close the dialog
            self.apply_font_size(font_size)  # Apply new font size immediately

        except Exception as e:
            QMessageBox.critical(self, "Error Saving Settings", f"An error occurred: {str(e)}")

def main():
    app = QApplication(sys.argv)
    # Set global stylesheet
    app.setStyleSheet("""
        QPushButton {
            background-color: lightgray;
            color: black;
            font-size: 14px;
            border-radius: 5px; /* Rounded corners */
        }
        QPushButton:hover {
            background-color: darkgray; /* Change color on hover */
        }
        QLabel {
            font-size: 16px;
            color: #333; /* Dark text color */
        }
        QPushButton:pressed {
            background-color: #3e8e41; /* Darker green when pressed */
        }
    """)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()