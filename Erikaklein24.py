#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

Vetor= []
Vetpar= []
Vetimpar=[]
i=20

for i in range (20):
    Vetor.append(i)
    print(Vetor [i])

    if Vetor [i] %2==0:
        Vetpar.append (Vetor [i])

    else:
        Vetimpar.append (Vetor [i])



print(Vetpar)
print(Vetimpar)
