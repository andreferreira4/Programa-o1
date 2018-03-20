#Exercício 4

numero=int(input("Escreva um número "))
divisivel3= numero % 3
divisivel5= numero % 5
if divisivel3 == 0 and divisivel5 == 0 :
    print("O {} é divisível por 3 e 5".format(numero))
elif divisivel3 != 0 and divisivel5 != 0 :
    print("O {} não é divisível por 3 nem 5".format(numero))
elif divisivel5 != 0 :
    print("O {} não é divisível por 5 mas por 3 é ".format(numero))
elif divisivel3 != 0 :
    print("O {} não é divisível por 3 mas por 5 é ".format(numero))

