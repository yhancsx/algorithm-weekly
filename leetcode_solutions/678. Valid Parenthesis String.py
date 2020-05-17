class Solution:
    def checkValidString(self, s: str) -> bool:
        depth = 0
        whild = 0

        for a in s:
            if a == '(':
                depth += 1
            elif a == ')':
                if depth == 0:
                    if whild == 0: return False
                    whild -= 1
                else:
                    depth -= 1

            else:
                whild += 1

        depth = 0
        whild = 0
        for a in s[::-1]:
            if a == ')':
                depth += 1
            elif a == '(':
                if depth == 0:
                    if whild == 0: return False
                    whild -= 1
                else:
                    depth -= 1

            else:
                whild += 1

        return True

    def checkValidString2(self, s):
        mi = 0
        ma = 0

        for a in s:
            if a == '(':
                mi += 1
                ma += 1
            elif a == ')':
                mi -= 1
                ma -= 1
            else:
                mi -= 1
                ma += 1

            if ma < 0: return False
            if mi < 0: mi += 1

        return mi == 0








