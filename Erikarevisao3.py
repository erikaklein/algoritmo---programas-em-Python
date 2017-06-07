#Altere o algoritimo anterior e informe a maior e menor idade:

a=int(input("Digite quantas vezes vc quer informar a idade"))
i=0
M=0
m=1000


for i in range (a):
    n=int(input("Digite uma idade"))
    if (n>M):
        M=n
    if (n<m):
        m=n
print(M)
print(m)

