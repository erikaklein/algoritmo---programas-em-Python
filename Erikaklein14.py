#Ler 10 números inteiros e identificar o maior

n=0
m=0
x=0

while(x<10):
    n=int(input ("entre com o número"))
    x=x+1
    if (n>m):
        m=n
print ("O maior número é: ", m)
