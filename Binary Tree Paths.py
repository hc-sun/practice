# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        return [str(root.val) + "->" + val for val in self.binaryTreePaths(root.left)] + [str(root.val) + "->" + val for val in self.binaryTreePaths(root.right)]
# Given a binary tree, return all root-to-leaf paths.
#    1
#  /   \
# 2     3
#  \
#   5
# Input
# [1,2,3,null,5]
# Output
# ["1->2->5","1->3"]