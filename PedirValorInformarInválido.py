#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido.

n=int(input('entre com a nota'));

while n>10 or n<0:
    print ("valor inválido")
    n=int(input('repita a nota'));
if n<10 and n>0:
    print ("valor válido")

