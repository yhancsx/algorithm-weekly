'''
다시보기
leetcode 160
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = l2 = 0
        ha, hb = headA, headB
        while ha:
            l1 += 1
            ha = ha.next

        while hb:
            l2 += 1
            hb = hb.next

        ha, hb = headA, headB
        if l1 > l2:
            for i in range(l1 - l2):
                ha = ha.next
        elif l2 > l1:
            for i in range(l2 - l1):
                hb = hb.next

        while ha is not hb:
            ha = ha.next
            hb = hb.next
        return ha





