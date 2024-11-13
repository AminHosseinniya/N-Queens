class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        placement_sets = []     # To hold all valid placements
        board = [[0] * n for _ in range(n)]     # To represent the chess board
        
        for row in board:
            print(row)

solution = Solution()
solution.solveNQueens(4)