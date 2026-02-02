import os
import subprocess

subprocess.call([
    "pyinstaller",
    "--onefile",
    "--noconsole",
    "--name", "EndfieldModLauncher",
    "launcher/gui.py"
])
