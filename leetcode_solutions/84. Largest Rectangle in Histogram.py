class Solution:
    def largestRectangleArea1(self, heights: List[int]) -> int:
        stack = []
        m = 0

        for i, h in enumerate(heights):
            if not len(stack) or h >= heights[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) and heights[stack[-1]] > h:
                    j = stack.pop()
                    w = i - 1 - (stack[-1] if len(stack) else -1)
                    m = max(m, w * heights[j])

                stack.append(i)

        i = len(heights)
        h = 0
        while len(stack) and heights[stack[-1]] > h:
            j = stack.pop()
            w = i - 1 - (stack[-1] if len(stack) else -1)
            m = max(m, w * heights[j])
        return m

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(0)
        m = 0
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                j = stack.pop()
                w = i - stack[-1] - 1
                m = max(m, w * heights[j])

            stack.append(i)

        return m