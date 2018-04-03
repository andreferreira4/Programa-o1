def soma(numero1,numero2):
    return numero1 + numero2

def subtraçao(numero1,numero2):
    return numero1 - numero2

def mutiplicaçao(numero1,numero2):
    return numero1 * numero2

def divisao(numero1,numero2):
    return numero1 / numero2

numero1 = int(input("Inserir um número: "))

numero2 = int(input("Inserir um número: "))

operação = input("Escolha a operação aritemética (+,-,*,/):  ")

if operação == "+":
    resultado = soma(numero1,numero2)
    print("{} + {} = {} ".format(numero1,numero2,resultado))
elif operação == "-":
    resultado = subtraçao(numero1,numero2)
    print("{} - {} = {} ".format(numero1,numero2,resultado))
elif operação == "*":
    resultado = mutiplicaçao(numero1,numero2)
    print("{} * {} = {} ".format(numero1,numero2,resultado))
elif operação == "/":
    resultado = divisao(numero1,numero2)
    print("{} / {} = {} ".format(numero1,numero2,resultado))

