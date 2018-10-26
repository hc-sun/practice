# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):#O(n) Space
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

    # Morris Traversal O(1) Space
    # 1. Initialize current as root 
    # 2. While current is not NULL
    #     If current does not have left child
    #         a) Print current’s data
    #         b) Go to the right, i.e., current = current->right
    #     Else
    #         a) Make current as right child of the rightmost 
    #             node in current's left subtree
    #         b) Go to this left child, i.e., current = current->left

    # def recoverTree(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: void Do not return anything, modify root in-place instead.
    #     """
    #     curr, first, second, predec = root, None, None, None
    #     while curr:
    #         if not curr.left:
    #             if predec and curr.val < predec.val:
    #                 if not first:
    #                     first = predec
    #                 second = curr
    #             predec = curr
    #             curr = curr.right
    #         else:
    #             pre = curr.left
    #             while pre.right and pre.right != curr:
    #                 pre = pre.right
    #             if not pre.right:
    #                 pre.right = curr
    #                 curr = curr.left
    #             else:
    #                 if predec and curr.val < predec.val:
    #                     if not first:
    #                         first = predec
    #                     second = curr
    #                 predec = curr
    #                 pre.right = None
    #                 curr = curr.right
    #     first.val, second.val = second.val, first.val
                

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