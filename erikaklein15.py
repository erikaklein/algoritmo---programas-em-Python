#Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#Tabuada de 5:	5 X 1 = 5 5 X 2 = 1 5 X 10 = 50

L=int(input("Digite o valor"))
x=0

while (x<=10):
    #print (L, "x", x, "=", L*x)
    print("%d x%d=%d" %(L,x, L*x))
    x=x+1









