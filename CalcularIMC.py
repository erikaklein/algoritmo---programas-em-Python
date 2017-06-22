'''
faça um algorítimo para efetuar o cálculo do IMC, sabendo que é feito dividindo o peso (Em kg) e a altura (em metros) ao
quadrado:
'''

a=float(input ("Digite altura: "))
p =float(input("digite peso: "))
sx= input("digite seu sexo: f/m")
IMC= p/(a*a)
print (IMC)
if sx==("f"):
    if IMC>27.3:
        print ("acima do peso ideal")
    elif IMC>25.8:
        print ("marginalmente acima do peso")
    elif IMC>19.1:
        print ("no peso normal")
    elif IMC<19.1:
        print ("abaixo do peso")
if sx==("m"):
    if IMC>27.8:
        print ("acima do peso ideal")
    elif IMC>26.4:
        print ("marginalmente acima do peso")
    elif IMC>20.7:
        print ("no peso normal")
    elif IMC<20.7:
        print ("abaixo do peso")
