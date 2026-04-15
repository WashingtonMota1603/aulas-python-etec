# 11-velocidade-carro.py

# Recebe a velocidade e converte para número
velocidade = float(input("Digite a velocidade do carro (km/h): "))

# Verifica se ultrapassou o limite
if velocidade > 80:
    print("Multado")
else:
    print("Dentro do limite")


