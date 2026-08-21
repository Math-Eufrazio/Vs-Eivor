import random
from utils import limpar_tela, pausa

def batalhar(jogador, inimigo):
    limpar_tela()
    print(f"\nUm combate contra {inimigo.nome} começou!")
    pausa()

    while inimigo.vida > 0 and jogador.vida > 0:
        limpar_tela()
        print(f"--- STATUS: {jogador.nome} [HP: {jogador.vida}] | {inimigo.nome} [HP: {inimigo.vida}] ---")
        print("""
        1. Atacar
        2. Fugir
        3. Defender
        4. Usar item
        """)

        escolha = input("Ação: ")

        inimigo_vai_atacar = False
        dano_reduzido = False

        if escolha == "1":
            limpar_tela()
            dano = random.randint(jogador.dano_minp, jogador.dano_maxp)
            inimigo.vida -= dano
            print(f"Você atacou {inimigo.nome} e causou {dano} de dano")
            pausa()
            inimigo_vai_atacar = True

        elif escolha == "3":
            limpar_tela()
            print("Você levanta seu escudo!")
            pausa()
            dano_reduzido = True

            if random.random() < 0.6:
                inimigo_vai_atacar = True
            else:
                print(f"{inimigo.nome} hesitou e não te atacou!")
                pausa()

        elif escolha == "2":
            limpar_tela()
            print("Você fugiu da batalha!")
            pausa()
            return "fugiu"

        elif escolha == "4":
            limpar_tela()
            if not jogador.mochila.itens:
                print("Sua mochila está vazia!")
                pausa()
                continue

            jogador.mochila.listar_itens()
            escolha_item = input("\nNúmero do item pra usar (0 pra cancelar): ")

            if escolha_item == "0":
                continue

            if escolha_item.isdigit() and 1 <= int(escolha_item) <= len(jogador.mochila.itens):
                item_escolhido = jogador.mochila.itens[int(escolha_item) - 1]
                limpar_tela()
                usado = jogador.mochila.usar_item(item_escolhido.nome, jogador)
                pausa()
                if not usado:
                    continue
                inimigo_vai_atacar = True
            else:
                print("Escolha inválida!")
                pausa(1)
                continue

        else:
            print("Escolha inválida!")
            pausa(1)
            continue

        if inimigo_vai_atacar and inimigo.vida > 0:
            dano_e = random.randint(inimigo.dano_min, inimigo.dano_max)
            if dano_reduzido:
                dano_e //= 3
            jogador.vida -= dano_e
            print(f"\n{inimigo.nome} atacou e causou {dano_e} de dano!")
            pausa()

    limpar_tela()
    if jogador.vida <= 0:
        print(f"\nVocê foi derrotado por {inimigo.nome}...")
        pausa()
        return "derrota"
    else:
        print(f"\nVocê venceu {inimigo.nome}!")
        pausa()
        return "vitoria"