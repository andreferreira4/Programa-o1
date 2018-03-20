#Exercício2

Numero1 = int(input("Escreva o primeiro número "))
Numero2 = int(input("Escreva o segundo número "))
Numero3 = int(input("Escreva o terceiro número "))

if Numero1 > Numero2 and Numero2 > Numero3 :
    print("{} > {} > {}".format(Numero1,Numero2,Numero3))
elif Numero1 > Numero2 and Numero1 > Numero3 :
    print("{} > {} > {}".format(Numero1,Numero3,Numero2))
elif Numero2 > Numero1 and Numero1 > Numero3 :
    print("{} > {} > {}".format(Numero2,Numero1,Numero3))
elif Numero2 > Numero1 and Numero2 > Numero3 :
    print("{} > {} > {}".format(Numero2,Numero3,Numero1))
elif Numero3 > Numero2 and Numero2 > Numero1 :
    print("{} > {} > {}".format(Numero3,Numero2,Numero1))
elif Numero3 > Numero2 and Numero3 > Numero1 :
    print("{} > {} > {}".format(Numero3,Numero1,Numero2))

