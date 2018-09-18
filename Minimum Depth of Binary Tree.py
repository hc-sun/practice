# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and root.right:
            return self.depthHelper(root, 0)
        elif root.left:
            return self.depthHelper(root.left, 1) # [1,2]
        elif root.right:
            return self.depthHelper(root.right, 1)
        else:
            return 1
    def depthHelper(self, root, depth):
        if root.left and root.right:
            return min(self.depthHelper(root.left, depth+1), self.depthHelper(root.right, depth+1))
        elif root.left:
            return self.depthHelper(root.left, depth+1) # node.left.left.left... and node.right.right...
        elif root.right:
            return self.depthHelper(root.right, depth+1)
        return depth + 1
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node
# Input: [3,9,20,null,null,15,7]
# Output: 2