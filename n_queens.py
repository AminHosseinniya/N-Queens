class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """ 
        placements_set = list()     # To hold all valid placements
        board = [[0] * n for _ in range(n)]     # To represent the chess board
        
        reachable_squares = list()
        valid_squares = [[]]*n
        queens = [[i, None] for i in range(n)]

        # queens[0][1] = 0
        for i in range(n):
            queens[0][1] = i   # Put first queen
            # board[queens[0][0]][queens[0][1]] = 1     # Show the queen on the board
            reachable_squares = self.reach_finder(board, queens[0], reachable_squares)
            valid_squares[i] = [[i, col] for col in range(n) if [i, col] not in reachable_squares]
    
        print(valid_squares)            





        # To show the board:
        for square in reachable_squares:
            board[square[0]][square[1]] = "*"
        
        print("\nreachable cells: ", reachable_squares)
        print("\nboard:")

        for row in board:
            print("  ".join(str(element) for element in row))


    def reach_finder(self, board, queen_coords, reach_list):        # This function is what I call a Filter. like a net with a special shape
                                                                    # that fells over something.
        board_border = range(len(board))
        # Horizontal reachable squares are not examined, 'cause no queen is gonne be out in same row with queen in hand.
        # Vertical reachable squares:
        [reach_list.append([x, queen_coords[1]]) for x in board_border]        # Reachable squares toward down

        # Diagonal reachable squares:
        for step in range(len(board))[1:]:
            if queen_coords[0]+step in board_border and queen_coords[1]-step in board_border:       # Reachable squares toward bottom-lef
                reach_list.append([queen_coords[0]+step, queen_coords[1]-step])
            if queen_coords[0]+step in board_border and queen_coords[1]+step in board_border:       # Reachable squares toward bottom-right
                reach_list.append([queen_coords[0]+step, queen_coords[1]+step])

        return reach_list



solution = Solution()
solution.solveNQueens(4)