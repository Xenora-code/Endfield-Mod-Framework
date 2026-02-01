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

def load_all_mods():
    mods = {}
    if not os.path.exists(MODS_DIR):
        return mods

    for folder in os.listdir(MODS_DIR):
        path = os.path.join(MODS_DIR, folder, "mod.json")
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
                data["folder"] = folder
                data.setdefault("depends", [])
                mods[folder] = data
    return mods

def resolve_dependencies(mods, enabled):
    resolved = []

    def add_mod(name):
        if name not in mods or name in resolved:
            return
        for dep in mods[name]["depends"]:
            add_mod(dep)
        resolved.append(name)

    for mod_name, is_enabled in enabled.items():
        if is_enabled:
            add_mod(mod_name)

    return [mods[m] for m in resolved]

def load_mods():
    enabled = load_enabled_config()
    mods = load_all_mods()

    for name in mods:
        mods[name]["enabled"] = enabled.get(name, True)

    return resolve_dependencies(mods, enabled)
