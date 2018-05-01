#Execício 3

def adicionar(lista):
    for i in range(0,10):
        numero = float(input("Insira um número: "))
        lista.append(numero)
    print("Lista: ",lista)

def dobro(lista):
    Novalista = lista [:]
    for i in range(len(Novalista)):
        Novalista[i] *= 2
    print("O dobro de cada elemento, Lista: ",Novalista)

def soma(lista):
    soma = 0
    for i in lista:
        soma += i
    print("A soma dos elementos da lista é: ",soma)

def media(lista):
    soma = 0
    for i in lista:
        soma += i
        media = soma / len(lista)
    print("A média é: ", media)

def maior(lista):
    maior = max(lista)
    print("O maior número da lista é: ",maior)

def menor(lista):
    menor = min(lista)
    print("O maior número da lista é: ",menor)

lista = []

adicionar(lista)

dobro(lista)

soma(lista)

media(lista)

maior(lista)

menor(lista)
