class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """ 
        placements_set = list()     # To hold all valid placements
        board = [[0] * n for _ in range(n)]     # To represent the chess board
        squares = [[row, col] for row in range(n) for col in range(n)]
        queens = [[None, None] for _ in range(n)]
        valid_squares = [[None, None] for _ in range(n)]
        status = [True]*n
        # valid_squares = [n for _ in range(n)]
        # rows_guide = [{"status": False, "num_of_valids": 0} for _ in range(n)]      # "status" of each row should be True if there are still                                              
                                                                                    # valid squares in that row that are not examined yet, 
                                                                                    # and "num_of_valids" show number of this valid sqaures.
        # print("queens: ", queens)

        
        self.result = self.put_queen(0, queens, board, squares, valid_squares, placements_set, status)
        print(self.result)

        # reachable_squares = self.reach_finder(board, queens)
        # self.show_the_board(board, reachable_squares)
        # print(self.placements_set)
    


    def put_queen(self, row, queens, board, squares, valid_squares, placements_set, status):
        if row == -1:
            print(row)
            print(placements_set)
            return placements_set

        print("\n========================")
        reachable_squares = self.reach_finder(board, queens)    # get valid square through the whole board
        if status[row] == True:
            valid_squares[row] = [square for square in squares if square[0]==row and square not in reachable_squares]   # get valid squares of considering row
            status[row] = False
        print(f"valid_squares: {valid_squares}")

        if len(valid_squares[row]) != 0:
            print("SAFA")
            print(f"row: {row}")
            queens[row] = valid_squares[row][0]     # out queen of considering row in first available position
            valid_squares[row].pop(0)    # drop filled square from valid squares of considering row
            print(f"valid_squares after pop: {valid_squares}")
            print(f"queens: {queens}")
            print(f"placements_set: {placements_set}")
            if row == len(board)-1:
                placements_set.append(queens)
                print(f"placements_set after append: {placements_set}")
                self.put_queen(row, queens[:], board, squares, valid_squares[:], placements_set, status[:])  # go for next row!
            else:
                status[row+1] = True
                self.put_queen(row+1, queens[:], board, squares, valid_squares[:], placements_set, status[:])  # go for next row!
        else:
            print("NOT SAFA")
            print(f"row: {row}")
            queens[(row-1):] = [[None, None]]*len(queens[(row-1):])
            status[row-1] = False    # not allowd to revalculate valid squares
            print(f"queens before going back: {queens}")
            self.put_queen(row-1, queens[:], board, squares, valid_squares[:], placements_set, status[:])  # go for previous row!
        
        
        # return placements_set



    def reach_finder(self, board, queens):        # This function is what I call a Filter. like a net with a special shape
        reachable_squares = list()                                                 # that fells over something.
        board_border = range(len(board))
        # Horizontal reachable squares are not examined, 'cause no queen is gonne be out in same row with queen in hand.
        
        for queen in queens:
            # Ensure queen is already initiated:
            if queen == [None, None]:
                continue
            
            # Vertical reachable squares:
            [reachable_squares.append([x, queen[1]]) for x in board_border]        # Reachable squares toward down

            # Diagonal reachable squares:
            for step in range(len(board))[1:]:
                if queen[0]+step in board_border and queen[1]-step in board_border:       # Reachable squares toward bottom-lef
                    reachable_squares.append([queen[0]+step, queen[1]-step])
                if queen[0]+step in board_border and queen[1]+step in board_border:       # Reachable squares toward bottom-right
                    reachable_squares.append([queen[0]+step, queen[1]+step])

        return reachable_squares



    def show_the_board(self, board, reachable_squares):
        for square in reachable_squares:
            board[square[0]][square[1]] = "*"
        
        print("\nreachable cells: ", reachable_squares)
        print("\nboard:")

        for row in board:
            print("  ".join(str(element) for element in row))


solution = Solution()
solution.solveNQueens(6)