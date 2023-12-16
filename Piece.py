class Piece:


    def __init__(self, piece: list):
        self.piece = piece


    def rotate(self, angle: int) -> None:
        
        # When a piece is misplaced (e.g: 0 inside for a corner), we perform circular permutations until it is placed well
        # HERE: Give a more concrete example
        # N.B: overwrites piece

        n, rotated_piece = len(self.piece), []
        
        for a in range(angle, n+angle):
            rotated_piece.append(self.piece[a%n])
        
        self.piece = rotated_piece