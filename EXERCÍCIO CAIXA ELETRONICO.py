import os
os.system("cls")

print("Bem-vindo ao Mota's Bank!\n" \
"Segurança, confiança e excelência em cada transação. Em que podemos lhe ajudar hoje?\n")

saldo=1000

while True:
    print("OPÇÃO [1] - Consultar Saldo")
    print("OPÇÃO [2] - Realizar Deposito")
    print("OPÇÃO [3] - Realizar Saque")
    print("OPÇÃO [4] - Sair\n")
    opcao = int(input("Digite a opção para o serviço desejado: "))

    if opcao == 1:
        print("'Opção [1] - Consultar Saldo' selecionada ... Seu saldo atual é: R$", saldo)
        print() # usei somente para quebrar a linha no terminal, pra ficar mais separadinho quando executar o cod.

    elif opcao == 2:
        print("'Opção [2] Realizar Depósito' selecionada ... Digite o valor que deseja depositar: ")
        valor = float(input("Valor R$: "))
        saldo = saldo + valor
        print("Deposito realizado! Novo saldo: R$", saldo)
        print("\n") # usei somente para quebrar a linha no terminal, pra ficar mais separadinho quando executar o cod.
        
    elif opcao == 3:
        print("'Opção [3] Realizar Saque' selecionada ... Digite o valor que deseja sacar: ")
        print("Seu saldo atual é: R$", saldo)
        valor = float(input("Valor que deseja sacar: R$ "))
        print("\n") # usei somente para quebrar a linha no terminal, pra ficar mais separadinho quando executar o cod.
        if valor > saldo: 
            print("Atenção: Saldo insuficiente! Favor verificar o saldo disponível em conta. Caso deseje outros serviços, selecione uma das opções abaixo: ")
            print("\n") # usei somente para quebrar a linha no terminal, pra ficar mais separadinho quando executar o cod.    
        else:
            saldo = saldo - valor
            print("** Saque realizado. Aguarde a contagem das notas**")
            print("Seu saldo atual é: R$", saldo)
            print("\n") # usei somente para quebrar a linha no terminal, pra ficar mais separadinho quando executar o cod.
    elif opcao == 4:
        print(" * Opção [4] - Sair *  foi selecionada, portanto, estamos encerrando o antendimento... Obrigado por usar o Mota's Bank!")
        print("\n") # usei somente para quebrar a linha no terminal, pra ficar mais separadinho quando executar o cod.
        break
    else:
        print("Opção inválida!")
