import os
os.system("cls")

def exibir_menu():
    print()
    print("      MENU DE PAGAMENTO")
    print()
    print("OPÇÃO [1] - Dinheiro (0%)")
    print("OPÇÃO [2] - VR (Taxa de 2%)")
    print("OPÇÃO [3] - Cartão (Taxa de 3%)")
    print()

def calcular_conta():
    # Entradas de dados
    pessoas = int(input("Digite a quantidade de pessoas na mesa: "))
    valor_compra = float(input("Digite o valor total da compra: R$ "))
    
    exibir_menu()
    opcao = input("Escolha a opção desejada (1, 2 ou 3): ")

    # Regras de Negócio: Taxa da forma de pagamento
    taxa_pagamento = 0
    if opcao == "1":
        taxa_pagamento = 0
    elif opcao == "2":
        taxa_pagamento = valor_compra * 0.02
    elif opcao == "3":
        taxa_pagamento = valor_compra * 0.03
    else:
        print("Opção inválida! Reinicie o programa.")
        return

    # Cálculos sequenciais
    valor_com_taxa = valor_compra + taxa_pagamento
    valor_garcom = valor_com_taxa * 0.10  # 10% sobre o valor com a taxa de pagamento
    total_final = valor_com_taxa + valor_garcom
    valor_por_pessoa = total_final / pessoas

    # Exibição dos resultados (Saída)
    print()
    print("RESUMO DA CONTA:")
    print()
    print(f"Valor original: R$ {valor_compra:.2f}")
    print(f"Taxa de pagamento: R$ {taxa_pagamento:.2f}")
    print(f"Taxa do garçom: R$ {valor_garcom:.2f}")
    print(f"VALOR TOTAL FINAL: R$ {total_final:.2f}")
    print(f"Cada pessoa paga: R$ {valor_por_pessoa:.2f}")
    print()

# Chama a função para iniciar o programa
calcular_conta()




