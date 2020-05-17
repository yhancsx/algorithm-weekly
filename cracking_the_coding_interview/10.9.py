'''
leetcode 74, 240
240번 다시보기
'''
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if not len(matrix) or not len(matrix[0]):
        return False

    l = 0
    r = len(matrix) - 1

    while l <= r:
        m = (l + r) // 2
        if matrix[m][0] == target: return True
        if matrix[m][0] < target:
            l = m + 1
        elif matrix[m][0] > target:
            r = m - 1

    row = r
    l = 0
    r = len(matrix[0]) - 1

    while l <= r:
        m = (l + r) // 2
        if matrix[row][m] == target: return True
        if matrix[row][m] < target:
            l = m + 1
        elif matrix[row][m] > target:
            r = m - 1
    return False

def searchMatrix2_1(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix or not matrix[0]: return False

    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target: return True
        if matrix[row][col] < target:
            row += 1
        else:
            col -= 1
    return False

def searchMatrix2_2(self, matrix, target):
    if not matrix or not matrix[0]: return False
    x0, x1, y0, y1 = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

    def findElement(x0, x1, y0, y1):
        if x0 > x1 or y0 > y1: return False

        x = (x0 + x1) // 2
        y = (y0 + y1) // 2

        if matrix[x][y] == target:
            return True
        if matrix[x][y] < target:
            return findElement(x0, x1, y + 1, y1) or findElement(x + 1, x1, y0, y)
        if matrix[x][y] > target:
            return findElement(x0, x1, y0, y - 1) or findElement(x0, x - 1, y, y1)

    return findElement(x0, x1, y0, y1)







