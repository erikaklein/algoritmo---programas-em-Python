#Utilizando a estrutura SE SENÃO, faça um algoritmo que deve possuir uma variável do tipo inteiro o ano de nascimento
# e a subtração pelo ano atual for menor que 18 informar a mensagem: "MENOR DE IDADE".'

n1=int(input("digite ano de nascimento"))
print(n1)
n2=int(input("digite ano atual"))
print(n2)
I=(n2-n1)
print(I)

if I<18:
    print("Menor de idade")
