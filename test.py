from src import pieces


class Test_unit_pawn_white:
    def test_pawn_upleft_corner_W(self):
        p = pieces.Pawn(0, 0, "White")
        assert p.valid_moves() == [(1, 0), (2, 0)]

    def test_pawn_upright_corner_W(self):
        p = pieces.Pawn(0, 7, "White")
        assert p.valid_moves() == [(1, 7), (2, 7)]

    def test_pawn_downleft_one_corner_W(self):
        p = pieces.Pawn(6, 0, "White")
        assert p.valid_moves() == [(7, 0)]

    def test_pawn_downleft_two_corner_W(self):
        p = pieces.Pawn(5, 0, "White")
        assert p.valid_moves() == [(6, 0), (7, 0)]

    def test_pawn_downright_one_corner_W(self):
        p = pieces.Pawn(6, 7, "White")
        assert p.valid_moves() == [(7, 7)]

    def test_pawn_downright_two_corner_W(self):
        p = pieces.Pawn(5, 7, "White")
        assert p.valid_moves() == [(6, 7), (7, 7)]

    def test_pawn_outleft_W(self):
        p = pieces.Pawn(2, -2, "White")
        assert p.valid_moves() == ("piece outside of the board")

    def test_pawn_outright_W(self):
        p = pieces.Pawn(0, 9, "White")
        assert p.valid_moves() == ("piece outside of the board")

    def test_pawn_outup_W(self):
        p = pieces.Pawn(-3, 2, "White")
        assert p.valid_moves() == ("piece outside of the board")

    def test_pawn_outdown_W(self):
        p = pieces.Pawn(10, 2, "White")
        assert p.valid_moves() == ("piece outside of the board")

    def test_pawn_free_forward_W(self):
        p = pieces.Pawn(3, 3, "White")
        assert p.valid_moves() == [(4, 3), (5, 3)]
    
    def test_pawn_blocked_W(self):
        p = pieces.Pawn(7, 3, "White")
        assert p.valid_moves() == []


class Test_unit_pawn_black:
    def test_pawn_downleft_corner_B(self):
        p = pieces.Pawn(7,0,"Black")
        assert p.valid_moves() == [(6,0),(5,0)]
    
    def test_pawn_downright_corner_B(self):
        p = pieces.Pawn(7,7,"Black")
        assert p.valid_moves() == [(6,7),(5,7)]
    
    def test_pawn_upleft_one_corner_B(self):
        p = pieces.Pawn(1,0,"Black")
        assert p.valid_moves() == [(0,0)]

    def test_pawn_upleft_two_corner_B(self):
        p = pieces.Pawn(2,0,"Black")
        assert p.valid_moves() == [(1,0),(0,0)]

    def test_pawn_upright_one_corner_B(self):
        p = pieces.Pawn(1,7,"Black")
        assert p.valid_moves() == [(0,7)]
    
    def test_pawn_upright_two_corner_B(self):
        p = pieces.Pawn(2,7,"Black")
        assert p.valid_moves() == [(1,7),(0,7)]

    def test_pawn_outleft_B(self):
        p = pieces.Pawn(5, -2, "Black")
        assert p.valid_moves() == ("piece outside of the board")

    def test_pawn_outright_B(self):
        p = pieces.Pawn(7, 9, "Black")
        assert p.valid_moves() == ("piece outside of the board")

    def test_pawn_outup_B(self):
        p = pieces.Pawn(-3, 2, "Black")
        assert p.valid_moves() == ("piece outside of the board")

    def test_pawn_outdown_B(self):
        p = pieces.Pawn(10, 2, "Black")
        assert p.valid_moves() == ("piece outside of the board")

    def test_pawn_free_forward_B(self):
        p = pieces.Pawn(6, 5, "Black")
        assert p.valid_moves() == [(5, 5), (4, 5)]

    def test_pawn_blocked_B(self):
        p = pieces.Pawn(0,3,"Black")
        assert p.valid_moves() == []



#########################################

# Rook

def test_rook_blocked_intial():
    r = pieces.Rook(0, 0, "White")
    assert r.valid_moves == []


def test_rook_mid_blocker():
    r = pieces.Rook(3, 3, "White")
    assert r.valid_moves == [(2, 3), (3, 0), (3, 1),
                             (3, 2), (3, 4), (4, 3), (5, 3)]


def test_rook_mid_enemy():
    r = pieces.Rook(4, 2, "Black")
    assert r.valid_moves == [(5, 2), (4, 0), (4, 1),
                             (3, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]

########################################

# King


def King_blocked():
    k = pieces.King(0, 4, "White")
    assert k.valid_moves() == []


def King_blocked_move():
    k = pieces.King(6, 4, "Black")
    assert k.valid_moves == [(7, 4), (5, 4), (5, 5)]
# still searching for the rules


###########################################

# knight

def test_knight_free():
    n = pieces.Knight(4, 3, "Black")
    assert n.valid_moves == [(2, 4), (2, 2), (3, 5), (3, 1)]


def test_knight_blocked():
    n = pieces.Knight(0, 1, "White")
    assert n.valid_moves == []


def test_knight_blocked_path():
    n = pieces.Knight(3, 3, "White")
    assert n.valid_moves == [(2, 5), (5, 2), (5, 4)]

###########################################

# Bishop


def test_Bishop_blocked():
    b = pieces.Bishop(7, 2, "Black")
    assert b.valid_moves == []


def test_Bishop_path_blocked():
    b = pieces.Bishop(3, 7, "White")
    assert b.valid_moves == [(1, 5), (4, 6), (5, 5)]


def test_Bishop_free():
    b = pieces.Bishop(3, 5, "Black")
    assert b.valid_moves == [(2, 6), (1, 7), (4, 4),
                             (5, 3), (2, 4), (1, 3), (4, 6), (5, 7)]

###########################################

# Queen


def test_queen_blocked():
    q = pieces.Queen(7, 3, "Black")
    assert q.valid_moves == []


def test_queen_free():
    q = pieces.Queen(3, 7, "White")
    assert q.valid_moves == [(2, 7), (3, 6), (3, 5), (3, 4),
                             (3, 3), (3, 2), (3, 1), (3, 0), (4, 7), (5, 7), (6, 7)]


def test_queen_path_limited():
    q = pieces.Queen(3, 0, "Black")
    assert q.valid_moves == [(2, 0), (1, 0), (3, 1),
                             (3, 2), (4, 1), (5, 2), (4, 0), (5, 0)]
