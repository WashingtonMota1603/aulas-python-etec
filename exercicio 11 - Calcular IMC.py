import os
os.system("cls")
print("CALCULAR IMC CORPORAL:")

# 1. Entrada de dados
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (ex: 1.75): "))

# 2. Cálculo do IMC
imc = peso / (altura ** 2)

# 3. Exibição do resultado
print(f"Seu IMC é: {imc:.1f}")

# 4. Classificação seguindo a imagem enviada
if imc < 17:
    print("Classificação: Muito abaixo do peso")
elif imc < 18.5:
    print("Classificação: Abaixo do peso")
elif imc < 25:
    print("Classificação: Peso normal")
elif imc < 30:
    print("Classificação: Acima do peso")
elif imc < 35:
    print("Classificação: Obesidade grau I")
elif imc <= 40:
    print("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III")

