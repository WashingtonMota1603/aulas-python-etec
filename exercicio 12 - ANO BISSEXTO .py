# 12-ano-bissexto.py

# Recebe o ano e converte para número inteiro
ano = int(input("Digite um ano: "))

# Verifica se o resto da divisão por 4 é zero
if ano % 4 == 0:
    print("Ano bissexto")
else:
    print("Não é bissexto")


