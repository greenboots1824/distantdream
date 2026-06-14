#!/bin/python3
import json
import time
import random

def typing_effect(text):
    linebreak = 50
    interval = 0.050

    for letter in text:
        print(letter, flush=True, end='')
        time.sleep(interval)

def main():
    # Abrir o jogo
    with open("scenes/intro.json", "r", encoding="utf-8") as file:
        game = json.load(file)

    # Começando pela intro...
    cenario_state = "intro"
    section  = game[game_state]["falas"]
    talk = game[game_state]

    while True:
        # Efeito de digitação
        typing_effect(f"Teste: {section[n]["texto"]}") 



        if section[n]["texto"] == None:
            break

    # Continuar no próximo arquivo

if __name__ == "__main__":
    main()
