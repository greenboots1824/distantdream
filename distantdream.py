#!/bin/python3
import os
from modules import engine

# Fazer reconhecimento de "clear"

def main():
    os.system("clear")
    engine.engine("scenes/intro.json")

if __name__ == "__main__":
    main()
