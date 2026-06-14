#!/bin/python3
import json
import time
import random

# All these values are
# in seconds.
interval_min = 0.050
interval_max = 0.150
pause_between_dialog = 0.400

def typing_effect(text):
    for letter in text:
        print(letter, flush=True, end='')
        time.sleep(random.uniform(interval_min, interval_max))

    time.sleep(pause_between_dialog)

def main():
    # Abrir o jogo
    with open("scenes/intro.json", "r", encoding="utf-8") as file:
        game = json.load(file) # Jogo na memória

    # Começando pela intro...
    scene = game["start"]["dialogs"]
    scenelen = len(scene)
    index = 0

    while index < scenelen:
        # Definir essa coisa pra não zoar
        # a minha vida, minha existência :D
        state = scene[index]
        dialog = state["text"]

        # Efeito de digitação
        typing_effect(dialog) 

        # Próximo texto....
        index += 1

    # Continuar no próximo arquivo
    # (Ainda farei esta parte)

if __name__ == "__main__":
    main()
