
class jogador():
    
    def __init__(self):
        self.nome = ""
        self.token = ""
class tabuleiro():

    def __init__(self):
        self.tabuleiro = [["", "" , "" ], 
                          ["", "" ,"" ], 
                          ["", "" ,"" ]]
        self.token = ""
    
    def __str__(self):
        print(' | A | B | C |')
        print( '-----------------------------')
        print( '1|  {}    |  {}    | {}     |'.format(self.tabuleiro[0][0], self.tabuleiro[0][1], self.tabuleiro[0][2]))
        print( '-----------------------------')
        print( '2|  {}    | {}     | {}     |'.format(self.tabuleiro[1][0], self.tabuleiro[1][1], self.tabuleiro[1][2]))
        print( '-----------------------------')
        print( '3| {}     | {}     | {}     |'.format(self.tabuleiro[2][0], self.tabuleiro[2][1], self.tabuleiro[2][2]))
        print( '-----------------------------')
    
jogador1 = jogador()
jogador1.nome = input("Nome do jogador: ")
jogador1.token = input("Token que o jogador1 pretende usar: ")

jogador2 = jogador()
jogador2.nome = input("Nome do jogador: ")
jogador2.token = input("Token que o jogador2 pretende usar: ")

while True:
    if jogador1.token == jogador2.token: 
        jogador2.token = input("Token que o jogador 2 que prente usar: ")
    else:
        break

tabuleiro1 = tabuleiro()
tabuleiro1.__str__()
print(jogador1.nome,jogador1.token,jogador2.nome,jogador2.token)

jogar = tabuleiro()
numero_max_jogadas = 9
while numero_max_jogadas <= 9:
    jogada = input("Escreva a posição que pretende jogar (A1-C3)")
    jogador1





