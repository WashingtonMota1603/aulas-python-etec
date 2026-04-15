# 17-semaforo.py

# Recebe a cor e padroniza para minúsculo
cor = input("Digite a cor do semáforo: ").lower()

if cor == "verde":
    print("Pode passar")
elif cor == "amarelo":
    print("Atenção")
elif cor == "vermelho":
    print("Pare")
else:
    print("Cor inválida")

