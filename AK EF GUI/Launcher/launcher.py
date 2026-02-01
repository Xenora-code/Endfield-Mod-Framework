import subprocess
from loader.mod_loader import load_mods

GAME_EXE = "ArknightsEndfield.exe"

def launch_game():
    mods = load_mods()
    print(f"Loaded {len(mods)} mods")

    for mod in mods:
        print(f"- {mod['name']} v{mod['version']}")

    subprocess.Popen([GAME_EXE])

if __name__ == "__main__":
    launch_game()
