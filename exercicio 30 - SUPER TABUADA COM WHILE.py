import os
os.system("cls")

print("Super Tabuada com While!")

numero = int(input("Digite um número: "))
contador = 0

while(contador <= 10):
    print(f"{numero} x {contador}= {numero * contador}") #eu poderia criar um tmb uma variavel "resultado = numero * contador" e adicionar a variavel resultado dps, ex: print(f"{numero} x {contador} = {resultado}")
    contador+=1