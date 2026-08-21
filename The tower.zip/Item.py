class Item:
    def __init__(self, nome, tipo, descricao, efeito_valor=0, quantidade=1):
        self.nome = nome
        self.tipo = tipo              # cura, arma, armadura, missao
        self.descricao = descricao
        self.efeito_valor = efeito_valor  #quanto de HP cura, ou bônus de dano
        self.quantidade = quantidade

    def __str__(self):
        return f"{self.nome} (x{self.quantidade}) - {self.descricao}"