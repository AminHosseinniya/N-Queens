class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        placement_sets = []     # To hold all valid placements
        board = [[0] * n for _ in range(n)]     # To represent the chess board
        board_border = range(len(board))

        ## The Placement Algorithm
        square = [0, 0]     # Put first square
        board[square[0]][square[1]] = 1     # Show the queen on the board

        reachable_squares = list()
        [reachable_squares.append([x, square[1]]) for x in board_border]                # Reachable squares toward down

        for step in range(len(board))[1:]:
            if square[0]+step in board_border and square[1]-step in board_border:       # Reachable squares toward bottom-lef
                reachable_squares.append([square[0]+step,square[1]-step])
            if square[0]+step in board_border and square[1]+step in board_border:       # Reachable squares toward bottom-right
                reachable_squares.append([square[0]+step,square[1]+step])
        print("\nreachable cells: ", reachable_squares)






        print("\nboard:")
        for row in board:
            print(row)

solution = Solution()
solution.solveNQueens(4)