import os
import json
import time
import random

# 1. Faça sistema de progresso depois

# Os valores são em segundos
interval = 0.025
pause_dialog = 0.100

# Sistema de limpeza de terminal
if os.name == "nt":
    system_clear = "cls"
else:
    system_clear = "clear"

def typing_effect(text):
    for letter in text:
        print(letter, flush=True, end='')
        #time.sleep(interval)
    print() # Nova linha

    time.sleep(pause_dialog)

def main(file):
    try:
        os.system(system_clear)

        # Indicadores de partes
        # da história
        part = "start"
        nextpart = None

        # Abrir o jogo
        with open(file, "r", encoding="utf-8") as jsonfile:
            game = json.load(jsonfile) # Jogo na memória

        # Variáveis do jogo em si...
        section = game[part]
        chapter = section["dialogs"]
        chapterlen = len(scene)

        index = 0

        while True: # Main loop
            while index < chapterlen: # Loop de exibição
                # Definir essa coisa pra não zoar
                # a minha vida, minha existência :D
                state = scene[index]
                dialog = state["text"]
                nextpart = section.get("nextpart")

                # Mecanismo de personagem
                if index == 0:
                    person = state["person"]
                    print(f"[{person}]")

                # Efeito de digitação
                typing_effect(dialog) 

                # Próximo texto....
                index += 1

            input("\nPressione <ENTER> para continuar...")

            index = 0

            print(chapter)
            print(nextpart)

            if nextpart is None:
                break
            else:
                part = nextpart
                chapter = game[nextpart]
                continue

        # Continuar no próximo arquivo
        # (Ainda farei esta parte)
        

        # No final, devolver o arquivo
        # para a lógica do jogo executar

    except KeyboardInterrupt:
        os.system(system_clear)
        print("Fechando o jogo...")
        time.sleep(1.5)

        os.system(system_clear)
