import os
import random
import time
os.system("cls")

vida_jogador = 100
vida_inimigo = 100

print("Bem vindo a batalha Pokémon em Python")

nome = input("Informe seu nome: ")

while(vida_jogador > 0 or vida_inimigo > 0):
    os.system("cls") #inserido aqui para limpar a tela 
    print(f"Vida: {vida_jogador}  |   Vida: {vida_inimigo}")

    print("Faça sua jogada")
    print("[1] - Atacar")
    print("[2] - Curar")
    print("[3] - Fugir")

    op_jogador = int(input("Escolha uma opção: "))

    #Atacou
    if(op_jogador == 1):
        vida_inimigo -= 10

    #Curou
    elif(op_jogador == 2):
        vida_jogador += 5

    #Fugiu
    elif(op_jogador == 3):
        print("Você fugiu!")

    print("Jogada encerrada... ")
    time.sleep (3)
    print("Iniciando a jogada em 3 segundos...")


    #Turno do inimigo
if(op_inimigo == 1)