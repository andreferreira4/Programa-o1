#Exercicio 1

percnota1= .25
percnota2= .35
percnota3= .40

#Nota1
nota1 = float(input("Escreva a primeira nota: "))
while nota1 < 0.0 or nota1 > 20.0:
    nota1 = float(input("Escreva a primeira nota: "))

#Nota2
nota2 = float(input("Escreva a segunda nota: "))
while nota2 < 0.0 or nota2 > 20.0:
    nota2 = float(input("Escreva a segunda nota: "))

#Nota3
nota3 = float(input("Escreva a terceira nota: "))
while nota3 < 0.0 or nota3 > 20.0:
    nota3 = float(input("Escreva a terceira nota: "))

#Média
media = int((nota1 * percnota1 + nota2 * percnota2 + nota3 * percnota3))

if media >= 9.5 :
    print("Aprovado com {} (valor arredondado)".format(media))
else :
    print("Reprovado com {} (valor arredondado)".format(media))