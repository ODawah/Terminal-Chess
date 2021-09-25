from src.rules import Pawn,Rook,Bishop,King,Knight,Queen

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

#########################################

# Rook

def rook_blocked_intial():
    r = Rook(0,0,"White")
    assert r.valid_moves == []

def rook_mid_blocker():
    r = Rook(3,3,"White")
    assert r.valid_moves == [(2,3),(3,0),(3,1),(3,2),(3,4),(4,3),(5,3)]

def rook_mid_enemy():
    r = Rook(4,2,"Black")
    assert r.valid_moves == [(5,2),(4,0),(4,1),(3,2),(4,3),(4,4),(4,5),(4,6),(4,7)]

########################################

# King

def King_blocked():
    k = King(0,4,"White")
    assert k.valid_moves() == []

def King_blocked_move():
    k = King(6,4,"Black")
    assert k.valid_moves == [(7,4),(5,4),(5,5)]
#still searching for the rules



###########################################

# knight

def knight_free():
    n = Knight(4,3,"Black")
    assert n.valid_moves == [(2,4),(2,2),(3,5),(3,1)]

def knight_blocked():
    n = Knight(0,1,"White")
    assert n.valid_moves == []

def knight_blocked_path():
    n = Knight(3,3,"White")
    assert n.valid_moves == [(2,5),(5,2),(5,4)]

###########################################

# Bishop

def Bishop_blocked():
    b = Bishop(7,2,"Black")
    assert b.valid_moves == []

def Bishop_path_blocked():
    b = Bishop(3,7,"White")
    assert b.valid_moves == [(1,5),(4,6),(5,5)]
def Bishop_free():
    b = Bishop(3,5,"Black")
    assert b.valid_moves == [(2,6),(1,7),(4,4),(5,3),(2,4),(1,3),(4,6),(5,7)]

###########################################

# Queen

def queen_blocked():
    q = Queen(7,3,"Black")
    assert q.valid_moves == []

def queen_free():
    q = Queen(3,7,"White")
    assert q.valid_moves == [(2,7),(3,6),(3,5),(3,4),(3,3),(3,2),(3,1),(3,0),(4,7),(5,7),(6,7)]

def queen_path_limited():
    q = Queen(3,0,"Black")
    assert q.valid_moves == [(2,0),(1,0),(3,1),(3,2),(4,1),(5,2),(4,0),(5,0)]
