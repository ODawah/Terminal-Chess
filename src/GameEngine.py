from board import Board

b = Board()

PLAYER_1 = 1
PLAYER_2 = 2

if __name__ == "__main__":
    while True:
        b.draw_board()

        print("\nPlayer 1")
        print("enter x1 position")
        x1 = input()
        print("enter y1 position")
        y1 = input()
        print("enter x2 position")
        x2 = input()
        print("enter y2 position")
        y2 = input()

        b.make_move(PLAYER_1,x1,y1,x2,y2)

        b.draw_board()
        print("\nPlayer 2")
        print("enter x1 position")
        x1 = input()
        print("enter y1 position")
        y1 = input()
        print("enter x2 position")
        x2 = input()
        print("enter y2 position")
        y2 = input()

        b.make_move(PLAYER_2,x1,y1,x2,y2)