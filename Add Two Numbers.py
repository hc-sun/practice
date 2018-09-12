# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        i = 0
        temp = 0
        while l1 or l2:
            if l1:
                temp += l1.val * 10 ** i
                l1 = l1.next
            if l2:
                temp += l2.val * 10 ** i
                l2 = l2.next          
            i += 1
        return list(map(int, str(temp)[::-1]))
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.