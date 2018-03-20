#Exercício 3

numero=int(input("Escreva um número "))
resultado= numero % 2
if resultado == 0 :
    print("O {} é par".format(numero))
else:
    print("O {} é ímpar".format(numero))