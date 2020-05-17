'''
다시보기
'''

class Node:
    left, right = None, None
    left_size = 0
    val = None

    def __init__(self, val):
        self.val = val

    def insert(self, x):
        if x <= self.val:
            if not self.left:
                self.left = Node(x)
            else:
                self.left.insert(x)
            self.left_size +=1
        else:
            if not self.right:
                self.right = Node(x)
            else:
                self.right.insert(x)

    def getRank(self, x):
        if x == self.val:
            return self.left_size
        elif x < self.val:
            if not self.left:
                return 0
            else:
                return self.left.getRank(x)
        else:
            right_rank = 0 if not self.right else self.right.getRank(x)
            return right_rank + 1 + self.left_size


class Sol:
    root = None

    def trace(self, x):
        if not self.root:
            self.root = Node(x)
        else:
            self.root.insert(x)


    def getRankOfNumber(self, number):
        return self.root.getRank(number)




s = Sol()
s.trace(5)
s.trace(1)
s.trace(4)
s.trace(4)
s.trace(5)
s.trace(9)
s.trace(7)
s.trace(13)
s.trace(3)
print(s.getRankOfNumber(1))
print(s.getRankOfNumber(3))
print(s.getRankOfNumber(4))


s = Sol()
s.trace(20)
s.trace(15)
s.trace(10)
s.trace(5)
s.trace(13)
s.trace(25)
s.trace(23)
s.trace(24)
print(s.getRankOfNumber(24))



