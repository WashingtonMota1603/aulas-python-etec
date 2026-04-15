import os

os.system("cls")

#PASSO 1 - VARIAVEIS E ENTRADAS
print("Calculadora de Desconto")

nome_produto = input("Entre com o nome do Produto:")
preco = float(input("Entre com o preço do Produto:"))
percentual_desconto = float(input("Entre com o percentual de desconto%:"))

# PASSO 2 - PROCESSAMENTO
valor_desconto = preco*percentual_desconto/100
preco_final=preco-valor_desconto

#PASSO 3 - EXIBIR A SAIDA
print("===================================================")
print("Preço  Original:", preco, "- Preço com Desconto:", preco_final)

print(f"Preço Original: R${preco} - Preço com Desconto: R$ {preco_final}")