#Atividade 2:
#Faça um algoritmo que leia dois números inteiros e exiba a média aritmética e exiba as mensagens a seguir
# de acordo com a média calculada.
#entre 0 e 5,9 - Insuficiente
#entre 6 e 6,9 - suficiente
#entre 7 e 8,9 - Bom
#entre 9 e 10 - Ótimo

n1=int(input("Digite um número:"))
print(n1)
n2=int(input("Digite um número:"))
print(n2)
M=(n1+n2)/2
print(M)

if M>=9:
    print("Ótimo")
elif M>=7:
    print("Bom")
elif M>=6:
    print("Suficiente")
elif M>=0:
    print("Insufiente")
