#Exercício 2

def adicionar(lista):
    for i in range(0,10):
        carater = input("Insira um carater: ")
        lista.append(carater)
    print("Lista: ",lista)

def contar_posição(lista):
    ver_carater = input("Carater: ")
    contar = lista.count(ver_carater)
    print("O {} existe: {} vezes.".format(ver_carater,contar)) 
    for i,j in enumerate(lista):
        if j == ver_carater:
            print("O {} encontra-se na posição {} .".format(j,i))

lista = []

adicionar(lista)

contar_posição(lista)

