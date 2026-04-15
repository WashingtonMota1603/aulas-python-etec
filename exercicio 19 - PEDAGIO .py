# 19-pedagio.py

print("Selecione o tipo de veículo:")
print("1 - Carro")
print("2 - Moto")
print("3 - Caminhão")

opcao = input("Digite o número da opção: ")

# Verificação das opções
if opcao == "1":
    print("Valor do pedágio: R$ 10,00")
elif opcao == "2":
    print("Valor do pedágio: R$ 5,00")
elif opcao == "3":
    print("Valor do pedágio: R$ 20,00")
else:
    print("Tipo inválido")


