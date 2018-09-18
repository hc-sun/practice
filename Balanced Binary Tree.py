# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.heightHelper(root) != -1
        
    def heightHelper(self, node):
        if not node:
            return 0
        left = self.heightHelper(node.left)
        right = self.heightHelper(node.right)
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        return max(left, right)+1

# Input: [1,2,3,4,5,null,6,7]
# Output: True
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1




    
# def heightHelper(self, root, height):
#     if root.left and root.right:
#         return max(self.heightHelper(root.left, height+1), self.heightHelper(root.right, height+1))
#     elif root.left:
#         return self.heightHelper(root.left, height+1)
#     elif root.right:
#         return self.heightHelper(root.right, height+1)
#     else:
#         return height+1