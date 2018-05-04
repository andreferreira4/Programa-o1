class jogador():
    
    def __init__(self):
        self.nome = ""
        self.token = ""
    def validar_jogador(self):
        while True:
            if jogador1.token != "X" or jogador1.token != "x" or jogador1.token != "O" or jogador1.token != "o":
                jogador1.token = input("Token que prente usar (X/O): ")   
            else:
                break
class tabuleiro():
    
    def printTabuleiro(self):
        print(' | A | B | C |')
        print( '--------------')
        print( '1| '   '  | '   '  | '   '  |')
        print( '--------------')
        print( '2| '   '  | '   '  | '   '  |') 
        print( '--------------')
        print( '3| '   '  | '   '  | '   '  |')
        print( '--------------')

tabuleiro1 = tabuleiro()
tabuleiro1.tabuleiro = [ ["A1", "A2", "A3"], 
                         ["B1", "B2", "B3"], 
                         ["C1", "C2", "C3"] ]
    
jogador1 = jogador()
jogador1.nome = input("Nome do jogador: ")
jogador1.token = input("Token que prente usar (X/O): ")

jogador2 = jogador()
jogador2.nome = input("Nome do jogador: ")
jogador2.token = input("Token que prente usar (X/O): ")

tabuleiro1.printTabuleiro()
jogador1.validar_jogador()


