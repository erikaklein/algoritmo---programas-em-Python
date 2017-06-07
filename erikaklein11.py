#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma=0
media=0
contador=0

for i in range(5):
    n=float(input("digite o número: "))
    soma=soma+n
    contador=contador+1
    media=(soma)/contador
print('A soma é:', soma)
print("A média é:", media)





