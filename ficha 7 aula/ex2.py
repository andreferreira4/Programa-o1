
from ex1 import Aluno

class Turma():
    
    def __init__(self, nome, ano): 
        self.nome = nome
        self.ano = ano
        self.lista = []
        self.numero_aluno = 0
    
    def inserir_aluno (self, numero):
        for i in range(self.lista):
            if numero in self.lista:
                print("O aluno já se encontra na turma")  
            else:  
                self.lista.append(numero)


turma1 = Turma("CRSIT2",2018)

turma1.inserir_aluno()