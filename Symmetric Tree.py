# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.searchHelper(root.left, root.right)
    def searchHelper(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        return self.searchHelper(left.left, right.right) and self.searchHelper(left.right, right.left)

# Input: [1,2,2,3,4,4,3]
# Output: True