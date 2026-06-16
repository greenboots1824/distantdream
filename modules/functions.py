import sys
import time
import random

# Sistema de configuração
def load_settings():
    with open("settings.json", "r", encoding="utf-8") as settingsfile:
        setting = json.load(settingsfile)

    return setting

def detect_clear():
    if os.name == "nt":
        # Windows
        system_clear = "cls"
    else:
        # Linux/MacOS
        system_clear = "clear"

    return system_clear

