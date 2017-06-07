'''
Elabore um algorítimo que dada a idade de um nadador classifica-o em uma das seguintes categorias:
Infantil A = 5-7anos
Infantil B = 8-10 anos
Juvenil A = 11-13 anos
Juvenil B = 14-17 anos
Adulto = maiores de 18 anos
'''

n=input ("Digite nome do nadador: ")
idade =int(input("digite idade do nadador: "))
print ("%s você tem %d anos"%(n,idade))
if idade>18:
    print ("maiores de 18 anos")
elif idade>=14:
    print ("Juvenil B")
elif idade>=11:
    print ("Juvenil A")
elif idade>=8:
    print ("Infantil B")
elif idade>=5:
    print ("Infantil A")
