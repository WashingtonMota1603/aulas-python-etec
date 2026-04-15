# 16-contador-letras.py

# Recebe a palavra do usuário (input sempre recebe texto)
palavra = input("Digite uma palavra: ")

# A função len() conta o número de caracteres do texto
quantidade = len(palavra)

# Exibe o resultado usando f-string para facilitar a leitura
print(f"A palavra '{palavra}' possui {quantidade} letras.")
