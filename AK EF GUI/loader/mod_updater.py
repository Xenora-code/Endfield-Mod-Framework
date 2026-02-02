import json
import os
import urllib.request

MODS_DIR = "mods"

def fetch_json(url):
    with urllib.request.urlopen(url, timeout=10) as r:
        return json.loads(r.read().decode("utf-8"))

def update_mod(mod):
    url = mod.get("update_url")
    if not url:
        return False

    remote = fetch_json(url)
    if remote["version"] == mod["version"]:
        return False

    mod_folder = os.path.join(MODS_DIR, mod["folder"])
    os.makedirs(mod_folder, exist_ok=True)

    with open(os.path.join(mod_folder, "mod.json"), "w", encoding="utf-8") as f:
        json.dump(remote, f, indent=2)

    return True

def update_all(mods):
    updated = []
    for mod in mods:
        try:
            if update_mod(mod):
                updated.append(mod["name"])
        except Exception:
            pass
    return updated
