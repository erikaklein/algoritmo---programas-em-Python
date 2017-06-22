#Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
#algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
#os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
#nenhuma delas esteja em falta no cai


conta=int(input("Digite o valor da conta :  "))
pagamento=int(input("Digite o valor do do pagamento :  "))
troco=pagamento-conta
print (troco, "reais")

notas=[50,20,10,5,2,1]
i=0
while troco>0:
    n=troco/notas[i]
    troco=troco%notas[i]
    if int(n) != 0:
        print('%d nota(s) de R$ %.2f' %(n, notas[i]))
    i=i+1
