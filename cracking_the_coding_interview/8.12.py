class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol = []

        def makeMap(queens):
            m = [['.'] * n for i in range(n)]
            for r, c in enumerate(queens):
                m[r][c] = 'Q'
            return ["".join(m[row]) for row in range(n)]

        def isValid(queens, row, col):
            for r, c in enumerate(queens):
                if row == r or col == c: return False
                if abs(row - r) == abs(col - c): return False

            return True

        def dfs(queens, row):
            if row == n:
                sol.append(makeMap(queens))

            for col in range(n):
                if isValid(queens, row, col):
                    queens.append(col)
                    dfs(queens, row + 1)
                    queens.pop()

        dfs([], 0)
        return sol
