'''
다시보기
'''
# box: [w, h, d]
def stackOfBoxes(boxes):
    sorted_boxes = sorted(boxes, key=lambda x: x[1], reverse=True)
    dp = [0] * len(sorted_boxes)

    def dfs(index, last):
        if index >= len(sorted_boxes):
            return 0

        cand1 = 0
        if sorted_boxes[index][0] <= last[0] and sorted_boxes[index][2] <= last[2]:
            if not dp[index]:
                dp[index] = dfs(index + 1, sorted_boxes[index]) + sorted_boxes[index][1]
            cand1 = dp[index]
        cand2 = dfs(index + 1, last)

        return max(cand1, cand2)

    return dfs(0, [float('inf'), 0, float('inf')])


def stackOfBoxes2(boxes):
    sorted_boxes = sorted(boxes, key=lambda x: x[1], reverse=True)
    dp = [0] * len(sorted_boxes)

    def dfs(index, last):
        if dp[index]:
            return dp[index]

        m = 0
        for i in range(index+1, len(sorted_boxes)):
            box = sorted_boxes[i]
            if box[0] <= last[0] and box[2] <= last[2]:
                m = max(m, dfs(i, box))

        dp[index] = m+sorted_boxes[index][1]

        return dp[index]


    m = 0
    for index, box in enumerate(sorted_boxes):
        m = max(m, dfs(index, box))

    return m


boxes = [
    [1, 1, 1],
    [4, 4, 1],
    [3, 5, 2],
    [2, 6, 4],
    [5, 7, 6],
    [9, 8, 9],
    [3, 2, 2],
    [5, 5, 3],
    [2, 1, 4],
    [9, 11, 9],
]
print(stackOfBoxes(boxes))
print(stackOfBoxes2(boxes))
