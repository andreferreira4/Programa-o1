file = open("ex1.txt", "r")

def ordenar(my_list):
    if len(my_list) > 1:
        mid = int(len(my_list)/2)
        left = my_list[:mid]
        right = my_list[mid:]
        # Split
        ordenar(left)
        ordenar(right)
        # sort
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        # left leftovers
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        # right leftovers
        while j < len(right):
            my_list[k] = right[j]
            j += 1
            k += 1


lista = []
linhas = file.readlines()
for i in linhas:
    i = int(i.split("\n")[0])
    lista.append(i)   

ordenar(lista)

print("Ordem Crescente: ")
for i in range(len(lista)):
    print(lista[i], end=" ")

print()
print("Ordem Decrescente: ")

for i in range(len(lista) - 1, -1, -1):
    print(lista[i], end=" ")

file.close()