#Exercício 1
from random import randint
import time
import re
def ValidarEmail(utilizador1_email):

    if len(utilizador1_email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", utilizador1_email) != None:
            return True
        return False
    if ValidarEmail("my.email@gmail.com") == True :
        print("This is a valid email address")
    else:
        print("This is not a valid email address")

class utilizador():
    def __init__(self):
        self.nome = ""
        self.email = ""
        self.password = ""
        self.identificador = ""
        self.resposta_secreta = ""
        self.data_criacao = ""
        self.bloquear = ""
    
    def login_utilizador(self):
        contar = 0
        if self.bloquear == True:
            resposta = input("Responder a pergunta de segurança: ")
            while resposta != self.resposta_secreta:
                resposta = input("Responder a pergunta de segurança: ")
            else:
                self.bloquear = False   
                utilizador1.login_utilizador()
        while contar < 3:
            login_email = input("Email: ")
            login_password = input("Password: ")
            if self.email == login_email and self.password == login_password:
                print("Parabéns você entrou")
                break
            else:
                print("Login errado!")
                contar += 1
        else:
            print("Utilizador bloqueado")
            self.bloquear = True
            utilizador1.login_utilizador()
                      
print("Introduzir dados para o utilizador1")
utilizador1 = utilizador()
utilizador1.nome = input("Nome de utilizador: ")
utilizador1.email = input("Email do utilizador: ")
utilizador1.password = input("Palavra-passe do utilizador: ")
utilizador1.identificador = "{}-{}".format(randint(100, 999),randint(1000, 9999))
utilizador1.resposta_secreta = input("Resposta secreta do utilizador: ")
utilizador1.data_criacao = time.strftime("%d/%m/%Y")

print("Introduzir dados para o utilizador2")
utilizador2 = utilizador()
utilizador2.nome = input("Nome de utilizador: ")
utilizador2.email = input("Email do utilizador: ")
utilizador2.password = input("Palavra-passe do utilizador: ")
utilizador2.identificador = "{}-{}".format(randint(100, 999),randint(1000, 9999))
utilizador2.resposta_secreta = input("Resposta secreta do utilizador: ")
utilizador2.data_de_criacao = time.strftime("%d/%m/%Y")

utilizador1.login_utilizador()