from pieces import Pawn
from pieces import Rook
from pieces import Bishop
from pieces import King
from pieces import Knight
from pieces import Queen
import os



class Board:
    def __init__(self):
        self.board = [
        [  Rook(0,0,"White", "♖")  ,  Bishop(0,1,"White", "♗")  ,  Knight(0,2,"White", "♘")  ,  Queen(0,3,"White", "♕")  ,  King(0,4,"White", "♔")  ,  Knight(0,5,"White", "♘")  ,  Bishop(0,6,"White", "♗")  ,  Rook(0,7,"White", "♖")  ],
        [  Pawn(1,0,"White", "♙")  ,  Pawn(1,1,"White", "♙")    ,  Pawn(1,2,"White", "♙")    ,  Pawn(1,3,"White", "♙")   ,  Pawn(1,4,"White", "♙")  ,  Pawn(1,5,"White", "♙")    ,  Pawn(1,6,"White", "♙")    ,  Pawn(1,7,"White", "♙")  ],
        [            "-"           ,             "-"            ,            "-"            ,            "-"            ,            "-"           ,            "-"             ,            "-"             ,            "-"           ],         
        [            "-"           ,             "-"            ,            "-"            ,            "-"            ,            "-"           ,            "-"             ,            "-"             ,            "-"           ],
        [            "-"           ,             "-"            ,            "-"            ,            "-"            ,            "-"           ,            "-"             ,            "-"             ,            "-"           ],
        [            "-"           ,             "-"            ,            "-"            ,            "-"            ,            "-"           ,            "-"             ,            "-"             ,            "-"           ],
        [  Pawn(6,0,"Black", "♟︎")  ,  Pawn(6,1,"Black", "♟︎")    ,  Pawn(6,2,"Black", "♟︎")    ,  Pawn(6,3,"Black", "♟︎")   ,  Pawn(6,4,"Black", "♟︎")  ,  Pawn(6,5,"Black", "♟︎")    ,  Pawn(6,6,"Black", "♟︎")    ,  Pawn(6,7,"Black", "♟︎")  ],
        [  Rook(7,0,"Black", "♜")  ,  Bishop(7,1,"Black", "♝")  ,  Knight(7,2,"Black", "♞")  ,  Queen(7,3,"Black", "♛")  ,  King(7,4,"Black", "♚")  ,  Knight(7,5,"Black", "♞")  ,  Bishop(7,6,"Black", "♝")  ,  Rook(7,7,"Black", "♜")  ],
    ]

    def make_move(self,player,x1,y1,x2,y2):
        x1 = int(x1)
        y1 = int(y1)
        if player == 1:
            if(self.board[x1][y1].color == "White"):
                self.board[x1][y1] == "-"
            else:
                return False
        elif player == 2:
            if(self.board[x1][y1].color == "Black"):
                self.board[x1][y1] == "-"
            else:
                print("play with your pieces only")

    def draw_board(self):
        os.system('clear')
        for i in range(len(self.board)):
            print("\n")
            for j in range(len(self.board[i])):
                if(self.board[i][j] == "-"):
                    print("-", end=" ")
                else:
                    print(self.board[i][j].label, end=" ")

        
        
