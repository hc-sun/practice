# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        temp = []
        node = root
        while node or temp:
            while node:
                temp.append(node)
                node = node.left
            node = temp.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right
            
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3