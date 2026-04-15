import os
os.system("cls")
print("Atividade Impar ou par")
#ETAPA 1 - ENTRADA DE DADOS
# Passo 1: Pedir ao utilizador para digitar um número

numero = int(input("Digite um número: "))

# Passo 2: Verificar se o resto da divisão por 2 é igual a zero
# O símbolo % calcula o "resto". Se o resto for 0, o número é par.

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")


