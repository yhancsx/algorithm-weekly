# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindromeOld(self, head: ListNode) -> bool:
        l = []

        while head:
            l.append(head.val)
            head = head.next

        n = len(l)
        return l[:n // 2] == l[-1:n // 2:-1] if n % 2 == 1 else l[:n // 2] == l[-1:n // 2 - 1:-1]

    def isPalindrome(self, head):
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while slow:
            if slow.val != rev.val: return False
            slow = slow.next
            rev = rev.next

        return True




