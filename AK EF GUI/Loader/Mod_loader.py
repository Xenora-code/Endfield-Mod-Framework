import json
import os

MODS_DIR = "mods"
CONFIG_FILE = "config/mods_enabled.json"

def load_enabled_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_enabled_config(config):
    os.makedirs("config", exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)

def load_mods():
    enabled = load_enabled_config()
    mods = []

    if not os.path.exists(MODS_DIR):
        return mods

    for mod_name in os.listdir(MODS_DIR):
        mod_path = os.path.join(MODS_DIR, mod_name, "mod.json")
        if os.path.isfile(mod_path):
            with open(mod_path, "r", encoding="utf-8") as f:
                mod = json.load(f)
                mod["folder"] = mod_name
                mod["enabled"] = enabled.get(mod_name, True)
                mods.append(mod)

    return mods
