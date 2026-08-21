class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, novo_item):
        for item in self.itens:
            if item.nome == novo_item.nome:
                item.quantidade += novo_item.quantidade
                print(f"Você recebeu mais {novo_item.quantidade}x {novo_item.nome}!")
                return
        self.itens.append(novo_item)
        print(f"Você recebeu: {novo_item.nome}!")

    def remover_item(self, nome_item, quantidade=1):
        for item in self.itens:
            if item.nome.lower() == nome_item.lower():
                item.quantidade -= quantidade
                if item.quantidade <= 0:
                    self.itens.remove(item)
                return True
        return False

    def tem_item(self, nome_item):
        return any(item.nome.lower() == nome_item.lower() for item in self.itens)

    def listar_itens(self):
        if not self.itens:
            print("Sua mochila está vazia.")
            return
        print("\n--- MOCHILA ---")
        for i, item in enumerate(self.itens, start=1):
            print(f"{i}. {item}")

    def usar_item(self, nome_item, jogador):
        for item in self.itens:
            if item.nome.lower() == nome_item.lower():
                if item.tipo == "cura":
                    jogador.vida = jogador.vida + item.efeito_valor
                    if jogador.vida > jogador.vida_maxima:
                        jogador.vida = jogador.vida_maxima
                    print(f"Você usou {item.nome} e recuperou {item.efeito_valor} HP!")
                    self.remover_item(item.nome)
                    return True
                elif item.tipo == "arma":
                    jogador.dano_minp = item.efeito_valor // 2  # metade do valor como mínimo
                    jogador.dano_maxp = item.efeito_valor
                    print(
                        f"Você equipou {item.nome}! Seu dano agora é entre {jogador.dano_minp} e {jogador.dano_maxp}.")
                    self.remover_item(item.nome)
                    return True
                else:
                    print(f"{item.nome} não pode ser usado assim.")
                    return False
        print("Você não tem esse item.")
        return False