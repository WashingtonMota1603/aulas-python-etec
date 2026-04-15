import os
os.system("cls")

#PRIMERIA ETAPA: REALIZAR AS ETAPAS
print("Seja bem vindo ao boletim virtual!")

nota01 = float(input("Entre com a primeira nota:"))
nota02 = float(input("Entre com a segunda nota:"))
nota03 = float(input("Entre com a terceira nota:"))

#SEGUNDA ETAPA: PROCESSAMENTO
media = (nota01 + nota02 + nota03) / 3
if(media >= 6):
    print("Você foi Aprovado!")
    
elif(media >= 4 and media <= 5):
    print("o aluno está de Recuperação!")
else:
    print("                            ***** Você está Reprovado... Se fudeuuuu, otário!*******")

# TERCEIRA EPATA: SAÍDA - EXIBIR O RESULTADO
print(f"Sua média foi", media)



