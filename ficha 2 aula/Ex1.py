#Exercício 1

numero1 = input("Ler primeiro número ")
numero2 = input("Ler segundo número ")

if numero1 == numero2:
    print("{} = {}".format(numero1,numero2))
elif numero1 > numero2:
    print("{} > {}".format(numero1,numero2))
else:
     print("{} < {}".format(numero1,numero2))