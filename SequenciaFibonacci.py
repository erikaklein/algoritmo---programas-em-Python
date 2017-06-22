#A seqüência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de
#formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a
#soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número
#de Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.


def fib(i):
    if i==1: return 0
    elif i==2: return 1
    else: return fib(i-1)+fib(i-2)

for i in range(1,11):
    print (fib(i))
