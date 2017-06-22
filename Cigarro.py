# sistema deve perguntar quantos cigarros a pessoa fuma por dia  e por quantos anos ela já fuma.
# Sabendo que cada cigarro se perde 10min de vida sistema deve calcular quantos dias de vida o fumante perderá.

Q= int(input("quantos cigarros vc fuma por dia?"))
A= float(input ("quantos anos vc já fuma?"))

A=Q*(A*365)
Qt=Q*A
print (Qt, "cigarros")

Qtm = Qt*10
print (Qtm, "minutos")

Qth= Qtm/60
print (Qth, "horas")

Qtd= Qth/24
print (Qtd, "dias perdidos de vida")




