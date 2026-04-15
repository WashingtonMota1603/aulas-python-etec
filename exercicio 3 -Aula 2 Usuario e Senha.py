#Faça um programa que solicite ao usuário um nome de usuário e uma senha.
#Caso o usuário seja admin e a senha 123 o programa deve exibir "Acesso liberado",
#caso contrário deve exibir "Acesso negado".

import os
os.system("cls")
print("Solicite ao usuário um nome de usuário e uma senha.")

# Entrada de dados
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Primeiro, verifica o usuário
if usuario == "admin":      # Aqui será veirifcado se o 
    if senha == "123":      # usuario e senha estão corretos. Se estiver, atenderá o print abaixo.
        print("Acesso liberado")
    else:                   # Se não estiverem corretos, será negado, conf.print abaixo.
        print("Acesso negado (senha incorreta)")
else:
    # Se o usuário não for 'admin', ele cai aqui direto
    print("Acesso negado (usuário inexistente)")


   




