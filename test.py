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
        p = pieces.Pawn(7, 0, "Black")
        assert p.valid_moves() == [(6, 0), (5, 0)]

    def test_pawn_downright_corner_B(self):
        p = pieces.Pawn(7, 7, "Black")
        assert p.valid_moves() == [(6, 7), (5, 7)]

    def test_pawn_upleft_one_corner_B(self):
        p = pieces.Pawn(1, 0, "Black")
        assert p.valid_moves() == [(0, 0)]

    def test_pawn_upleft_two_corner_B(self):
        p = pieces.Pawn(2, 0, "Black")
        assert p.valid_moves() == [(1, 0), (0, 0)]

    def test_pawn_upright_one_corner_B(self):
        p = pieces.Pawn(1, 7, "Black")
        assert p.valid_moves() == [(0, 7)]

    def test_pawn_upright_two_corner_B(self):
        p = pieces.Pawn(2, 7, "Black")
        assert p.valid_moves() == [(1, 7), (0, 7)]

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
        p = pieces.Pawn(0, 3, "Black")
        assert p.valid_moves() == []


#########################################

# Rook
class Test_unit_rook():
    def test_rook_upleft_corner_W(self):
        r = pieces.Rook(0, 0, "White")
        assert r.valid_moves() == [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (
            0, 6), (0, 7)]

    def test_rook_upleft_corner_B(self):
        r = pieces.Rook(0, 0, "Black")
        assert r.valid_moves() == [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (
            0, 6), (0, 7)]

    def test_rook_upright_corner_W(self):
        r = pieces.Rook(0, 7, "White")
        assert r.valid_moves() == [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0, 0), (
            0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]

    def test_rook_upright_corner_B(self):
        r = pieces.Rook(0, 7, "Black")
        assert r.valid_moves() == [(1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (0, 0), (
            0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]

    def test_rook_downright_corner_W(self):
        r = pieces.Rook(7, 7, "White")
        assert r.valid_moves() == [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (
            5, 7), (6, 7), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)]

    def test_rook_downright_corner_B(self):
        r = pieces.Rook(7, 7, "Black")
        assert r.valid_moves() == [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (
            5, 7), (6, 7), (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6)]

    def test_rook_downleft_corner_W(self):
        r = pieces.Rook(7, 0, "White")
        assert r.valid_moves() == [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (
            7, 6), (7, 7)]

    def test_rook_downleft_corner_B(self):
        r = pieces.Rook(7, 0, "B")
        assert r.valid_moves() == [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (
            7, 6), (7, 7)]

    def test_rook_middle_left_W(self):
        r = pieces.Rook(3, 0, "White")
        assert r.valid_moves() == [(0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (
            6, 0), (7, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)]

    def test_rook_middle_left_B(self):
        r = pieces.Rook(3, 0, "Black")
        assert r.valid_moves() == [(0, 0), (1, 0), (2, 0), (4, 0), (5, 0), (
            6, 0), (7, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)]

    def test_rook_middle_right_W(self):
        r = pieces.Rook(3, 7, "White")
        assert r.valid_moves() == [(0, 7), (1, 7), (2, 7), (4, 7), (5, 7), (
            6, 7), (7, 7), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)]

    def test_rook_middle_right_B(self):
        r = pieces.Rook(3, 7, "Black")
        assert r.valid_moves() == [(0, 7), (1, 7), (2, 7), (4, 7), (5, 7), (
            6, 7), (7, 7), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6)]

    def test_rook_outleft_B(self):
        r = pieces.Rook(5, -2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_rook_outleft_W(self):
        r = pieces.Rook(5, -2, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_rook_outright_B(self):
        r = pieces.Rook(7, 9, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_rook_outright_W(self):
        r = pieces.Rook(7, 9, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_rook_outup_B(self):
        r = pieces.Rook(-3, 2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_rook_outup_W(self):
        r = pieces.Rook(-3, 2, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_rook_outdown_B(self):
        r = pieces.Rook(10, 2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_rook_outdown_W(self):
        r = pieces.Rook(10, 2, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_rook_middle_B(self):
        r = pieces.Rook(4, 4, "Black")
        assert r.valid_moves() == [(0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (
            6, 4), (7, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7)]

    def test_rook_middle_W(self):
        r = pieces.Rook(4, 4, "White")
        a = r.valid_moves()
        b = [
            (6, 4), (0, 4), (1, 4), (2, 4), (3, 4), (5, 4), (7, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7)]
        diff  = set(a) ^ set(b)
        assert not diff 


########################################

# King

class Test_unit_king:

    def test_King_upleft_corner_W(self):
        k = pieces.King(0, 0, "White")
        a = k.valid_moves() 
        b = [(0, 1), (1, 1), (1, 0)]
        diff  = set(a) ^ set(b)
        assert not diff

    def test_King_upleft_corner_B(self):
        k = pieces.King(0, 0, "Black")
        a = k.valid_moves() 
        b = [(0, 1), (1, 1), (1, 0)]
        diff  = set(a) ^ set(b)
        assert not diff

    def test_King_upright_corner_W(self):
        k = pieces.King(0, 7, "White")
        a = k.valid_moves()
        b = [(1, 7), (0, 6), (1, 6)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_King_upright_corner_B(self):
        k = pieces.King(0, 7, "Black")
        a = k.valid_moves()
        b = [(1, 7), (0, 6), (1, 6)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_King_downleft_corner_W(self):
        k = pieces.King(7, 0, "White")
        a = k.valid_moves() 
        b = [(7, 1), (6, 1), (6, 0)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_King_downleft_corner_B(self):
        k = pieces.King(7, 0, "Black")
        a = k.valid_moves() 
        b = [(7, 1), (6, 1), (6, 0)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_King_downright_corner_W(self):
        k = pieces.King(7, 7, "White")
        a = k.valid_moves() 
        b = [(7, 6), (6, 6), (6, 7)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_King_downright_corner_B(self):
        k = pieces.King(7, 7, "Black")
        a = k.valid_moves() 
        b = [(7, 6), (6, 6), (6, 7)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_king_midright_W(self):
        k = pieces.King(3, 7, "White")
        a = k.valid_moves()
        b = [(2, 7), (2, 6), (3, 6), (4, 6), (4, 7)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_king_midright_B(self):
        k = pieces.King(3, 7, "Black")
        a = k.valid_moves()
        b = [(2, 7), (2, 6), (3, 6), (4, 6), (4, 7)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_king_midleft_W(self):
        k = pieces.King(4, 0, "White")
        a = k.valid_moves()
        b = [(3, 0), (3, 1), (4, 1), (5, 1), (5, 0)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_king_midleft_B(self):
        k = pieces.King(4, 0, "Black")
        a = k.valid_moves()
        b = [(3, 0), (3, 1), (4, 1), (5, 1), (5, 0)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_king_middle_W(self):
        k = pieces.King(4, 3, "White")
        a = k.valid_moves()
        b = [(3, 3), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (4, 2), (3, 2)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_king_middle_B(self):
        k = pieces.King(4, 3, "Black")
        a = k.valid_moves()
        b = [(3, 3), (3, 4), (4, 4), (5, 4), (5, 3), (5, 2), (4, 2), (3, 2)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_King_outleft_B(self):
        r = pieces.King(5, -2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_King_outleft_W(self):
        r = pieces.King(5, -2, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_King_outright_B(self):
        r = pieces.King(7, 9, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_King_outright_W(self):
        r = pieces.King(7, 9, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_King_outup_B(self):
        r = pieces.King(-3, 2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_King_outup_W(self):
        r = pieces.King(-3, 2, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_King_outdown_B(self):
        r = pieces.King(10, 2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_King_outdown_W(self):
        r = pieces.King(10, 2, "White")
        assert r.valid_moves() == ("piece outside of the board")


###########################################

# knight

class Test_unit_knight:

    def test_knight_upleft_corner_B(self):
            n = pieces.Knight(0, 0, "Black")
            a = n.valid_moves()
            b = [(1, 2), (2, 1)]
            diff = set(a) ^ set(b)
            assert not diff

    def test_knight_upleft_corner_W(self):
            n = pieces.Knight(0, 0, "White")
            a = n.valid_moves()
            b = [(1, 2), (2, 1)]
            diff = set(a) ^ set(b)
            assert not diff
    
    def test_knight_upright_corner_B(self):
            n = pieces.Knight(0, 7, "Black")
            a = n.valid_moves()
            b = [(1, 5), (2, 6)]
            diff = set(a) ^ set(b)
            assert not diff
    
    def test_knight_upright_corner_W(self):
            n = pieces.Knight(0, 7, "White")
            a = n.valid_moves()
            b = [(1, 5), (2, 6)]
            diff = set(a) ^ set(b)
            assert not diff
    
    def test_knight_downleft_corner_B(self):
            n = pieces.Knight(7, 0, "Black")
            a = n.valid_moves()
            b = [(5, 1), (6, 2)]
            diff = set(a) ^ set(b)
            assert not diff
    
    def test_knight_downleft_corner_W(self):
            n = pieces.Knight(7, 0, "White")
            a = n.valid_moves()
            b = [(5, 1), (6, 2)]
            diff = set(a) ^ set(b)
            assert not diff

    def test_knight_downright_corner_B(self):
            n = pieces.Knight(7, 7, "Black")
            a = n.valid_moves()
            b = [(5, 6), (6, 5)]
            diff = set(a) ^ set(b)
            assert not diff
    
    def test_knight_downright_corner_W(self):
            n = pieces.Knight(7, 7, "White")
            a = n.valid_moves()
            b = [(5, 6), (6, 5)]
            diff = set(a) ^ set(b)
            assert not diff
    
    def test_knight_midLeft_B(self):
            n = pieces.Knight(4, 0, "Black")
            a = n.valid_moves()
            b = [(2, 1), (3, 2), (5, 2), (6, 1)]
            diff = set(a) ^ set(b)
            assert not diff
    
    def test_knight_midLeft_W(self):
            n = pieces.Knight(4, 0, "White")
            a = n.valid_moves()
            b = [(2, 1), (3, 2), (5, 2), (6, 1)]
            diff = set(a) ^ set(b)
            assert not diff

    def test_knight_midRight_B(self):
            n = pieces.Knight(4, 7, "Black")
            a = n.valid_moves()
            b = [(2, 6), (3, 5), (5, 5), (6, 6)]
            diff = set(a) ^ set(b)
            assert not diff
    
    def test_knight_midRight_W(self):
            n = pieces.Knight(4, 7, "White")
            a = n.valid_moves()
            b = [(2, 6), (3, 5), (5, 5), (6, 6)]
            diff = set(a) ^ set(b)
            assert not diff
    
    def test_knight_middle_B(self):
            n = pieces.Knight(4, 4, "Black")
            a = n.valid_moves()
            b = [(2, 5), (2, 3), (3, 6), (5, 6), (6, 3), (6, 5), (5, 2), (3, 2)]
            diff = set(a) ^ set(b)
            assert not diff

    def test_knight_middle_W(self):
            n = pieces.Knight(4, 4, "White")
            a = n.valid_moves()
            b = [(2, 5), (2, 3), (3, 6), (5, 6), (6, 3), (6, 5), (5, 2), (3, 2)]
            diff = set(a) ^ set(b)
            assert not diff

    def test_Knight_outleft_B(self):
        r = pieces.Knight(5, -2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Knight_outleft_W(self):
        r = pieces.Knight(5, -2, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Knight_outright_B(self):
        r = pieces.Knight(7, 9, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Knight_outright_W(self):
        r = pieces.Knight(7, 9, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Knight_outup_B(self):
        r = pieces.Knight(-3, 2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Knight_outup_W(self):
        r = pieces.Knight(-3, 2, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Knight_outdown_B(self):
        r = pieces.Knight(10, 2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Knight_outdown_W(self):
        r = pieces.Knight(10, 2, "White")
        assert r.valid_moves() == ("piece outside of the board")



###########################################

# Bishop

class Test_unit_bishop:

    def test_upleft_corner_B(self):
        w = pieces.Bishop(0, 0, "Black")
        a = w.valid_moves()
        b = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_upleft_corner_W(self):
        b = pieces.Bishop(0, 0, "White")
        a = b.valid_moves()
        b = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_upright_corner_B(self):
        b = pieces.Bishop(0, 7, "Black")
        a = b.valid_moves()
        b = [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_upright_corner_W(self):
        b = pieces.Bishop(0, 7, "White")
        a = b.valid_moves()
        b = [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (7, 0)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_downleft_corner_B(self):
        b = pieces.Bishop(7, 0, "Black")
        a = b.valid_moves()
        b = [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1), (0, 7)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_downleft_corner_W(self):
        b = pieces.Bishop(7, 0, "White")
        a = b.valid_moves()
        b = [(6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6), (0, 7)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_downright_corner_B(self):
        b = pieces.Bishop(7, 7, "Black")
        a = b.valid_moves()
        b = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_downright_corner_W(self):
        b = pieces.Bishop(7, 7, "White")
        a = b.valid_moves()
        b = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_midleft_B(self):
        b = pieces.Bishop(4, 0, "Black")
        a = b.valid_moves()
        b = [(5, 1), (6, 2), (7, 3), (3, 1), (2, 2), (1, 3), (0, 4)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_midleft_W(self):
        b = pieces.Bishop(4, 0, "White")
        a = b.valid_moves()
        b = [(5, 1), (6, 2), (7, 3), (3, 1), (2, 2), (1, 3), (0, 4)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_midright_B(self):
        b = pieces.Bishop(4, 7, "Black")
        a = b.valid_moves()
        b = [(5, 6), (6, 5), (7, 4), (3, 6), (2, 5), (1, 4), (0, 3)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_midright_W(self):
        b = pieces.Bishop(4, 7, "White")
        a = b.valid_moves()
        b = [(5, 6), (6, 5), (7, 4), (3, 6), (2, 5), (1, 4), (0, 3)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_middle_B(self):
        b = pieces.Bishop(4, 3, "Black")
        a = b.valid_moves()
        b = [(3, 4), (2, 5), (1, 6), (0, 7), (5, 4), (6, 5), (7, 6), (5, 2), (6, 1), (7, 0), (3, 2), (2, 1), (1, 0)]
        diff = set(a) ^ set(b)
        assert not diff
    
    def test_middle_W(self):
        b = pieces.Bishop(4, 3, "White")
        a = b.valid_moves()
        b = [(3, 4), (2, 5), (1, 6), (0, 7), (5, 4), (6, 5), (7, 6), (5, 2), (6, 1), (7, 0), (3, 2), (2, 1), (1, 0)]
        diff = set(a) ^ set(b)
        assert not diff

    def test_Bishop_outleft_B(self):
        r = pieces.Bishop(5, -2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Bishop_outleft_W(self):
        r = pieces.Bishop(5, -2, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Bishop_outright_B(self):
        r = pieces.Bishop(7, 9, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Bishop_outright_W(self):
        r = pieces.Bishop(7, 9, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Bishop_outup_B(self):
        r = pieces.Bishop(-3, 2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Bishop_outup_W(self):
        r = pieces.Bishop(-3, 2, "White")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Bishop_outdown_B(self):
        r = pieces.Bishop(10, 2, "Black")
        assert r.valid_moves() == ("piece outside of the board")

    def test_Bishop_outdown_W(self):
        r = pieces.Bishop(10, 2, "White")
        assert r.valid_moves() == ("piece outside of the board")

    
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
