# O .lower() converte a entrada para minúsculo logo de cara
usuario = input("Digite o nome de usuário: ").lower()
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "123":
    print("Acesso liberado")
elif usuario != "admin":
    print("Acesso negado: Usuário incorreto")
else:
    print("Acesso negado: Senha incorreta")
