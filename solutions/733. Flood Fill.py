class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visit = set()
        n, m = len(image), len(image[0])
        color = image[sr][sc]
        mx = [1, 0, -1, 0]
        my = [0, 1, 0, -1]

        queue = []
        queue.append((sr, sc))

        while queue:
            r, c = queue.pop(0)
            visit.add((r, c))
            image[r][c] = newColor

            for x, y in zip(mx, my):
                new_r = r + x
                new_c = c + y
                if 0 <= new_r < n and 0 <= new_c < m and (new_r, new_c) not in visit and \
                        image[new_r][new_c] == color:
                    queue.append((new_r, new_c))

        return image
