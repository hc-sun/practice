class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #two pointers
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: max area is from height[1] to height[8] which is 7 multiply lower num which is height[8]