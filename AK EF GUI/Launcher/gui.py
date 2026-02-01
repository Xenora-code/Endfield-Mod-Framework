import sys
import subprocess
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QListWidget, QPushButton, QMessageBox
)
from loader.mod_loader import load_mods

GAME_EXE = "ArknightsEndfield.exe"

class LauncherUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Endfield Mod Launcher")
        self.setFixedSize(420, 520)

        layout = QVBoxLayout()

        title = QLabel("Endfield Mod Framework")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.mod_list = QListWidget()
        layout.addWidget(self.mod_list)

        self.launch_button = QPushButton("Launch Game")
        self.launch_button.clicked.connect(self.launch_game)
        layout.addWidget(self.launch_button)

        self.setLayout(layout)
        self.load_mods()

    def load_mods(self):
        mods = load_mods()
        for mod in mods:
            self.mod_list.addItem(f"{mod['name']} v{mod['version']}")

    def launch_game(self):
        try:
            subprocess.Popen([GAME_EXE])
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Game executable not found!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LauncherUI()
    window.show()
    sys.exit(app.exec())
