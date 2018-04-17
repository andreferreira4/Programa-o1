#Exercício 4 

def imprimir_números(numero_max) :
    if numero_max >= 0:
        imprimir_números(numero_max - 1)
        print(numero_max, end=" ")
numero_max=int(input("Inserir número máximo: "))

imprimir_números(numero_max)