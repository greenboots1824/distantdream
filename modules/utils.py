import os
import json
import sys
import time
import random

def typing_effect(setting, text, Wait=-1.0, NewLine=True):
    if not isinstance(NewLine, bool):
        raise TypeError("NewLine is not a boolean!")

    if not isinstance(Wait, float):
        raise TypeError("Wait is not an int!")

    for letter in text:
        print(letter, flush=True, end='')

        # -1 para desativado
        if Wait == -1.0:
            time.sleep(random.uniform(setting["interval_min"], setting["interval_max"]))

        else:
            time.sleep(Wait)

    if NewLine:
        print() # Nova linha

    time.sleep(setting["pause_dialog"])

def loadfile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def detect_clear():
    # Windows
    if os.name == "nt":
        system_clear = "cls"

    # Linux/MacOS
    else:
        system_clear = "clear"

    return system_clear
