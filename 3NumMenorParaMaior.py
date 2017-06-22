#leia 3 numeros e coloque em ordem (do menor para o maior)


n1=int(input("digite o primeiro número"))
print(n1)
n2=int(input("digite o segundo número"))
print(n2)
n3=int(input("digite o terceiro número"))
print(n3)
if (n1<n2) & (n1<n3):
    if n2<n3:
        print (n1,n2,n3)
    else:
        print (n1,n3,n2)
if (n2<n1) & (n2<n3):
    if n1<n3:
        print(n2,n1,n3)
    else:
        print (n2,n3,n1)
if (n3<n1) & (n3<n2):
    if n1<n2:
        print (n3,n1,n2)
    else:
        print (n3,n2,n1)
