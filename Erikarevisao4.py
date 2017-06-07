#Altere os exercicios e armazene em um vetor as idades.

a=int(input("Digite quantas vezes vc quer informar a idade"))
i=0
n=[]


for i in range(a):
    n.append(int(input("Digite uma idade")))
    i=i+1
print (n)
