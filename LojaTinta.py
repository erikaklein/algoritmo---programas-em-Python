#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a
#ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
#em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem
#compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas.

L=80
b=54
A = float(input("Digite o tamanho em m²:"))
u=A//b
i=A%b

if A<b:
    print("Quantidade de latas a serem compradas: 1")
    print("Preço: R$ 80,00")

if A>b and i==0:
    print("Quantidade de latas a serem compradas é de: ", u)
    v= u*L
    print ("O valor a ser pago é: ", v)

elif A>b and i>=1:
    u=u+1
    print("Quantidade de latas a serem compradas é de: ", u)
    v= u*L
    print("O valor a ser pago é: ", v)







