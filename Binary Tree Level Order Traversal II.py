# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root] #iterable
        result = []
        while level:
            level_result = []
            temp = []
            for node in level:
                level_result.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            level = temp # next level
            result.insert(0, level_result)
        return result

# Input: [3,9,20,null,null,15,7]
# Output: [[15,7],[9,20],[3]]