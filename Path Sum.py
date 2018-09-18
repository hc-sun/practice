# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.dfs(root, sum)
    def dfs(self, root, sum):
        if root.left:
            if self.dfs(root.left, sum - root.val):
                return True
        if root.right:
            if self.dfs(root.right, sum - root.val):
                return True
        if not root.left and not root.right and sum - root.val == 0:
            return True
        return False

# DFS Inorder
# Input:[5,4,8,11,null,13,4,7,2,null,null,null,1] 22
# Output: True