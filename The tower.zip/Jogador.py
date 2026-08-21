from Inventario import  Inventario

class Jogador:
    def __init__(self, nome, vida_maxima, dano_minp, dano_maxp):
        self.nome = nome
        self.vida = vida_maxima
        self.vida_maxima = vida_maxima
        self.mochila = Inventario()
        self.dano_minp = dano_minp
        self.dano_maxp = dano_maxp