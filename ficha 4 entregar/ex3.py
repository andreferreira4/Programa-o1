#Exercício3

def desenhar(carater,linha,coluna) :
    for i in range(linha):
        if i == 0 or i == linha - 1 :
            print(carater * coluna)
        else:
            print(carater + " "*(coluna - 2) + carater)
carater = input("Escreva o carater a ser utilizado: ")
linha = int(input("Escreva o número de linhas a ser utilizado: "))
coluna = int(input("Escreva o número de colunas a ser utilizado: "))

desenhar(carater,linha,coluna)