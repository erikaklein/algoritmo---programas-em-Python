def LerNumero():
    a=int(input("Digite um número inteiro: "))
    return(a)

def soma (a,b,c):
    return (a+b+c)

def media (a,b,c):
    return(soma(a,b,c)/3)

def maior (a,b,c):
    if a>b and a>c:
        M=a
    elif b>a and b>c:
        M=b
    elif c>a and c>b:
        M=c
    return (M)

def menor (a,b,c):
    if a<b and a<c:
        M=a
    elif b<a and b<c:
        M=b
    elif c<a and c<b:
        M=c
    return (M)


opcao=int(input("Selecione uma das opções =  Soma digite [1] -  Menor [2] - Maior[3] - Media [4]"))

n1=LerNumero()
n2=LerNumero()
n3=LerNumero()

if opcao==1:
    x=soma(n1,n2,n3)
    print ("A soma dos três números é: ",x)
if opcao==2:
    x=media(n1,n2,n3)
    print ("A média é: ",x)
if opcao==3:
    x=maior(n1,n2,n3)
    print ("O maior número é: ",x)
if opcao==4:
    x=menor(n1,n2,n3)
    print ("O menor número é: ",x)

