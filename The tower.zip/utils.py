import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausa(segundos=1.5):
    time.sleep(segundos)