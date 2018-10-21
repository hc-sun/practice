# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):# Recursion, Time O(n), worst space O(n) depends on num of nodes
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





    # def inorderTraversal(self, root): #Iterative
    #     """
    #     :type root: TreeNode
    #     :rtype: List[int]
    #     """
    #     result = []
    #     stack = []
    #     #first find the end of left while putting left roots in stack, append left to result, append root to result, append right to stack, if leaf pop right and append right to result, pop parent root.....
    #     #Time O(n) Space O(n)
    #     while stack or root:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         node = stack.pop()
    #         result.append(node.val)
    #         root = node.right
    #     return result