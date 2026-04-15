#Consumo-combustivel - Crie um programa que receba a quantidade de quilômetros percorridos
# e a quantidade de litros de combustível gastos. Ao final, o programa deve calcular 
# e exibir o consumo médio do veículo em km por litro.
import os
os.system("cls")
print("Consumo de combustível")

#Entrada de dados
km = float(input("Digite a distância percorrida (km): "))
litros = float(input("Digite a quantidade de litros gastos: "))

# Calculo do consumo médio
consumo = km / litros

#Saída
print(f"O consumo médio do veículo é de {consumo:.2f} km/l.") # O :.2f serve para mostrar apenas 2 casas decimais

