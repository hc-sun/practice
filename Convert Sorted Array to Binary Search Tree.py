# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) <= 0:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        if mid - 1 >= 0:
            root.left = self.sortedArrayToBST(nums[:mid])
        if mid + 1 < len(nums):
            root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
# self-balancing/height-balanced binary search tree, depth of the two subtrees of every node never differ by more than 1
# Input: [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]