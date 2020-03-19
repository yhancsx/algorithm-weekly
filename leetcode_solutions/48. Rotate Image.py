'''
Same with
cracking the coding interview > 1.7
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-i-1):
                top = (i, j)
                right = (j, n-1-i)
                bottom = (n-1-i, n-1-j)
                left = (n-1-j, i)

                tmp = matrix[top[0]][top[1]]
                matrix[top[0]][top[1]] = matrix[left[0]][left[1]]
                matrix[left[0]][left[1]] = matrix[bottom[0]][bottom[1]]
                matrix[bottom[0]][bottom[1]] = matrix[right[0]][right[1]]
                matrix[right[0]][right[1]] = tmp
