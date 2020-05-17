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




