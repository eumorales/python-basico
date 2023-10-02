import os 
from utils import *

placas = []
carregarDados(placas)

while True:
    print("\nSelecione uma opção:")
    print("\n - 1: Cadastrar nova placa")
    print(" - 2: Remover uma placa")
    print(" - 3: Listar placas")
    x = input(" > ")

    if x == '1':
        registrarPlaca(placas)
    elif x == '2':
        removerPlaca(placas)
    elif x == '3':
        listarPlacas(placas)
    else:
        print('Opção inválida!')
