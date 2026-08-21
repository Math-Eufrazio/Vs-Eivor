class Sala:
    def __init__(self, nome, descricao, anterior=None, requisitos=None):
        self.nome = nome
        self.descricao = descricao
        self.saidas = {}
        self.anterior = anterior
        self.explorada = False
        self.itens = []        # lista de Items fixos dessa sala
        self.monstros = []     # lista de Inimigos fixos dessa sala
        self.requisitos = requisitos if requisitos else []  # nomes de itens necessários pra entrar

    def conectar(self, direcao, outra_sala):
        self.saidas[direcao] = outra_sala

    def conectar_mao_dupla(self, direcao, direcao_oposta, outra_sala):
        self.saidas[direcao] = outra_sala
        outra_sala.saidas[direcao_oposta] = self

    def pode_entrar(self, jogador):
        for nome_item in self.requisitos:
            if not jogador.mochila.tem_item(nome_item):
                return False
        return True

    def explorar(self):
        if self.explorada:
            print("Você já explorou essa sala, não parece ter mais nada aqui.")
            return

        self.explorada = True

        if not self.itens and not self.monstros:
            print("\nVocê explora a sala, mas não encontra nada de interessante.")
            return

        if self.monstros:
            print(f"\n⚠️ Você encontrou {len(self.monstros)} inimigo(s) nessa sala!")
            for m in self.monstros:
                print(f" - {m.nome}")

        if self.itens:
            print(f"\nVocê encontrou {len(self.itens)} item(ns) nessa sala:")
            for i in self.itens:
                print(f" - {i.nome}")