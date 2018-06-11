from random import randint
Vezes = 10
file = open("lista_numero.txt","a")


for i in range(Vezes): 
    numero = str(randint(0, 9)) + "\n"
    file.write(numero)
file.close()