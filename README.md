# EternityPuzzle

  The Eternity puzzle is a tiling puzzle created by Christopher Monckton and launched by the Ertl Company in June 1999. It was marketed as being practically unsolvable, with a £1 million prize on offer for whoever could solve it within four years.
  The essence of the problem is to arrange puzzle pieces in a way that they align correctly with each other. The challenge of the problem lies in the fact that the number of possible arrangements can be exponential in relation to the puzzle size.
  The Eternity puzzle problem appears to be an NP (Non-deterministic Polynomial time) problem. NP is a class of decision problems for which, if the answer is given, it can be verified in polynomial time.


  The objective was to achieve the highest score heuristicly (i.e swap and/or rotate pieces of the puzzle).
Here is my approach to do so:
- All pieces are not the same. In fact, some have distinctive characteristics (i.e edges and more particurlarly corners) enabling to identify them (i.e function classify).
- 0s must be outside the puzzle. Therefore we can check if a corner or an edge piece is correctly placed or not (i.e function is_piece_position_correct)
- As all the pieces are not the same, we can be smart when swapping them. For example, it would make no sense to swap a corner with an edge or a middle piece. Therefore, we swap only pieces with the same type (i.e function swap_piece).
  About the simulation of the puzzle:
- At each iteration, we update the puzzle if the score is greater or equal than the previous reached. The equality matters because it avoids getting stuck in a local minima early.  


Additional content:
[1] - https://en.wikipedia.org/wiki/Eternity_puzzle
[2] - https://en.wikipedia.org/wiki/NP_(complexity)
