import os

EXE_NAME = "ArknightsEndfield.exe"

POSSIBLE_PATHS = [
    r"C:\Program Files\Arknights Endfield",
    r"C:\Program Files (x86)\Arknights Endfield",
    r"D:\Games\Arknights Endfield",
    r"E:\Games\Arknights Endfield"
]

def get_game_exe():
    for base in POSSIBLE_PATHS:
        exe_path = os.path.join(base, EXE_NAME)
        if os.path.exists(exe_path):
            return exe_path
    return None
