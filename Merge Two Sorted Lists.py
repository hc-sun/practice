# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        li = head
        while l1 and l2:
            if l1.val <= l2.val:
                li.next = l1
                l1 = l1.next
            else:
                li.next = l2
                l2 = l2.next
            li = li.next
        if l1 is None:
            li.next = l2
        else:
            li.next = l1
        return head.next