from .pieces import Board


class Pawn(Board):
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color


    def valid_moves(self):
        valid = []
        if(self.color == "White"):
            pass

        return False
    # def __init__(self, x2, y2):
    #     self.x2 = x2
    #     self.y2 = y2

    # def rule(self,player,x1,y1):
    #     if player == 1:
    #         if (self.y2 - y1 == 2) and x1 == 1:
    #             return True
    #         elif (self.y2 - y1 == 1):
    #             return True
    #         else:
    #             print("pawn doesn't move like that")
    #             return False

    #     elif player == 2:
    #         if (self.y2 - y1 == -2) and x1 == 6:
    #             return True
    #         elif (self.y2 - y1 == -1):
    #             return True
    #         else:
    #             print("pawn doesn't move like that")
    #             return False


class Rook(Board):
    def __init__(self,x,y,color):
        self.position = (x,y)
        self.color = color
    
    def valid_moves(self):
        return False
    # def __init__(self, x2, y2):
    #     self.x2 = x2
    #     self.y2 = y2

    # def rule(self, x1, y1):
    #     if  (abs(self.x2 - x1) == 0) or (abs(self.y2 - y1) == 0):
    #         return True
    #     else:
    #         return False


class Knight(Board):
    def __init__(self,x,y,color):
        self.position = (x,y)
        self.color = color

    def valid_moves(self):
        return False
    # def __init__(self, x2, y2):
    #     self.x2 = x2
    #     self.y2 = y2

    # def rule(self, x1, y1):
    #     if (abs(self.y2 - y1) == 2 and abs(self.x2 - x1) == 1) or (abs(self.y2 - y1) == 1 and abs(self.x2 - x1) == 2):
    #         return True
    #     else:
    #         return False
            


class Bishop(Board):
    def __init__(self,x,y,color):
        self.position = (x,y)
        self.color = color

    def valid_moves(self):
        return False
    # def __init__(self, x2, y2):
    #     self.x2 = x2
    #     self.y2 = y2

    # def rule(self, x1, y1):
    #     if abs((x1 - self.x2) / (y1 - self.y2)):
    #         return True
    #     else:
    #         return False


class Queen(Board):
    def __init__(self,x,y,color):
        self.position = (x,y)
        self.color = color

    def valid_moves(self):
        return False
    # def __init__(self, x2, y2):
    #     self.x2 = x2
    #     self.y2 = y2

    # def rule(self, x1, y1):
    #     if (
    #         (abs((x1 - self.x2) / (y1 - self.y2)) == 1)
    #         or ((x1 - self.x2) == 0)
    #         or ((y1 - self.y2) == 0)
    #     ):
    #         return True
    #     else:
    #         return False


class King(Board):
    def __init__(self,x,y,color):
        self.position = (x,y)
        self.color = color

    def valid_moves(self):
        return False
        
    # def __init__(self, x2, y2):
    #     self.x2 = x2
    #     self.y2 = y2

    # def rule(self, x1, y1):
    #     if (self.x2 - x1 > 1) or (self.y2 - y1 > 1):
    #         return True
    #     else:
    #         return False

