# src/settings_dialog.py

from PyQt5.QtWidgets import QDialog
from ui.dialogs.settings_dialog import Ui_SettingsDialog


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)

        # Connect signals
        self.ui.saveButton.clicked.connect(self.save_settings)
        self.ui.cancelButton.clicked.connect(self.reject)

    def save_settings(self):
        """Save the selected settings."""
        font_size = self.ui.fontSizeComboBox.currentText()
        difficulty = self.ui.difficultyComboBox.currentText()

        # Here you can implement logic to save these settings
        # For now, we'll just print them to the console
        print(f"Font Size: {font_size}, Difficulty: {difficulty}")

        # Close the dialog
        self.accept()