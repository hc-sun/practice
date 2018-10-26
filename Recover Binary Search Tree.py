# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        temp = []
        self.inorder(root, temp)
        temp.sort()
        self.swap(root, temp)
    def inorder(self, node, temp):
        if not node: return
        self.inorder(node.left, temp)
        temp.append(node.val)
        self.inorder(node.right, temp)
    def swap(self, node, temp):
        if not node: return
        self.swap(node.left, temp)
        node.val = temp.pop(0)
        self.swap(node.right, temp)

# Two elements of a binary search tree (BST) are swapped by mistake.
# Recover the tree without changing its structure.

# Input: [1,3,null,null,2]

#    1
#   /
#  3
#   \
#    2

# Output: [3,1,null,null,2]

#    3
#   /
#  1
#   \
#    2

# Input: [3,1,4,null,null,2]

#   3
#  / \
# 1   4
#    /
#   2

# Output: [2,1,4,null,null,3]

#   2
#  / \
# 1   4
#    /
#   3