class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h = [[0 for i in range(9)] for i in range(9)]
        v = [[0 for i in range(9)] for i in range(9)]
        b = [[0 for i in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num)-1
                    h[i][num] +=1
                    if h[i][num] > 1: return False
                    ########
                    v[j][num] += 1
                    if v[j][num] > 1: return False
                    ########
                    x = i//3 + 3*(j//3)
                    b[x][num] += 1
                    if b[x][num] > 1: return False
        return True
