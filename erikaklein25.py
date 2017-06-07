#faça um algoritmo que receba 3 números inteiros e o usuário decida quais das opções o sistema deve retornar:
#	-a soma dos números
#	-o maior
#	-o menor
#	-a média


n1=int(input ("Digite o Número 1: "))
n2=int(input ("Digite o Número 2: "))
n3=int(input ("Digite o Número 3: "))
opcao=int(input("Selecione uma das opções =  Soma digite [1] -  Maior [2] - Menor[3] - Media [4]"))
r=(n1+n2+n3)
med=r/3

if n1>n2 and n1>n3:
    M=n1
if n2>n1 and n2>n3:
    M=n2
if n3>n1 and n3>n2:
    M=n3

if n1<n2 and n1<n3:
    m=n1
if n2<n1 and n2<n3:
    m=n2
if n3<n1 and n3<n2:
    m=n3

if opcao==1:
    print ("A soma dos três números é: ", r)
if opcao==2:
    print ("O maior número é: ", M)
if opcao==3:
    print ("O menor número é: ", m)
if opcao==4:
    print ("A média é: ", med)
