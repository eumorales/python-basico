import os

from utils import *

lista_inscritos = [] 
conexao_base(lista_inscritos)

while True:
    os.system('cls')
    print('MENU')
    print('1 - Fazer inscrições')
    print('2 - Listar inscritos')
    print('3 - Registrar entrada')
    print('4 - Registrar saída')
    print('5 - Finalizar')
    op = input('Opção: ')

    if op == '1':
        print('Inscrições')
        inscricao(lista_inscritos)
    elif op == '2':
        print('Listagem de inscritos')
        listagem(lista_inscritos)
    elif op == '3':
        print('Registrar entrada')
        entrada(lista_inscritos)
    elif op == '4':
        print('Registrar saída')
        saida(lista_inscritos)
    elif op == '5':
        break
    else:
        print('Opção inválida!')

    os.system('pause')