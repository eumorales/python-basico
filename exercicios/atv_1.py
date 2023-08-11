#1 - Um usuário (diabético) de insulina rápida precisa fazer uso do medicamento sempre que for realizar
#    uma refeição. Assim, faça um programa que receba do usuário sua glicemia do momento (mg/dl),
#    meta pré-refeição (em geral é 100 mg/dl), fator de sensibilidade (valor inteiro entre 20 a 60). 
#    A partir desses valores, o programa deve calcular e exibir para o usuário a quantidade de insulina
#    que ele deverá administrar baseada na equação: 
#    quantidade_insulina = (glicemia_do_momento - meta_pre_refeicao) / fator_sensibilidade

import math

glicemia = float(input("\nInsira a glicemia do usuário (mg/dl): "))
meta = float(input("\nInsira a meta pré-refeição do usuário (mg/dl): "))
fator = int(input("\nInsira o fator de sensibilidade: "))

insulina = (glicemia - meta) / fator
print("\n\nA quantidade de insulina no momento é ", insulina, ".")