# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = []
        p = q = head
        while p:
            temp.append(p.val)
            p = p.next
        while q:
            if q.val != temp.pop():
                return False
            q = q.next
        return True
# Given a singly linked list, determine if it is a palindrome.
# Input: 1->2->2->1
# Output: true