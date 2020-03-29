'''
leetcode 232
'''
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        while len(self.s1):
            x = self.s1.pop()
            self.s2.append(x)
        sol = self.s2.pop()

        while len(self.s2):
            x = self.s2.pop()
            self.s1.append(x)
        return sol

    def peek(self) -> int:
        """
        Get the front element.

        """
        while len(self.s1):
            x = self.s1.pop()
            self.s2.append(x)
        sol = x
        while len(self.s2):
            x = self.s2.pop()
            self.s1.append(x)
        return sol

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()