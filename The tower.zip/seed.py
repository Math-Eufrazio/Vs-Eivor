from Item import Item

# Itens de cura
pocao_pequena = Item("Poção Pequena", "cura", "Restaura 15 HP", efeito_valor=15)
pocao_grande = Item("Poção Grande", "cura", "Restaura 40 HP", efeito_valor=40)
pocao_MASTODONTICA = Item("Poção MASTODONTICA","cura", "Restaura tudo meu mano", efeito_valor= 100)

# Armas
espada_enferrujada = Item("Espada Enferrujada", "arma", "Aumenta o dano base", efeito_valor=5)
machado_viking = Item("Machado Vikingo", "arma", "Aumenta bastante o dano", efeito_valor=12)
zenite = Item("Zênite", "arma", "Algo que um mortal jamais deveria segurar", efeito_valor=67)

# Itens de missão
chave_antiga = Item("Chave Antiga", "missao", "Abre uma porta trancada em algum lugar")
chave_brilhante = Item("Chave Brilhante", "missao","Abre um lugar muito especial, cuide bem dessa chave")

seed = {
    "pocao_pequena": pocao_pequena,
    "pocao_grande": pocao_grande,
    "pocao_mastodontica": pocao_MASTODONTICA,
    "espada_enferrujada": espada_enferrujada,
    "machado_viking": machado_viking,
    "zenite": zenite,
    "chave_antiga": chave_antiga,
    "chave_brilhante": chave_brilhante,
}
