#Exercício1

def login(inserir_login,inserir_password) :
    login = "aluno"
    password = "estg2018"
    if login == inserir_login and password == inserir_password:
        return True
    return False

def validarlogin() :
    contar = 0    
    while contar < 3:
        
        inserir_login=input("Insira o seu nome de utilizador ")
        inserir_password=input("Insira a sua password ")
        if login(inserir_login,inserir_password):
            print("Login realizado com sucesso")
            break
        else:
            print("O login não foi realizado com sucesso")
        contar += 1
    

validarlogin()
    