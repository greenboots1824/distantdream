import os
import sys
import json
import time

from .functions import detect_clear

# 1. Faça sistema de progresso depois

# Continuar no próximo arquivo
# (Ainda farei esta parte)


# No final, devolver o arquivo
# para a lógica do jogo executar

# Sistema de limpeza de terminal
system_clear = detect_clear()

# Sistema de configuração
with open("settings.json", "r", encoding="utf-8") as settingsfile:
    setting = json.load(settingsfile)

#def load_file(filename):
#    with open(filename, "r", encoding="utf-8") as file:
#        return json.load(file)

def typing_effect(text):
    for letter in text:
        print(letter, flush=True, end='')
        time.sleep(random.uniform(setting["interval_min"], setting["interval_max"]))
    print() # Nova linha

    time.sleep(setting["pause_dialog"])

def main(file):
    try:
        # Abrir o jogo
        with open(file, "r", encoding="utf-8") as gamefile:
            game = json.load(gamefile) # Jogo na memória

        # Indicadores de partes da história 
        part = "wake_up"
        nextpart = None
        nextfile = None # Trabalhar na importação de arquivos

        index = 0

        # Lógica principal do jogo
        while True:
            os.system(system_clear)

            while index < len(game[part]["dialogs"]):
                # Definir essa coisa pra não zoar
                # a minha vida, minha existência :D
                section = game[part]["dialogs"][index]
                dialog = section["text"]

                nextpart = section.get("nextpart")

                # Mecanismo de personagem
                if index == 0:
                    person = section["person"]
                    print(f"[{person}]")

                # Efeito de digitação
                typing_effect(dialog) 

                # Se for uma pergunta, então...
                if section.get("question") is True:
                    options = section["options"]

                    # Você recebe as escolhas...
                    for i, choice in enumerate(options):
                        typing_effect(f"[{i+1}] {options[i]["option"]}")

                        while True:
                            try:
                                # Agora escolha por onde trilhar
                                choice_player = int(input("> "))

                                # Bora processar dados!
                                break

                            # Digite um número, seu boboca!
                            except ValueError: 
                                continue

                    # A escolha foi sua! Presuma sua consequência!
                    if choice_player < 0 or choice_player > len(options):
                        part = options[choice_player]["nextpart"]





                # Próximo texto....
                index += 1 

            # Deseja que o jogo pause com enter?
            # Não parece muito legal as vezes

            # Só configurar e arrastar pra cima, pô!
            if setting["pause_enter"] is True:
                input("\nPressione <ENTER> para continuar...")
            else:
                time.sleep(setting["long_pause"])

            # Segmento da história...
            if nextpart is None:
                break
            else:
                # Afinal, a história não acaba, poxa.
                # Deixa rolar! Deixa ir pra outra parte!
                part = nextpart
                section = game[part]
                index = 0 

    except KeyboardInterrupt:
        os.system(system_clear)
        print("Fechando o jogo...")
        time.sleep(1.5)

    except Exception as error:
        os.system(system_clear)
        print("An error occurred:", error)
        sys.exit(1)
