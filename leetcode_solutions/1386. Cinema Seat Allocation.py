class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = set()
        iset = set()
        for i, j in reservedSeats:
            iset.add(i)
            reserved.add((i, j))

        ret = n * 2

        for i in list(iset):
            c = 0
            if (i, 2) not in reserved and (i, 3) not in reserved and (i, 4) not in reserved and (
            i, 5) not in reserved: c += 1
            if (i, 6) not in reserved and (i, 7) not in reserved and (i, 8) not in reserved and (
            i, 9) not in reserved: c += 1
            if (i, 4) not in reserved and (i, 5) not in reserved and (i, 6) not in reserved and (
            i, 7) not in reserved and c == 0: c += 1
            ret += (c - 2)

        return ret