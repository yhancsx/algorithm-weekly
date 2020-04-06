'''
leetcode 22
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.sol = []
        def dfs1(depth, complete, path):
            if complete == n:
                self.sol.append(path)
                return

            if depth > 0:
                dfs1(depth - 1, complete + 1, path + ")")

            if depth + complete < n:
                dfs1(depth + 1, complete, path + "(")

        def dfs2(left, right, path):
            if not left and not right:
                self.sol.append(path)

            if left > 0:
                dfs2(left - 1, right, path + '(')
            if right > left:
                dfs2(left, right - 1, path + ')')

        dfs2(n, n, "")
        return self.sol