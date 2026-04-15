import os
os.system("cls")

print("Calcular idade de uma pessoa!")

#Entrada de dados
ano_atual= int(input("Digite seu ano atual:"))
ano_nascimento= int(input("Digite o ano de nascimento:"))

#Processamento
idade = ano_atual - ano_nascimento

#Saída
print("A idade atual da pessoa é:", idade, "anos")