#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa

vetor= [1.1,2.3,4.5,6.5,7.6,8.8,9.6,9.5,9.9,8.5]
i=10

for i in range (10):
    vetor = vetor + [i]
for i in range (9,-1,-1):
    print (vetor[i])



