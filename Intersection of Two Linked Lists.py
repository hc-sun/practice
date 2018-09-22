# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pointerA = headA
        pointerB = headB
        while pointerA != pointerB: 
            if not pointerA:
                pointerA = headB
            else:
                pointerA = pointerA.next
            if not pointerB:
                pointerB =headA
            else:
                pointerB = pointerB.next
        return pointerA
#Write a program to find the node at which the intersection of two singly linked lists begins.
