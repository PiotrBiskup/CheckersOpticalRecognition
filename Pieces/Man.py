from Pieces.Piece import Piece

class Man(Piece):

    alliance = None
    position = None

    def __init__(self, alliance, position):
        self.alliance = alliance
        self.position = position

    def toString(self):
        return "BM" if self.alliance == "Black" else "WM"