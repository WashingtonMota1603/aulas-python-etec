import os
os.system("cls")

print("Exemplo com while - Salario do Professor")

resposta = "sim"

while True:
    os.system("cls")

    print("=== Menu ===")
    print("[1] - Calcular salario")
    print("[2] - Sair do programa")

    opcao= int(input("Escolha uma opção:"))

 #verificando qual foi a opção escolhida
    if(opcao == 1):
        os.system("cls")
        print("Qual e o nivel do professor: ")
        print("[1] - Nivel 1")
        print("[2] - Nivel 2")
        print("[3] - Nivel 3")
        
        nivel = int(input("Escolha um nivel:"))
        if(nivel >=4):
            print("Nivel inválido!")
            input("Pressione <enter> para continuar...")
            continue
        else:
            qtd_aulas = int(input("Informe a qtd de aulas mensais: "))

        if(nivel == 1):
            salario = qtd_aulas * 12
        elif(nivel == 2):
            salario = qtd_aulas * 17
        elif(nivel ==3):
             salario = qtd_aulas * 25
        else:
            print("Nivel invalido!")
            input("Pressione <ENTER> para continuar...")
            continue

        print(f"O salario do professor sera: {salario}")
        input("Pressione <ENTER> para continuar...")

    elif(opcao == 2):
        input("Pressione <ENTER> para continuar...")
        break
       
print("Finalizar o programa!")