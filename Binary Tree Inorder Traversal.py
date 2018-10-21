# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        return self.helper(root, result)
    
    def helper(self, node, result):
        if node:
            if node.left:
                self.helper(node.left, result)
            result.append(node.val)
            if node.right:
                self.helper(node.right, result)
        return result
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]