from board import Board

b = Board()

PLAYER_1 = 1
PLAYER_2 = 2

if __name__ == "__main__":
    b.initial_board()  
    while True:
        
        print("\nPlayer 1")
        print("enter x1 position")
        Wx1 = input()
        print("enter y1 position")
        Wy1 = input()
        print("enter x2 position")
        Wx2 = input()
        print("enter y2 position")
        Wy2 = input()

        while b.input_checker(PLAYER_1,Wx1,Wy1,Wx2,Wy2) == False:
            b.draw_board()
            print("\nPlayer 1")
            print("enter x1 position")
            Wx1 = input()
            print("enter y1 position")
            Wy1 = input()
            print("enter x2 position")
            Wx2 = input()
            print("enter y2 position")
            Wy2 = input()
        
        b.make_move(PLAYER_1,Wx1,Wy1,Wx2,Wy2)
        


        print("\nPlayer 2")
        print("enter x1 position")
        Bx1 = input()
        print("enter y1 position")
        By1 = input()
        print("enter x2 position")
        Bx2 = input()
        print("enter y2 position")
        By2 = input()

        while b.input_checker(PLAYER_2,Bx1,By1,Bx2,By2) == False:
            b.draw_board()
            print("\nPlayer 2")
            print("enter x1 position")
            Bx1 = input()
            print("enter y1 position")
            By1 = input()
            print("enter x2 position")
            Bx2 = input()
            print("enter y2 position")
            By2 = input()

        b.make_move(PLAYER_2,Bx1,By1,Bx2,By2)