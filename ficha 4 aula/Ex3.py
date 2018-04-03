def imprima(min,max):
    numero = min - 1
    while numero < min or numero > max:
        numero = int(input("Inserir um número: "))
    return numero
valor_introduzido = imprima(0,20)

print(valor_introduzido)