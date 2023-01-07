class tictac:
    def __init__(self):
        self.board=[
        [1,1,1],
        [1,1,1],
        [1,1,1]]
    def place_xo(self,row,col,player):
        self.board[row][col]=player
    def showboard(self):
        for row in self.board:
            #for col in row:
            print(row,end="\n")
    def swap_player(self,player):
        return 'x' if player=='o' else 'o'
    def check_win(self,player):
        if self.board[0].count(player)==3 or self.board[1].count(player)==3 or self.board[2].count(player)==3:
            return player
        elif self.board[0][0]==player and self.board[1][0]==player and self.board[2][0]==player:
            return player
        elif self.board[0][1]==player and self.board[1][1]==player and self.board[2][1]==player:
            return player
        elif self.board[0][2]==player and self.board[1][2]==player and self.board[2][2]==player:
            return player
        elif self.board[0][0]==player and self.board[1][1]==player and self.board[2][2]==player:
            return player
        elif self.board[0][2]==player and self.board[1][1]==player and self.board[2][0]==player:
            return player
        else:
            print("continue")
    def checkfull(self):
        if self.board[0].count(1)==0 and self.board[1].count(1)==0 and self.board[2].count(1)==0 :
            return True
        else:
            return False
    def start(self):
        print("THE FIRST CHANCE GOES WITH PLAYER X")
        player='x'
        while True:
            self.showboard()
            print("\n")
            r=int(input("enter the row positon"))
            c=int(input("enter the column position"))
            self.place_xo(r-1,c-1,player)
            if self.check_win(player)=='x':
                print("congrats player X")
                break
            elif self.check_win(player)=='o':
                print("congrats player O")
                break
            else:
                pass
            player=self.swap_player(player)
            if self.checkfull():
                print("match draw !!")
                break

        self.showboard()
toe=tictac()
toe.start()	
