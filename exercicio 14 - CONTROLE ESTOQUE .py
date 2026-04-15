# 14-controle-estoque.py

# Solicita a quantidade de produtos (usamos int para números inteiros)
quantidade = int(input("Digite a quantidade de produtos em estoque: "))

# Verifica a regra de negócio
if quantidade < 5:
    print("Estoque baixo!")
else:
    print("Estoque OK")


