# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        curr = head
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head

# Remove all elements from a linked list of integers that have value val.
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5