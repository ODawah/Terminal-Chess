class piece:
    def __init__(self, x, y, color,label):
        self.x = x
        self.y = y
        self.color = color
        self.label = label


class Blank(piece):
        def valid_moves(self):
            if(self.x in range(0, 8) and self.y in range(0, 8)):
                    pass
            else:
                return ("piece outside of the board")


class Pawn(piece):
    
    def valid_moves(self):
        valid = []

        if(self.color == "White"):
            if(self.x in range(0, 8) and self.y in range(0, 8)):
                if((self.x + 1) in range(self.x + 1, 8)):
                    valid.append((self.x + 1, self.y))
                    if((self.x + 2) in range(self.x, 8)):
                        valid.append((self.x + 2, self.y))
                return valid
            else:
                return ("piece outside of the board")

        elif(self.color == "Black"):
            if (self.x in range(0, 8) and self.y in range(0, 8)):
                if((self.x - 1) in range(0, 8)):
                    valid.append((self.x - 1, self.y))
                    if((self.x - 2) in range(0, 8)):
                        valid.append((self.x - 2, self.y))
                return valid
            else:
                return ("piece outside of the board")


class Rook(piece):

    def valid_moves(self):
        valid = []

        if(self.x in range(0, 8) and self.y in range(0, 8)):
            for i in [x for x in range(0, 8) if x != self.x]:
                valid.append((i, self.y))
            for j in range(0, 8):
                if(j == self.y):
                    continue
                else:
                    valid.append((self.x, j))
            
            return valid
        else:
            return ("piece outside of the board")


class Knight(piece):

    def valid_moves(self):
        valid = []

        X = [2, 1, -1, -2, -2, -1, 1, 2]
        Y = [1, 2, 2, 1, -1, -2, -2, -1]
        if self.x in range(0, 8) and self.y in range(0, 8):
            for i in range(0, 8):
                x2 = self.x + X[i]
                y2 = self.y + Y[i]
                if x2 in range(0, 8) and y2 in range(0, 8):
                    valid.append((x2, y2))

            return valid
        else:
            return ("piece outside of the board")


class Bishop(piece):

    def valid_moves(self):

        valid = []

        if(self.x in range(0, 8) and self.y in range(0, 8)):
            for i in range(1, 8):
                x2 = self.x + i 
                y2 = self.y + i
                if (x2 in range(0, 8)) and (y2 in range(0, 8)):
                    valid.append( (x2, y2) )
            
            for i in range(1, 8):
                x2 = self.x - i 
                y2 = self.y - i
                if (x2 in range(0, 8)) and (y2 in range(0, 8)):
                    valid.append( (x2, y2) )

            for i in range(1, 8):
                x2 = self.x + i 
                y2 = self.y - i
                if (x2 in range(0, 8)) and (y2 in range(0, 8)):
                    valid.append( (x2, y2) )
            
            for i in range(1, 8):
                x2 = self.x - i 
                y2 = self.y + i
                if (x2 in range(0, 8)) and (y2 in range(0, 8)):
                    valid.append( (x2, y2) )
            
            
                
            return valid
        else:
            return ("piece outside of the board")


class Queen(piece):

    def valid_moves(self):
        valid = []
        
        if(self.x in range(0, 8) and self.y in range(0, 8)):
            for i in [x for x in range(0, 8) if x != self.x]:
                valid.append((i, self.y))
            for j in range(0, 8):
                if(j == self.y):
                    continue
                else:
                    valid.append((self.x, j))
            for i in range(1, 8):
                x2 = self.x + i 
                y2 = self.y + i
                if (x2 in range(0, 8)) and (y2 in range(0, 8)):
                    valid.append( (x2, y2) )
            
            for i in range(1, 8):
                x2 = self.x - i 
                y2 = self.y - i
                if (x2 in range(0, 8)) and (y2 in range(0, 8)):
                    valid.append( (x2, y2) )

            for i in range(1, 8):
                x2 = self.x + i 
                y2 = self.y - i
                if (x2 in range(0, 8)) and (y2 in range(0, 8)):
                    valid.append( (x2, y2) )
            
            for i in range(1, 8):
                x2 = self.x - i 
                y2 = self.y + i
                if (x2 in range(0, 8)) and (y2 in range(0, 8)):
                    valid.append( (x2, y2) )



            return valid

        else:
           return ("piece outside of the board")



class King(piece):

    def valid_moves(self):

        valid = []

        if (self.x in range(0, 8) and self.y in range(0, 8)):
            if(self.x-1 in range(0, 8)):
                valid.append((self.x-1, self.y))
            if(self.x+1 in range(0, 8)):
                valid.append((self.x+1, self.y))

            if(self.y-1 in range(0, 8)):
                valid.append((self.x, self.y-1))
            if(self.y+1 in range(0, 8)):
                valid.append((self.x, self.y+1))

            if(self.y+1 in range(0, 8) and self.x+1 in range(0, 8)):
                valid.append((self.x+1, self.y+1))
            if(self.y-1 in range(0, 8) and self.x-1 in range(0, 8)):
                valid.append((self.x-1, self.y-1))

            if(self.y+1 in range(0, 8) and self.x-1 in range(0, 8)):
                valid.append((self.x-1, self.y+1))

            if(self.y-1 in range(0, 8) and self.x+1 in range(0, 8)):
                valid.append((self.x+1, self.y-1))

            return valid
        else:
            return ("piece outside of the board")
