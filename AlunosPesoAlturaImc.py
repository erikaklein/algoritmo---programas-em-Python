#Faça um programa que o usuário informe a quantidade de alunos de uma turma, o sistema deve ler o peso e altura de cada
# aluno, ao final informar o imc.



T= int(input("entre com a quantidade de alunos"))
x=0
soma=0
somapesos=0
somaltura=0


while (x<T):
    P= float(input("entre com o peso do aluno"))
    A= float(input("entre com a altura do aluno"))
    IMC=P/(A*A)
    print("IMC é ", IMC)
    x=x+1

    

