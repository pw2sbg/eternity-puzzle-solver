from collections import Counter
from random import randint, choice
from Piece import *



class Puzzle:



    def __init__(self, file_name: str = None):
        self.rows, self.columns, self.pieces = self.get_features(file_name)
        self.puzzle = []



    def get_features(self, file_name: str):
        
        with open(file_name, "r") as f:
            features = [line.split() for line in f]
        shape = features.pop(0)
        rows, columns = shape
        rows, columns = int(rows), int(columns)
        
        return rows, columns, features



    def classify(self) -> list:

        # We know that each piece is divided in 4 parts, each containing an integer
        # 0 must form the edges of the puzzle
        # Therefore, we can classify each piece
        # According to the number of 0 it has, it is a corner, an edge or a middle piece.
        # How do we count them ?
        # 2 solutions:
        # - 2 for-loop => complexity increases with the number of pieces
        # - built-in class/method

        corners, edges, middles = [], [], []
        
        for piece in self.pieces:
            # zero_counter = self.count_zeros(piece)
            zero_counter = Counter(piece)["0"]
            if zero_counter == 2:
                corners.append(piece)
            elif zero_counter == 1:
                edges.append(piece)
            else:
                middles.append(piece)
        
        return corners, edges, middles



    def count_zeros(self, piece: str) -> int:
        
        zero_counter = 0
        for i in piece:
            if i == "0":
                zero_counter += 1
        
        return zero_counter
    

    
    """
    def construct(self) -> list:

        # The problem is to construct the puzzle the most efficiently
        # My first idea was to construct subpuzzles (i.e list) designing pieces on a row and add them to the big puzzle
        # That implies 2 main issues:
        # - for each row, instantiate a list => increases memory complexity
        # - you get list of lists (of lists) at the end (e.g [[piece_1, piece_2, piece_3], [piece_4, piece_5, piece_6], [piece_7, piece_8, piece_9]], where piece_i are lists)
        # So, I come up with another idea: construct the puzzle from left-to-right and from top-to-right
        # With 2 counters, I am able to determine, pick and place the right type of piece

        corners, edges, middles = self.classify(self.pieces)

        i, j = 0, 0
        for k in range(len(self.pieces)):
            if k!=0 and k%self.columns == 0:
                i += 1
                j = 0
            
            # First condition constructs top and bottom rows of the puzzle
            # Second condition constructs outside columns of the puzzle
            # Third condition completes the puzzle
            if i==0 or i==self.rows-1:
                if j==0 or j==self.columns-1:
            # First if-condition selects top or bottom row
                # From those, second if-condition selects first or last column
                # Therefore, we get all 4 corners
                    corner = corners.pop(randint(0, len(corners)-1))
                    corner_piece = Piece(corner)
                    self.puzzle.append(corner_piece)
                else:
                # Otherwise, we get all edges from top and bottom rows 
                    edge = edges.pop(randint(0, len(edges)-1))
                    edge_piece = Piece(edge)
                    self.puzzle.append(edge_piece)
            elif j==0 or j==self.columns-1:
            # Rows different from top or bottom
            # elif-condition selects first or last column
            # Therefore, we get all outside columns
                edge = edges.pop(randint(0, len(edges)-1))
                edge_piece = Piece(edge)
                self.puzzle.append(edge_piece)
            else:
            # Last condition completes the puzzle
                middle = middles.pop(randint(0, len(middles)-1))
                middle_piece = Piece(middle)
                self.puzzle.append(middle_piece)
            
            j+=1

        return self.puzzle
    """


    def construct(self) -> None:

        # Original idea seems better because:
        # - at the end, you get a matrix
        # - pieces can be obtained using indeces (e.g: random_piece = puzzle[i][j])
            
        corners, edges, middles = self.classify()
        
        for i in range(self.rows):
            sub_puzzle = []
            for j in range(self.columns):
            
            # First condition constructs top and bottom rows of the puzzle
            # Second condition constructs outside columns of the puzzle
            # Third condition completes the puzzle
            
                if i==0 or i==self.rows-1:
                    if j==0 or j==self.columns-1:
                # First if-condition selects top or bottom row
                    # From those, second if-condition selects first or last column
                    # Therefore, we get all 4 corners
                        corner = corners.pop(randint(0, len(corners)-1))
                        corner_piece = Piece(corner)
                        sub_puzzle.append(corner_piece)
                    else:
                    # Otherwise, we get all edges from top and bottom rows 
                        edge = edges.pop(randint(0, len(edges)-1))
                        edge_piece = Piece(edge)
                        sub_puzzle.append(edge_piece)
                
                elif j==0 or j==self.columns-1:
                # Rows different from top or bottom
                # elif-condition selects first or last column
                # Therefore, we get all outside columns
                    edge = edges.pop(randint(0, len(edges)-1))
                    edge_piece = Piece(edge)
                    sub_puzzle.append(edge_piece)
                
                else:
                # Last condition completes the puzzle
                    middle = middles.pop(randint(0, len(middles)-1))
                    middle_piece = Piece(middle)
                    sub_puzzle.append(middle_piece)


            self.puzzle.append(sub_puzzle)
        
        return self
    

    
    def is_piece_position_correct(self, row: int, column: int) -> int:
        
        piece = self.puzzle[row][column]

        angle = 0
        
        if row == 0:
            if column == 0:
                while (piece.piece[1] != "0") or (piece.piece[2] != "0"):
                    angle += 1
                    piece.rotate(1)
            elif column == self.columns-1:  
                while (piece.piece[2] != "0") or (piece.piece[3] != "0"):
                    angle += 1
                    piece.rotate(1)
            
            else:
                while piece.piece[2] != "0":
                    angle += 1
                    piece.rotate(1)


        elif row == self.rows-1:
            if column == 0:
                while (piece.piece[0] != "0") or (piece.piece[1] != "0"):
                    angle += 1
                    piece.rotate(1)
            elif column == self.columns-1:
                while (piece.piece[0] != "0") or (piece.piece[3] != "0"):
                    angle += 1
                    piece.rotate(1)
            else:
                while piece.piece[0] != "0":
                    angle += 1
                    piece.rotate(1)

        else:
            if column == 0:
                while piece.piece[1] != "0":
                    angle += 1
                    piece.rotate(1)
            elif column == self.columns-1:
                while piece.piece[3] != "0":
                    angle += 1
                    piece.rotate(1)

        self.puzzle[row][column] = piece

        return angle



    def get_piece_index(self, piece: Piece):
        return self.pieces.index(piece)
    


    def swap_piece(self) -> None:

        # All print below enable to check if the method passes Test 7

        type = choice(["corner", "edge", "middle"])
        # print(type)

        if type == "corner":
            i1, j1 = choice([0, self.rows-1]), choice([0, self.columns-1])
            i2, j2 = choice([0, self.rows-1]), choice([0, self.columns-1])
            while i1 == i2 and j1 == j2:
                i2, j2 = choice([0, self.rows-1]), choice([0, self.columns-1])


        elif type == "edge":
            
            i1 = randint(0, self.rows-1)
            if i1 == 0 or i1 == self.rows-1:
                j1 = randint(1, self.columns-2)
            else:
                j1 = choice([0, self.columns-1])
                
            i2 = randint(0, self.rows-1)
            if i2 == 0 or i2 == self.rows-1:
                j2 = randint(1, self.columns-2)
            else:
                j2 = choice([0, self.columns-1])
            
            while i1 == i2 and j1 == j2:
                i2 = randint(0, self.rows-1)
                if i2 == 0 or i2 == self.rows-1:
                    j2 = randint(1, self.columns-2)
                else:
                    j2 = choice([0, self.columns-1])


        elif type == "middle":
            i1, j1 = randint(1, self.rows-2), randint(1, self.columns-2)
            i2, j2 = randint(1, self.rows-2), randint(1, self.columns-2)
            while i1 == i2 and j1 == j2:
                i2, j2 = randint(1, self.rows-2), randint(1, self.columns-2)


        # print(f"Before swapping: {self.puzzle[i1][j1].piece, self.puzzle[i2][j2].piece}")
        self.puzzle[i1][j1], self.puzzle[i2][j2] = self.puzzle[i2][j2], self.puzzle[i1][j1]
        # print(f"After swapping: {self.puzzle[i1][j1].piece, self.puzzle[i2][j2].piece}")
        self.is_piece_position_correct(i1, j1)
        self.is_piece_position_correct(i2, j2)
        # print(f"After checking position: {self.puzzle[i1][j1].piece, self.puzzle[i2][j2].piece}")

        return self



    def get_score(self) -> int:

        # To calculate the score of the puzzle (i.e the number of faces which match), we iterate over the rows first and over the columns then
        # Pieces are compared two by two
        # The maximum possible score is given by the formula: score = rows*(columns-1) + (rows-1)*columns = 2*n*(n-1), if puzzle is squared

        score = 0

        for i in range(self.rows):
            for j in range(self.columns-1):
                left_piece, right_piece = self.puzzle[i][j].piece, self.puzzle[i][j+1].piece
                if left_piece[3] == right_piece[1]:
                    score += 1
                    
        for i in range(self.rows-1):
            for j in range(self.columns):
                piece_above, piece_below = self.puzzle[i][j].piece, self.puzzle[i+1][j].piece
                if piece_above[0] == piece_below[2]:
                    score += 1

        return score


    def initialize(self) -> None:

        self.construct()

        for i in range(self.rows):
            for j in range(self.columns):
                self.is_piece_position_correct(i, j)

        return self    





# Test 1: class (and therefore: get_features)
# path = "pieces_set/"
# file_name = path + "pieces_10x10.txt"
# puzzle = Puzzle(file_name=file_name)
# print(puzzle)
# output: <__main__.Puzzle object at 0x00000212835EBC40>


# Test 2: classify
# corners, edges, middles = puzzle.classify()
# print(corners)
# output: [['0', '0', '1', '1'], ['0', '0', '1', '2'], ['0', '0', '2', '1'], ['0', '0', '2', '2']]
# print(edges)
# output: [['0', '1', '3', '1'], ['0', '1', '3', '2'], ['0', '1', '4', '2'], ['0', '2', '3', '1'], ['0', '2', '4', '1'], ['0', '2', '4', '2']]
# print(middles)
# output: [['3', '3', '3', '4'], ['3', '3', '4', '4']]


# Test 3: construct
# eternity = puzzle.construct()
# print(eternity)
# output: <__main__.Puzzle object at 0x0000016661DEBC40>
# eternity remains Puzzle object

# print(eternity.puzzle)
# output: [[<Piece.Piece object at 0x0000016661DEBC10>, <Piece.Piece object at 0x0000016661DEAEC0>, <Piece.Piece object at 0x0000016661DEAD70>], [<Piece.Piece object at 0x0000016661DEAD10>, <Piece.Piece object at 0x0000016661DEACB0>, <Piece.Piece object at 0x0000016661DEAC50>], [<Piece.Piece object at 0x0000016661DEABF0>, <Piece.Piece object at 0x0000016661DEAB90>, <Piece.Piece object at 0x0000016661DEAB30>], [<Piece.Piece object at 0x0000016661DEAAD0>, <Piece.Piece object at 0x0000016661DEAA70>, <Piece.Piece object at 0x0000016661DEAA10>]]
# eternity is a 4-times-3 shaped puzzle made of Piece

# Check each piece
# for i in range(eternity.rows):
#     for j in range(eternity.columns):
#         print(eternity.puzzle[i][j].piece)
# output:
# ['0', '0', '2', '2']
# ['0', '1', '3', '2']
# ['0', '0', '2', '1']
# ['0', '1', '4', '2']
# ['3', '3', '4', '4']
# ['0', '2', '4', '2']
# ['0', '2', '4', '1']
# ['3', '3', '3', '4']
# ['0', '2', '3', '1']
# ['0', '0', '1', '1']
# ['0', '1', '3', '1']
# ['0', '0', '1', '2']


# Test 4: get_score
# print(eternity.get_score())
# output: 2


# Test 5: Piece.rotate
# piece_0_0 = eternity.puzzle[0][0]
# print(piece_0_0.piece)
# output: ['0', '0', '2', '2']
# piece_0_0_bis = piece_0_0.rotate(1)
# print(piece_0_0_bis.piece)
# output: ['0', '2', '2', '0']
# print(piece_0_0.piece)
# output: ['0', '2', '2', '0']
# N.B: overwrites piece

# Test 6: is_piece_position_correct
# print(eternity.puzzle[0][0].piece)
# output: ['0', '0', '1', '2']
# eternity.is_piece_position_correct(0, 0)
# print(eternity.puzzle[0][0].piece)
# output: ['2', '0', '0', '1']

# Test 7: swap_piece
# eternity.swap_piece()
# output:
# edge
# Before swapping: (['0', '1', '3', '1'], ['0', '2', '3', '1'])
# After swapping: (['0', '2', '3', '1'], ['0', '1', '3', '1'])
# After checking position: (['2', '3', '1', '0'], ['3', '1', '0', '1'])