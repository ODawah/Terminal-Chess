from board import Board

b = Board()

PLAYER_1 = "Player 1 (White)"
PLAYER_2 = "Player 2 (Black)"


def user_input(player_name):
    while True:
        print(f"\n{player_name} move: 1(comma seprated)\n")
        i = input()
        try:
            x1, y1, x2, y2 = [int(i.strip()) for i in i.split(",")]
            return (x1, y1), (x2, y2)
        except Exception as e:
            continue


if __name__ == "__main__":
    b.initial_board()  
    while True: # game loop
        
        while True:
            src, dest = user_input("Player 1 (White)")
            b.board, changed, er = b.make_move(PLAYER_1, src, dest)
            if changed:
                break
            b.draw_board()
            print(er)

        b.draw_board()
        # check ended
        # check mate
        # check blocked

        while True:
            src, dest = user_input("Player 2 (Black)")
            b.board, changed, er = b.make_move(PLAYER_2, src, dest)
            if changed:
                break
            b.draw_board()
            print(er)



        b.draw_board()  
        # check ended
        # check mate
        # check blocked
