#3 - Refaça o programa anterior (refatorar) para que o programa recebe a distância e a velocidade média,
#    mas calcule e exiba o tempo da viagem.

distancia = float(input("\nDigite a distância a ser percorrida (km): "))
velocidadeMedia = float(input("\nDigite a velocidade média do motorista (km/h): "))

tempo = distancia / velocidadeMedia
print("\nA viagem vai durar em média", tempo, "hora(s).")