
class jogador():
    
    def __init__(self, nome, token): #A semelhança nesta classe com a dos meu colegas Diogo Neves e Carlos Antunes foi porque me ajudaram a difinir as classes        
        self.nome = nome
        self.token = token

class tabuleiro():

    def __init__(self):
        self.tabuleiro = [["", "" , "" ], 
                          ["", "" ,"" ], 
                          ["", "" ,"" ]]
    
    def __str__(self):
        return ' |  A   |   B  |   C  |\n-----------------------------\n1|   {}   |   {}   |   {}   |\n-----------------------------\n2|   {}   |   {}   |   {}   |\n-----------------------------\n3|   {}   |   {}   |   {}   |\n-----------------------------'.format(self.tabuleiro[0][0], self.tabuleiro[0][1], self.tabuleiro[0][2],self.tabuleiro[1][0], self.tabuleiro[1][1], self.tabuleiro[1][2],self.tabuleiro[2][0], self.tabuleiro[2][1], self.tabuleiro[2][2])
    #Função que nos permite verificar a jogada inserida pelo o jogador e inserir a mesma na lista
    def validar_jogada(self,jogada,token):
        if (jogada[0] == "A" or jogada[0] == "B" or jogada[0] == "C") and (jogada[1] == "1" or jogada[1] == "2" or jogada[1] == "3"):
            if jogada[0] == "A":
                coluna = 0
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == "":
                    self.tabuleiro[linha][coluna] += token
                else:
                    self.jogada = input("Escreva a posição que pretende jogar (A1-C3)")
                    self.validar_jogada(self.jogada,token)
            if jogada[0] == "B":
                coluna = 1
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == "":
                    self.tabuleiro[linha][coluna] += token
                else:
                    self.jogada = input("Escreva a posição que pretende jogar (A1-C3)")
                    self.validar_jogada(self.jogada,token)
            if jogada[0] == "C":
                coluna = 2
                linha = int(jogada [1]) - 1
                if self.tabuleiro[linha][coluna] == "":
                    self.tabuleiro[linha][coluna] += token
                else:
                    self.jogada = input("Escreva a posição que pretende jogar (A1-C3)")
                    self.validar_jogada(self.jogada,token)
        else:
            self.jogada = input("Escreva a posição que pretende jogar (A1-C3)")
            self.validar_jogada(self.jogada,token)
    #Função que permite verificar se existe vencedor do jogo
    def vencedor(self,nome,token): #A semelhança de termos separados as opçãos por linhas em vez de uma só deve-se à ajuda do João Gonçalves 
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

#Inserir dados do jogador1
jogador1nome = input("Nome do jogador: ")
jogador1token = input("Token que o jogador1 pretende usar: ")
jogador1 = jogador(jogador1nome, jogador1token)

#Inserir dados do jogador2
jogador2nome = input("Nome do jogador: ")
jogador2token = input("Token que o jogador2 pretende usar: ")

#Verificar e modificar se o token do jogador2 é igual ao jogador1
while True:
    if jogador1token == jogador2token: 
        jogador2token = input("Token que o jogador 2 que prente usar: ")
    else:
        jogador2 = jogador(jogador2nome, jogador2token)
        break

jogar = tabuleiro()
print(jogar)
print("Jogador1 {}: {} jogador2 {}: {}".format(jogador1.nome,jogador1.token,jogador2.nome,jogador2.token))

jogar = tabuleiro()
numero_max_jogadas = 0
vencedor = False
# Este ciclo serve para enquanto a 9 jogadas não forem jogadas ou não existir vencedor o programa continua a pedir jogadas aos utilizadores
while numero_max_jogadas < 9 :
    jogada = input("{}, escreva a posição que pretende jogar (A1-C3): ".format(jogador1.nome))
    if jogada == "Desistir" or jogada == "desistir":
        break
    jogar.validar_jogada(jogada,jogador1.token)
    print(jogar)
    jogar.vencedor(jogador1.nome,jogador1.token)
    if vencedor == True:
        print("O vencedor é o: ",jogador1.nome)
        break
    numero_max_jogadas += 1
    if numero_max_jogadas == 9:
        break
    jogada = input("{}, escreva a posição que pretende jogar (A1-C3): ".format(jogador2.nome))
    if jogada == "Desistir" or jogada == "desistir":
        break
    jogar.validar_jogada(jogada,jogador2.token)
    print(jogar)
    jogar.vencedor(jogador2.nome,jogador2.token)
    if vencedor == True:
        print("O vencedor é o: ",jogador2.nome)
        break
    numero_max_jogadas += 1

#Se as 9 jogadas forem feitas e não exister vencedor temos empate
if numero_max_jogadas == 9:
    print("empate")