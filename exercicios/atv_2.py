#2 - Faça um programa que ajude motoristas calcular e estimar viagens com diferentes tempos de viagem.
#    O programa deve receber do usuário do sistema (motorista) a distância a ser percorrida e o tempo
#    desejado da viagem. A partir disso, o programa deve calcular e exibir na tela a velocidade média
#    necessária.

# distância a ser percorrida e o tempo desejado da viagem

distancia = float(input("\nDigite a distância a ser percorrida (km): "))
tempoDesejado = float(input("\nDigite o tempo desejado até o destino (horas): "))

velocidadeMedia = distancia / tempoDesejado
print("\nA velocidade média deve ser ", velocidadeMedia, "km/h.")


