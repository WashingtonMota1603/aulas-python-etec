import random

# O programa escolhe um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Solicita o palpite do usuário
palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))

# Verifica se o palpite está correto
if palpite == numero_secreto:
    print("Acertou!")
else:
    print(f"Errou! O número era: {numero_secreto}")


