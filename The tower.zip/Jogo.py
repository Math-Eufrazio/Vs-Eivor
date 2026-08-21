import time
from utils import limpar_tela, pausa
from Castelo import quarto
from seed import seed
from Jogador import Jogador
from Batalha import batalhar

jogador = Jogador("Follks", 100, 5, 20)
jogador.mochila.adicionar_item(seed["pocao_pequena"])

print("""░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")


                                        jogo das maravilhas




                                      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                                      █--------MENU---------█
                                      █-------1. JOGAR------█
                                      █-------2. SAIR-------█
                                      █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█




░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n""")

escolha1 = input()

if escolha1 == "1":
    print(""" ... Iniciando ... """)
    time.sleep(2)
else:
    print(""" ... Encerrando ... """)
    exit()

limpar_tela()
print("Você acorda em uma sala escura com paredes de pedra e somente uma cama")
input()
limpar_tela()
print(f"A única coisa que você se lembra é seu nome: {jogador.nome}")
pausa(2)
limpar_tela()
print("e o fato de que você precisa sair daqui")
pausa(2)

sala_atual = quarto

while True:
    limpar_tela()
    print(f"Você está em: {sala_atual.nome}")
    print(sala_atual.descricao)
    print(f"[HP: {jogador.vida}/{jogador.vida_maxima}]")

    if jogador.vida <= 0:
        print("\nSua jornada termina aqui...")
        exit()

    saidas_visiveis = [d for d in sala_atual.saidas if d != "secreto"]
    if saidas_visiveis:
        print("\nVocê pode ir para:", ", ".join(saidas_visiveis))
    print("(digite 'mochila' pra ver seus itens)")

    comando = input("> ").lower()

    if comando == "mochila":
        limpar_tela()
        if not jogador.mochila.itens:
            print("Sua mochila está vazia.")
            pausa(2)
            continue

        jogador.mochila.listar_itens()
        escolha_item = input("\nNúmero do item pra usar (0 pra voltar): ")

        if escolha_item.isdigit() and 1 <= int(escolha_item) <= len(jogador.mochila.itens):
            item_escolhido = jogador.mochila.itens[int(escolha_item) - 1]
            limpar_tela()
            jogador.mochila.usar_item(item_escolhido.nome, jogador)
            pausa(2)

        continue

    elif comando in sala_atual.saidas:
        destino = sala_atual.saidas[comando]

        if not destino.pode_entrar(jogador):
            limpar_tela()
            print("Algo impede sua passagem... você sente que precisa de algo específico pra entrar aqui.")
            pausa(2)
        else:
            limpar_tela()
            if comando == "secreto":
                print("Você sussurra a palavra... e o mundo ao seu redor desaparece.")
            else:
                print(f"Você segue em direção ao {comando}...")
            pausa()
            sala_atual = destino

            sala_atual.explorar()
            pausa()

            for monstro in sala_atual.monstros:
                if monstro.vida > 0:
                    resultado = batalhar(jogador, monstro)
                    if resultado == "derrota":
                        limpar_tela()
                        print("Fim de jogo.")
                        exit()

            if sala_atual.itens:
                for item in sala_atual.itens:
                    limpar_tela()
                    print(f"Você guardou: {item.nome}")
                    jogador.mochila.adicionar_item(item)
                    pausa()
                sala_atual.itens = []

    else:
        print("Nada acontece.")
        pausa(1)
