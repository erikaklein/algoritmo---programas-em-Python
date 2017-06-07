#2vetores
#login
#senhas
#Sortear um login exibir o login
#Um usuário deve digitar a senha correspondente ao login sorteado
#Se acertar, exibea msg: "Acesso liberado"
#O sistema só pode permitir 3 tentativas
from random import randint
login=["erika", "fabiano", "emmanuel", "alessandro"]
senha=["Erika123", "Fabiano123", "Emmanuel123", "Alessandro123"]
c=0
x=randint(0,3)
print(x)
print(login[x])

while (c<3):
    senha1=input("Digite a senha correspondente ao login sorteado")
    if senha1==senha[x]:
        print("Acesso liberado")
        break
    c=c+1







