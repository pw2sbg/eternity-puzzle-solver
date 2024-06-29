class Piece:



    def __init__(self, values: list):
        
        self.values = values



    def rotate(self, angle: int) -> None:
        
        # When a piece is misplaced (e.g: 0 inside for a corner), we perform circular permutations until it is placed well
        
        # N.B: Does not return another piece but update the values of the piece itself

        n, rotated_piece = len(self.values), []
        
        for a in range(angle, n+angle):
            rotated_piece.append(self.values[a%n])
        
        self.values = rotated_piece