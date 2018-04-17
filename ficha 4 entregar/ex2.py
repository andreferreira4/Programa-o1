#Exercício2

taxa_de_converção_euro = 1.22958
taxa_de_converção_dólar = 0.81319

def converter_euro(quantidade):
    return ( quantidade * taxa_de_converção_euro)

def converter_dólar(quantidade):
    return ( quantidade * taxa_de_converção_dólar)

def inserir(opção,quantidade):
    if opção ==  "E" or opção =="e":
        resultado = converter_euro(quantidade)
        print("O resultado da sua converção é {} $".format(resultado))
    elif opção ==  "D" or opção =="d":
        resultado = converter_dólar(quantidade)
        print("O resultado da sua converção é {} €".format(resultado))

quantidade=float(input("Escolha a quantidade que quer converter "))
opção=input("Escolha a opção (E para converter de € para $) e (D para converter de $ para €) ")

inserir(opção,quantidade)