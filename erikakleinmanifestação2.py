from random import randint
l=[["erika", "fabiano", "emmanuel", "alessandro"],["Erika123", "Fabiano123", "Emmanuel123", "Alessandro123"]]

c=0
x=randint(0,3)
print(x)
print(l[0][x])
print(l[1][x])

while (c<3):
    senha1=input("Digite a senha correspondente ao login sorteado")
    if senha1==l[1][x]:
        print("Acesso liberado")
        break
    c=c+1

