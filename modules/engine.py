import os
import sys
import json
import time

from . import utils

#####################################
# 1. Faça sistema de progresso depois

# Continuar no próximo arquivo
# (Ainda farei esta parte)

# No final, devolver o arquivo
# para a lógica do jogo executar
#####################################

# Sistema de limpeza de terminal
system_clear = utils.detect_clear()

# Sistema de configuração
setting = utils.loadfile("settings.json")

def main(file):
    try:
        # Loop para leitura de arquivos
        while True:
            game = utils.loadfile(file) # Jogo na memória

            # Indicadores de partes da história 
            # Inicializando eles...
            part = "start" # O padrão é "start"
            nextpart = None # Nada carregado
            nextfile = None # Também não já nada...

            # Já viu começar de outro lugar?
            # Claro que o index pra "folhear" a história
            # é justo do ponto zero!
            index = 0

            # Lógica principal do jogo
            while True:
                os.system(system_clear)

                while index < len(game[part]["dialogs"]):
                    # Definir essa coisa pra não zoar
                    # a minha vida, minha existência :D
                    section = game[part]["dialogs"][index]
                    dialogs = game[part]["dialogs"]
                    dialog = section["text"]

                    # Próxima parte para continuar
                    nextpart = section.get("nextpart")

                    # Checagem de personagens
                    oldperson = dialogs[index - 1].get("person", None)
                    newperson = section.get("person", None)
                    
                    print(f"oldperson: {oldperson}\nnewperson: {newperson}")

                    # Mecanismo de personagem
                    if index == 0:
                        print(f"[{newperson}]")

                    # Cheque se o personagem anterior é diferente
                    # ou igual ao atual. Se verdadeiro para diferente,
                    # logo, exibir personagem diferente

                    # Foi a parte mais legal do código, poxa :,)
                    if oldperson != newperson and not oldperson is None:
                        print(f"\n[{newperson}]")

                    # A gente as vezes tem que parar, né?
                    # Já pensou como vive o trabalhador
                    # sem descansar?
                    if section.get("wait", False) is True: 
                        interval = section["interval"]

                        # Roda pião!
                        for _ in range(section["roll"]):
                            os.system(system_clear)
                            utils.typing_effect(setting, dialog, Wait=interval, NewLine=False)

                    else:
                        # Efeito de digitação 
                        utils.typing_effect(setting, dialog) 

                    # Se for uma pergunta, então...
                    if section.get("question") is True:
                        options = section["options"]

                        # Você recebe as escolhas...
                        for i, choice in enumerate(options):
                            utils.typing_effect(setting, f"[{i+1}] {options[i]["option"]}")

                        while True:
                            try:
                                # Agora escolha por onde trilhar
                                choice_player = int(input("> ")) - 1

                                # A escolha foi sua! Presuma sua consequência!
                                if choice_player >= 0 and choice_player < len(options):
                                    # Verificar se tem continuação no próximo arquivo...
                                    # Vire a página, filho!
                                    nextfile = options[choice_player].get("nextfile", None)

                                    # Se houver algo, apenas seguir o que manda
                                    # Se não houver nada, segue o padrão...
                                    nextpart = options[choice_player].get("nextpart", "start") 

                                    # Bora processar dados!
                                    break
                                else:
                                    # Volta pra trás, rapaz!
                                    # Escolhe direito! >:(
                                    continue

                            # Digite um número, seu boboca!
                            except ValueError: 
                                continue

                    # Próximo texto....
                    index += 1 

                # Deseja que o jogo pause e continue com enter?
                # Não parece muito legal as vezes
                # Só configurar e arrastar pra cima, pô!
                if setting["pause_enter"] is True:
                    input("\nPressione <ENTER> para continuar...")
                else:
                    time.sleep(setting["long_pause"])

                # Se houver continuação em outro arquivo,
                # apenas devolver e deixar o loop main
                # fazer seu serviço, é claro
                if nextfile:
                    file = nextfile
                    nextfile = None
                    break

                # A história apenas continua...
                if nextpart is None:
                    break

                else:
                    # Afinal, a história não acaba, poxa.
                    # Deixa rolar! Deixa ir pra outra parte!
                    part = nextpart
                    section = game[part]
                    index = 0

            # O fim.
            if nextfile is None and nextpart is None:
                break

    except KeyboardInterrupt:
        os.system(system_clear)
        print("Fechando o jogo...")
        time.sleep(1.5)
