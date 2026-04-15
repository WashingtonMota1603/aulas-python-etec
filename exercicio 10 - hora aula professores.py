
import os
os.system("cls")
print("Atividade calcular hora/aula dos professores")
# 1. Entrada de dados
nivel = int(input("Digite o nível do professor (1, 2 ou 3): "))
aulas_semana = int(input("Digite a quantidade de aulas por semana: "))

# 2. Definir o valor da hora conforme o nível
if nivel == 1:
    valor_hora = 12.00
elif nivel == 2:
    valor_hora = 17.00
elif nivel == 3:
    valor_hora = 25.00
else:
    valor_hora = 0
    print("Nível inválido!")

# 3. Calcular e exibir o resultado
if valor_hora > 0:
    salario = aulas_semana * valor_hora
    print(f"O salário final do professor é: R$ {salario:.2f}")
