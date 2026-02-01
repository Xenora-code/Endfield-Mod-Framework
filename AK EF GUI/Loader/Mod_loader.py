import json
import os

MODS_DIR = "mods"

def load_mods():
    mods = []
    if not os.path.exists(MODS_DIR):
        return mods

    for mod_name in os.listdir(MODS_DIR):
        mod_path = os.path.join(MODS_DIR, mod_name, "mod.json")
        if os.path.isfile(mod_path):
            with open(mod_path, "r", encoding="utf-8") as f:
                mods.append(json.load(f))
    return mods
