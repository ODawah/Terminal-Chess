from src.rules import Pawn,Rook,Bishop,king,king,Knight,Queen

def example_pawn_data_W():
    p = Pawn(1,3,"White")

    return p.valid_moves

def example_pawn_data_B():
    p = Pawn(6,7,"Black")

    return p.valid_moves


def pawn_free_forward_W():

    assert example_pawn_data_W == [(2,3),(3,3)]

def pawn_one_forward_W():
    assert example_pawn_data_W == [(2,3)]

def pawn_cant_move_W():
    assert example_pawn_data_W == []

## vague
def pawn_eat_pawn_W():
    assert Pawn(2,3,"White") == [(3,2)]



def pawn_free_forward_B():

    assert example_pawn_data_B == [(5,7),(4,7)]

def pawn_one_forward_B():
    assert example_pawn_data_B == [(5,7)]

def pawn_cant_move_B():
    assert example_pawn_data_B == []

## vague
def pawn_eat_pawn_B():
    assert Pawn(5,7,"Black") == [(4,6)]

