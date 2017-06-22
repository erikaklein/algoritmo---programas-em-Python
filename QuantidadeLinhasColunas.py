#faça um algoritmo que o usuário informe a quantidade de linhas e colunas que a matriz deve ter. O sistema deve criar
#a matriz atribuindo zero para cada campo

linha=int(input("linhas"))
colunas=int(input("colunas"))
m = [0]*linha
for i in range(linha):
    m[i] = [0]*colunas
print(m)








