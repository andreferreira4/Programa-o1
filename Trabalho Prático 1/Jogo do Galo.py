
class jogador():
    
    def __init__(self, nome, token):
        
        self.nome = nome
        self.token = token

class tabuleiro():

    def __init__(self):
        self.tabuleiro = [["", "" , "" ], 
                          ["", "" ,"" ], 
                          ["", "" ,"" ]]
        self.token = ""
    
    def __str__(self):
        return ' |  A   |   B  |   C  |\n-----------------------------\n1|   {}   |   {}   |   {}   |\n-----------------------------\n2|   {}   |   {}   |   {}   |\n-----------------------------\n3|   {}   |   {}   |   {}   |\n-----------------------------'.format(self.tabuleiro[0][0], self.tabuleiro[0][1], self.tabuleiro[0][2],self.tabuleiro[1][0], self.tabuleiro[1][1], self.tabuleiro[1][2],self.tabuleiro[2][0], self.tabuleiro[2][1], self.tabuleiro[2][2])
    
    def validar_jogada(self,jogada,token):
        if (jogada[0] == "A" or jogada[0] == "B" or jogada[0] == "C") and (jogada[1] == "1" or jogada[1] == "2" or jogada[1] == "3"):
            if jogada[0] == "A":
                coluna = 0
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == "":
                    self.tabuleiro[linha][coluna] += token
                else:
                    jogada = input("Escreva a posição que pretende jogar (A1-C3)")
                    self.validar_jogada(jogada,token)
            if jogada[0] == "B":
                coluna = 1
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == "":
                    self.tabuleiro[linha][coluna] += token
                else:
                    jogada = input("Escreva a posição que pretende jogar (A1-C3)")
                    self.validar_jogada(jogada,token)
            if jogada[0] == "C":
                coluna = 2
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == "":
                    self.tabuleiro[linha][coluna] += token
                else:
                    jogada = input("Escreva a posição que pretende jogar (A1-C3)")
                    self.validar_jogada(jogada,token)
        else:
            jogada = input("Escreva a posição que pretende jogar (A1-C3)")
            self.validar_jogada(jogada,token)
    
    def vencedor(self,nome,token):
        if  (self.tabuleiro[0][0] == token and self.tabuleiro[0][1] == token and self.tabuleiro[0][2] == token) or \
            (self.tabuleiro[1][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[1][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[2][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[0][0] == token and self.tabuleiro[1][0] == token and self.tabuleiro[2][0] == token) or \
            (self.tabuleiro[0][1] == token and self.tabuleiro[1][1] == token and self.tabuleiro[2][1] == token) or \
            (self.tabuleiro[0][2] == token and self.tabuleiro[1][2] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[0][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[2][2] == token) or \
            (self.tabuleiro[2][0] == token and self.tabuleiro[1][1] == token and self.tabuleiro[0][2] == token):
            global vencedor
            vencedor = True
            return vencedor
jogador1nome = input("Nome do jogador: ")
jogador1token = input("Token que o jogador1 pretende usar: ")
jogador1 = jogador(jogador1nome, jogador1token)

jogador2nome = input("Nome do jogador: ")
jogador2token = input("Token que o jogador2 pretende usar: ")
jogador2 = jogador(jogador2nome, jogador2token)

while True:
    if jogador1token == jogador2token: 
        jogador2token = input("Token que o jogador 2 que prente usar: ")
    else:
        break

jogar = tabuleiro()
jogar.__str__()
print(jogador1.nome,jogador1.token,jogador2.nome,jogador2.token)

jogar = tabuleiro()
numero_max_jogadas = 0
vencedor = False
while numero_max_jogadas < 9 :
    jogada = input("Escreva a posição que pretende jogar (A1-C3)")
    jogar.validar_jogada(jogada,jogador1.token)
    print(jogar)
    jogar.vencedor(jogador1.nome,jogador1.token)
    if vencedor == True:
        print("O vencedor é o: ",jogador1.nome)
        break
    numero_max_jogadas += 1
    if numero_max_jogadas == 9:
        break
    jogada = input("Escreva a posição que pretende jogar (A1-C3)")
    jogar.validar_jogada(jogada,jogador2.token)
    print(jogar)
    jogar.vencedor(jogador2.nome,jogador2.token)
    if vencedor == True:
        print("O vencedor é o: ",jogador2.nome)
        break
    numero_max_jogadas += 1

if numero_max_jogadas == 9:
    print("empate")
