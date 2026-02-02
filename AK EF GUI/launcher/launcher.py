import os
import subprocess
from loader.mod_loader import load_mods
from loader.lua_sandbox import run_lua_script
from launcher.game_path import get_game_exe

def launch_game():
    game_exe = get_game_exe()
    if not game_exe:
        print("Game not found")
        return

    mods = load_mods()

    for mod in mods:
        if mod["enabled"] and "entry" in mod:
            script = os.path.join("mods", mod["folder"], mod["entry"])
            if os.path.exists(script):
                run_lua_script(script)

    subprocess.Popen([game_exe])

if __name__ == "__main__":
    launch_game()
