#Limpar o terminal
import os
os.system ("cls")

#CRIAR UM PROGRAMA EM PYTHON QUE EFETUE A CONVERSÃO DE UMA TEMPERATURA CELSIUS PARA FAHRENHEIT

print("Atividade - Conversor de Temperatura")

#Entrada de Dados
celsius = float (input("Digite a temperatura em Celsius:"))

#Processamento
fahrenheit = (9 * celsius + 160) / 5

#saída
print("A temperatura em Fahrenheit é:", fahrenheit)