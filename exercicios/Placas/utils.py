def carregarDados(placas):
    try:
        arquivo = open('placas.dat', 'r')
        for linha in arquivo:
            placa = linha.strip()
            placas.append(placa)
        arquivo.close()
    except IOError:
        print("Ocorreu um erro ao carregar as placas.")

def registrarPlaca(placas):
    placa = input("\nInforme a placa do veículo: ").upper()
    if placa in placas:
        print("Veículo já cadastrado.")
    else:
        print("Placa cadastrada com sucesso.")
        placas.append(placa)
        escritor = open('placas.dat', 'a')
        escritor.write(placa + '\n')
        escritor.close()

def removerPlaca(placas):
    placa = input("\nInforme a placa do veículo a ser removido: ").upper()
    if placa in placas:
        placas.remove(placa)
        print("Placa removida com sucesso.")
        arquivo = open('placas.dat', 'w')
        for p in placas:
            arquivo.write(p + '\n')
        arquivo.close()
    else:
        print("Placa não encontrada.")

def listarPlacas(placas):
    if placas:
        print("\nLista de placas:")
        for placa in placas:
            print(placa)
    else:
        print("\nNenhuma placa cadastrada.")

