from pieces import Pawn
from pieces import Rook
from pieces import Bishop
from pieces import King
from pieces import Knight
from pieces import Queen
from pieces import Blank
import os



class Board:
    def __init__(self):
        # TODO (omardawah) : Change blank tiles into Piece:Blank
        self.board = [
        [  Rook(0, 0, "White", "♖")  ,  Bishop(0, 1, "White", "♗")  ,  Knight(0, 2, "White", "♘")  ,  Queen(0, 3, "White", "♕")  ,  King(0, 4, "White", "♔")  ,  Knight(0, 5, "White", "♘")  ,  Bishop(0, 6, "White", "♗")  ,  Rook(0, 7, "White", "♖") ],
        [  Pawn(1, 0, "White", "♙")  ,  Pawn(1, 1, "White", "♙")    ,  Pawn(1, 2, "White", "♙")    ,  Pawn(1, 3, "White", "♙")   ,  Pawn(1, 4, "White", "♙")  ,  Pawn(1, 5, "White", "♙")    ,  Pawn(1, 6, "White", "♙")    ,  Pawn(1, 7, "White", "♙") ],
        [  Blank(2, 0, "blank", "-")  ,  Blank(2, 1, "blank", "-")    ,  Blank(2, 2, "blank", "-")   ,   Blank(2, 3, "blank", "-")   , Blank(2, 4, "blank", "-")  ,  Blank(2, 5, "blank", "-")    ,  Blank(2, 6, "blank", "-")   ,   Blank(2, 7, "blank", "-") ],         
        [  Blank(3, 0, "blank", "-")  ,  Blank(3, 1, "blank", "-")    ,  Blank(3, 2, "blank", "-")   ,   Blank(3, 3, "blank", "-")   , Blank(3, 4, "blank", "-")  ,  Blank(3, 5, "blank", "-")    ,  Blank(3, 6, "blank", "-")   ,   Blank(3, 7, "blank", "-") ],
        [  Blank(4, 0, "blank", "-")  ,  Blank(4, 1, "blank", "-")    ,  Blank(4, 2, "blank", "-")   ,   Blank(4, 3, "blank", "-")   , Blank(4, 4, "blank", "-")  ,  Blank(4, 5, "blank", "-")    ,  Blank(4, 6, "blank", "-")    ,  Blank(4, 7, "blank", "-") ],
        [  Blank(5, 0, "blank", "-")  ,  Blank(5, 1, "blank", "-")    ,  Blank(5, 2, "blank", "-")   ,   Blank(5, 3, "blank", "-")   , Blank(5, 4, "blank", "-")  ,  Blank(5, 5, "blank", "-")    ,  Blank(5, 6, "blank", "-")    ,  Blank(5, 7, "blank", "-") ],
        [  Pawn(6, 0, "Black", "♟︎")  ,  Pawn(6, 1, "Black", "♟︎")    ,  Pawn(6, 2, "Black", "♟︎")    ,  Pawn(6, 3, "Black", "♟︎")   ,  Pawn(6, 4, "Black", "♟︎")  ,  Pawn(6, 5, "Black", "♟︎")    ,  Pawn(6 ,6, "Black", "♟︎")    ,  Pawn(6, 7, "Black", "♟︎") ],
        [  Rook(7, 0, "Black", "♜")  ,  Bishop(7, 1, "Black", "♝")  ,  Knight(7, 2, "Black", "♞")  ,  Queen(7, 3, "Black", "♛")  ,  King(7, 4, "Black", "♚")  ,  Knight(7, 5, "Black", "♞")  ,  Bishop(7, 6, "Black", "♝")  ,  Rook(7, 7, "Black", "♜") ],
    ]

        self.colors = {
            'Player 1 (White)': "White",
            'Player 2 (Black)': "Black"
        }

    def inboard(self, p):
        for i in p:
            if i > 7 or i < 0:
                return False
        return True
    
    def clear_path(self, start, end):
        x1, y1 = start
        x2, y2 = end
        if self.board[x1][y1].color == self.board[x2][y2].color:
            return False
        if self.board[x1][y1].label == ("♙" or "♟︎"):
            moves = self.board[x1][y1].valid_moves()
            if (x2, y2) in moves:
                for i in range(0,2):
                    e1 = moves[i][0]
                    e2 = moves[i][1]
                    if self.board[e1][e2].label != "-":
                        print(e1)
                        print(e2)
                        return False
                return True
        else:
            return True
            


    def make_move(self, player, src, dist):
        current_board = self.board
        x1, y1 = src
        x2, y2 = dist
        
        if current_board[x1][y1].color != self.colors[player]:
            return self.board, False , "you can play with your pieces only"


        if not self.inboard([x1, y1, x2, y2]):
            return self.board, False , "you choosed tile outside of the board"
        
        if not self.clear_path((x1, y1), (x2, y2)):
            return self.board, False, "your destination is blocked"
        # check clear path


        current_board[x2][y2] = current_board[x1][y1]
        current_board[x2][y2].x, current_board[x2][y2].y = x2, y2
        current_board[x1][y1] = Blank(x1, y1, "blank", "-")
        return current_board, True, ""
        
        

    def draw_board(self):
        os.system('clear')
        for i in range(len(self.board)):
            print("\n")
            for j in range(len(self.board[i])):
                if(self.board[i][j] == "-"):
                    print("-", end=" ")
                else:
                    print(self.board[i][j].label, end=" ")

    def initial_board(self):
        os.system('clear')
        for i in range(len(self.board)):
            print("\n")
            for j in range(len(self.board[i])):
                if(self.board[i][j] == "-"):
                    print("-", end=" ")
                else:
                    print(self.board[i][j].label, end=" ")
    
    def input_checker(self,player,x1,y1,x2,y2):
        x1 = int(x1)
        x2 = int(x2)
        y1 = int(y1)
        y2 = int (y2)
        if player == 1:
                if self.board[x1][y1] == "-" or self.board[x1][y1].color == "Black":
                    
                    return False
                else:
                    return True
        elif player == 2:
                if self.board[x1][y1] == "-" or self.board[x1][y1].color == "White":
                    print("play with your pieces")
                    return False
                else:
                    return True
    
    def board_change(self,x1,y1,x2,y2):
        self.board[x1][y1] = "-"

        piece_type = type(self.board[x1][y1])
        print(piece_type.__name__)

    def piece_type(self,x1,y1,x2,y2):
        
        print(type(self.board[x1][y1]))

        
