#6 - Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que 
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens: 
#    Carioca Paulista Mineiro Outros estados

sigla = input("\nInsira a sigla de um estado brasileiro (RJ, SP, MG): ")

if (sigla == "rj"):
    print("Carioca!")

elif (sigla == "sp"):
    print("Paulista!")

elif (sigla == "mg"):
    print("Mineiro!")

else:
    print("Outro estado.")
