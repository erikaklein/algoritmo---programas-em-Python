#Faça um algoritmo que o usuário infomre quantas idades serão informadas e exiba a maior.

a=int(input("Digite quantas vezes vc quer informar a idade"))
i=0
m=0

for i in range (a):
    n=int(input("Digite uma idade"))
    if (n>m):
        m=n
print(m)
