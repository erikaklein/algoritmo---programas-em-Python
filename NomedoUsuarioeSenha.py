#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
# uma mensagem de erro e voltando a pedir as informações.

n=input('Digite o login');
s=input ('Entre com a senha')
while n==s:
    print ("Erro. Tente uma nova senha")
    n=input('Digite o login');
    s=input ('Entre com a senha')
