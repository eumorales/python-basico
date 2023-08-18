
#8 - Faça um programa em Python que manipule listas com números inteiros, representando
#    valores de glicemia (45 a 450) de um doente diabético. O programa deve receber valores de 
#    glicemia (um a um) até que o usuário não queira mais cadastrá-los. Os dados digitados
#    devem ser inseridos na lista listaDadosOriginais.

#9 - Faça uma adição/complemento no código anterior para mostrar os valores de glicemia
#    da listaDadosOriginais, um abaixo do outro.

#10 - Faça um complemento no código anterior para copiar a listaDadosOriginais para a 
#     listaDadosOrdenados, que na sequência precisa ser ordenada. ?????

#11 - Faça um complemento no código anterior para mostrar o menor e o maior valores
#     de glicemia cadastrados. 

#12 - Faça um complemento no código anterior para mostrar a média dos valores de 
#     glicemia cadastros e na sequência contar e mostrar quantos valores estão abaixo e
#     acima da média.

numeroPacientes = 0

mediaGlicemia = 0
abaixoMedia = 0
acimaMedia = 0

listaDadosOriginais = []

for i in range(numeroPacientes):

    vg = int(input(f"Insira o valor glicêmico do paciente #{i + 1}: "))

    if (vg >= 45 and vg <= 450):

        listaDadosOriginais.append(vg)

    else:

        print("Valor inválido.")


print("\n\nValores glicêmicos registrados: \n")

for i in range(len(listaDadosOriginais)):

    print(f"Paciente #{i + 1}: {listaDadosOriginais[i]}")

print(f"\nMaior valor encontrado: ", max(listaDadosOriginais))
print(f"Menor valor encontrado: ", min(listaDadosOriginais))

for i in range(len(listaDadosOriginais)):
    mediaGlicemia += listaDadosOriginais[i]

print("\nMédia: ", mediaGlicemia / numeroPacientes)

for i in range(len(listaDadosOriginais)):
    
    if (listaDadosOriginais[i] < (mediaGlicemia / numeroPacientes)):

        abaixoMedia += 1

    else:
        
        acimaMedia += 1

print("Acima da média: ", acimaMedia)
print("Abaixo da média: ", abaixoMedia)















