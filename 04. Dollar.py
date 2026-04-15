import os
os.system("cls")

#1 - Entrada de Dados
print("Atividade - Conversor de Dollar para Real")
quantia_dollar = float(input("Entre com uma quantia de dollar($):"))

cotacao_dollar = float(input("Digite a cotação do dollar do dia:"))

#2 - Processamento
total_em_reais = quantia_dollar * cotacao_dollar

#3 - Saída
print(f"O valor total em reais será R$ {total_em_reais:.2f}")

