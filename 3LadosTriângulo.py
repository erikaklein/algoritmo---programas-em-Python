#o sistema deve perguntar a medida dos 3 lados de um triangulo, o sistema deve informar o tipo de triangulo:
# equilatero, isosceles ou escaleno.

L1=int(input("Digite o lado 1 do triângulo"))
L2=int(input("Digite o lado 2 do triângulo"))
L3=int(input("Digite o lado 3 do triângulo"))

if L1==L2 & L1==L3:
    print ("Equilátero")
elif L1==L2 & L1!=L3:
    print ("Isósceles")
elif L1!=L2 & L1!=L3:
    print ("Escaleno")
