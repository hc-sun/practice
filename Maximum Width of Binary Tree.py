class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #max width is most right node-most left node,
        # each level most left node is 2*previous position and continus.., root is position 1
        # most right node is 2*previous+1, and continues (e.g., next level is 2(2*prev+1)+1)

        queue = [(root, 0)]
        max_width = 0
        while queue:
            level = []
            for node, pos in queue:
                if node.left:#only save most left and right node and position
                    level.append((node.left, pos*2))
                if node.right:
                    level.append((node.right, pos*2+1))
            max_width = max(max_width, queue[-1][1]-queue[0][1]+1)   
            queue = level
        return max_width

# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.
# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:
# Input: 

#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:
# Input: 

#           1
#          /  
#         3    
#        / \       
#       5   3     
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:
# Input: 

#           1
#          / \
#         3   2 
#        /        
#       5      
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:
# Input: 

#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
# Note: Answer will in the range of 32-bit signed integer.