#Exercício4

nota1 = float(input("Escreva a primeira nota: "))
nota2 = float(input("Escreva a segunda nota: "))
nota3 = float(input("Escreva a terceira nota: "))

media =float((nota1 * 25 + nota2 * 35 + nota3 * 40) /100)
media_inteira = int((nota1 * 25 + nota2 * 35 + nota3 * 40) //100)
media_modulo = int((nota1 * 25 + nota2 * 35 + nota3 * 40)%100)
print("A média das notas é: {}\n A média inteira é: {}\n O resto da média é {}".format(media,media_inteira,media_modulo))