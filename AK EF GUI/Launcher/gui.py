import sys
import subprocess
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QListWidget, QListWidgetItem,
    QPushButton, QMessageBox
)
from loader.mod_loader import load_mods, save_enabled_config
from launcher.game_path import get_game_exe
from loader.mod_updater import update_all

class LauncherUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Endfield Mod Launcher")
        self.setFixedSize(460, 600)

        self.mods = []

        layout = QVBoxLayout()

        title = QLabel("Endfield Mod Framework")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(title)

        self.mod_list = QListWidget()
        self.mod_list.itemChanged.connect(self.save_mod_states)
        layout.addWidget(self.mod_list)

        self.update_button = QPushButton("Update Mods")
        self.update_button.clicked.connect(self.update_mods)
        layout.addWidget(self.update_button)

        self.launch_button = QPushButton("Launch Game")
        self.launch_button.clicked.connect(self.launch_game)
        layout.addWidget(self.launch_button)

        self.setLayout(layout)
        self.load_mods()

    def load_mods(self):
        self.mods = load_mods()
        self.mod_list.clear()

        for mod in self.mods:
            item = QListWidgetItem(f"{mod['name']} v{mod['version']}")
            item.setCheckState(2 if mod["enabled"] else 0)
            self.mod_list.addItem(item)

    def save_mod_states(self):
        config = {}
        for i, mod in enumerate(self.mods):
            config[mod["folder"]] = self.mod_list.item(i).checkState() == 2
        save_enabled_config(config)

    def update_mods(self):
        updated = update_all(self.mods)
        if updated:
            QMessageBox.information(self, "Updates", "Updated:\n" + "\n".join(updated))
        else:
            QMessageBox.information(self, "Updates", "All mods are up to date.")
        self.load_mods()

    def launch_game(self):
        game_exe = get_game_exe()
        if not game_exe:
            QMessageBox.critical(self, "Error", "Game executable not found!")
            return
        subprocess.Popen([game_exe])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LauncherUI()
    window.show()
    sys.exit(app.exec())
