from Inimigo import Inimigo

eivor = Inimigo("O grande Eivor", vida=150, dano_min=1, dano_max=40)
lobo_selvagem = Inimigo("Lobo Selvagem", vida=60, dano_min=5, dano_max=15)
draugr = Inimigo("Draugr Amaldiçoado", vida=90, dano_min=16, dano_max=10)
gato_chapeu = Inimigo("Gato de Chapéu", vida=6, dano_min=3, dano_max=6)
armadura_amaldicoada = Inimigo("Armadura Amaldiçoada", vida=43, dano_min=2, dano_max=20)
Androesfinge = Inimigo("Androesfinge", vida=51, dano_min=10, dano_max=12)
Espirito = Inimigo("Espirito", vida=100, dano_min=0, dano_max=0)

monstros = {
    "eivor": eivor,
    "lobo_selvagem": lobo_selvagem,
    "draugr": draugr,
    "gato_chapeu": gato_chapeu,
    "armadura_amaldicoada": armadura_amaldicoada,
    "Androesfinge": Androesfinge,
    "Espirito": Espirito
}