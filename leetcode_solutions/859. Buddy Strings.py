class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        if A == B:
            return len(A) - len(set(A)) >= 1

        count = 0
        a1, b1 = "", ""

        for a, b in zip(A, B):
            if a != b:
                if count == 0:
                    a1 = a
                    b1 = b
                    count += 1
                elif count == 1:
                    if a1 != b or a != b1: return False
                    count += 1
                else:
                    return False

        if count == 2:
            return True

        return False

