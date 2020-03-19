'''
Same with
cracking the coding interview > 1.8
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        xs = set()
        ys = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    xs.add(i)
                    ys.add(j)

        for x in xs:
            for j in range(len(matrix[x])):
                matrix[x][j] = 0
        for y in ys:
            for i in range(len(matrix)):
                matrix[i][y] = 0

    def setZeroes(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 0: return matrix

        zeroFirstRow = 0
        zeroFirstCol = 0

        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                zeroFirstRow = 1
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zeroFirstCol = 1
                break

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0


        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0

        if zeroFirstRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if zeroFirstCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0




