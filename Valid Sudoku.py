class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        sub_boxes = [[[] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue
                if cell in rows[i] or cell in cols[j] or cell in sub_boxes[i//3][j//3]:
                    return False
                rows[i].append(cell)
                cols[j].append(cell)
                sub_boxes[i//3][j//3].append(cell)
        return True

#another solution: loop 9 times: use a helper func every time create a list of digits of row or col or sub_box, then compare if len(row)==len(set(row))

# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being 
#     modified to 8. Since there are two 8's in the top