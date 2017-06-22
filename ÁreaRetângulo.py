#Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e escrever a área do retângulo
# , e caso seja um quadrado, exibir a frase: área de um quadrado.


B=int(input("digite a base: "))
A=int(input("digite a altura: "))
D=B*A
print(D)
if B==A:
    print ("área de um quadrado")
