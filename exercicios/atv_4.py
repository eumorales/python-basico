#4 - O volume de um cubo é determinado através do produto da área da base pela altura, 
#    (mas as arestas do cubo possuem medidas iguais), então temos que:
#    V = Ab * a ou V = a * a * a → V = a³. A partir disso, faça um programa, adequando as variáveis
#    para receber medidas de uma piscina (altura, largura e comprimento), para responder o volume de
#    água necessário para enchê-la.

import math

altura = float(input("\nInforme a altura da piscina (m): "))
largura = float(input("\nInforme a largura da piscina (m): "))
comprimento = float(input("\nInforme o comprimento da piscina (m): "))

piscina = (altura * largura * comprimento) * 1000
print("Para encher a piscina será necessário", round(piscina), "litros de água.")