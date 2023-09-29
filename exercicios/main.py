import os

from utils import *

placas = []
carregarDados(placas)

while (True):

    placas = [] 
    print("\nSelecione uma opção:")
    print("\n - 1: Cadastrar nova placa")
    print(" - 2: Remover uma placa")
    print(" - 3: Listas placas\n")
    x = input(" > ")

    if x == '1':
        registrarPlaca(placas)
    elif x == '2':
        removerPlaca(placas)
    else:
        print('Opção inválida!')

    



