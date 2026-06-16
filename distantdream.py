#!/usr/bin/env python3
import os
from modules import engine, detect_sys

system_clear = detect_clear()

def main():
    os.system("clear")
    engine.main("scenes/intro.json")

if __name__ == "__main__":
    main()
