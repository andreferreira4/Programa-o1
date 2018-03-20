#Exercício 5

saldobancario = int(input("Escreva o saldo bancário "))
print("1 - Creditar")
print("2 - Debitar")
operacao = int(input("Escolha se quer debitar ou creditar "))
montante = int(input("Montante "))
if operacao == 2 :
    saldoapos = saldobancario - montante
    if saldoapos < 0:
        print("Operação impossivel")
    else:
        print("O saldo da conta bancária é de {} €".format(saldoapos))
if operacao == 1 :
    saldoapos = saldobancario + montante
    print("O saldo da conta bancária é de {} €".format(saldoapos))
