# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 1
        return self.depthHelper(root, depth)
    def depthHelper(self, root, depth):
        if root.left and root.right:
            return max(self.depthHelper(root.left, depth + 1), self.depthHelper(root.right, depth + 1))
        elif root.left:
            return (self.depthHelper(root.left, depth + 1))
        elif root.right:
            return (self.depthHelper(root.right, depth + 1))
        else: #both left and right are None
            return depth
# Input: [3,9,20,null,null,15,7]
# Output: 3