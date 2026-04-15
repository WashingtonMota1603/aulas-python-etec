# 10-tempo-estudo.py

# Solicita as horas e converte para número decimal (float)
horas = float(input("Quantas horas por dia você estuda? "))

if horas < 2:
    print("Pouco estudo")
elif horas <= 4:
    # Cai aqui se for entre 2 e 4 horas
    print("Estudo médio")
else:
    # Cai aqui se for maior que 4 horas
    print("Muito estudo")
