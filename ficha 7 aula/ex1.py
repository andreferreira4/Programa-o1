#Exercício1

class Aluno():
    
    def __init__(self, numero, nome): 
        self.numero = numero
        self.nome = nome
    
    def __str__(self):
       return "O nome do aluno é {} e o seu número é o {}".format(self.nome.title(),self.numero)

    
if __name__ == "__main__":
    aluno1 = Aluno(1, "andré ferreira")
    print(aluno1)

    aluno2 = Aluno(2, "carlos gomes")
    print(aluno2)


