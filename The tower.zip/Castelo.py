from Sala import Sala
from Monstros import monstros
from seed import seed
import copy

quarto = Sala("Quarto Escuro", "Uma cama velha e paredes de pedra fria.")

corredor_norte = Sala("Corredor Norte", "Um corredor frio. a uma tocha meio torta nele")
corredor_norte.itens = [copy.deepcopy(seed["pocao_pequena"])]

salao_sul = Sala("Salão Sul", "Um salão empoeirado com um baú entreaberto.")
salao_sul.itens = [
    copy.deepcopy(seed["espada_enferrujada"]),
    copy.deepcopy(seed["chave_antiga"]),]

sala_leste = Sala("Sala Leste", "Algo parece errado aqui.")
sala_leste.monstros = [copy.deepcopy(monstros["draugr"])]
sala_leste.itens = [copy.deepcopy(seed["pocao_grande"])]

# sala oculta: SEM requisito, é aqui que se pega a Chave Brilhante
sala_oculta = Sala("Sala oculta", "Um lugar que não parece ter chão nem paredes")
sala_oculta.monstros = [copy.deepcopy(monstros["gato_chapeu"])]
sala_oculta.itens = [copy.deepcopy(seed["chave_brilhante"])]

# limbo: só acessível pelo comando secreto no quarto, exige Chave Brilhante
limbo = Sala(
    "O Limbo",
    "Um vazio silencioso, fora do tempo. Algo poderoso repousa aqui.",
    requisitos=["Chave Brilhante"],
)
limbo.itens = [copy.deepcopy(seed["zenite"])]

sala_trono = Sala(
    "Sala do Trono",
    "O grande Eivor aguarda, sentado em seu trono.",
    requisitos=["Chave Antiga"],
)
sala_trono.monstros = [copy.deepcopy(monstros["eivor"])]

biblioteca = Sala("Biblioteca", "Cheira a ácaro e poeira, você ve livros velhos jogados em todos os cantos, senti por algum motivo sente um certo arrepio")
biblioteca.monstros = [copy.deepcopy(monstros["Espirito"])]
biblioteca.Item = [copy.deepcopy(seed["pocao_mastodontica"])]

sala_arma = Sala("Sala de armas", "E cheio de armas nas paredes, espada, arcos, lanças. por algum motivo que nem você sabe vc não sente vontade de pegar nenhuma")
sala_arma.monstros = [copy.deepcopy(monstros["lobo_selvagem"])]
sala_arma.Item = [copy.deepcopy(seed["machado_viking"])]
sala_arma.Item = [copy.deepcopy(seed["pocao_grande"])]

# conexões normais (mão dupla = pode ir e voltar)
quarto.conectar_mao_dupla("norte", "sul", corredor_norte)
quarto.conectar_mao_dupla("sul", "norte", salao_sul)
quarto.conectar_mao_dupla("leste", "oeste", sala_leste)
corredor_norte.conectar_mao_dupla("tocha", "oeste", sala_oculta)
sala_leste.conectar_mao_dupla("leste", "oeste", sala_trono)
corredor_norte.conectar_mao_dupla("norte", "sul", biblioteca)
corredor_norte.conectar_mao_dupla("oeste", "leste", sala_arma)

# conexão secreta: só existe no dicionário, não é mostrada no menu normal
quarto.conectar_mao_dupla("secreto", "sair", limbo)