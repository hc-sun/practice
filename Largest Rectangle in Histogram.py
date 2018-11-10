class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [] #indices of heights in ascending order
        result = 0
        heights.append(0) #append zero height to make sure the last height is compared
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]: ##keep poping when meet a lower height(current height < highest height),and calculating areas
                height = heights[stack.pop()]  #pop heighest height in stack    
                width = i - stack[-1] - 1 if stack else i #width is current height idx(right) - poped higher height idx(left) - 1, if empty then current height's idx(right) is width
                result = max(result, height*width)
                print("height {0} * width {1} = {2}, and result {3}".format(height, width, height*width, result))
            stack.append(i) #if current height is higher append idx to stack
        heights.pop()
        return result

# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# Input: [2,1,5,6,2,3]
# Output: 10

# [0]
# height 2 * width 1 = 2, max_area 2
# [1]
# [1, 2]
# [1, 2, 3]
# height 6 * width 1 = 6, max_area 6
# height 5 * width 2 = 10, max_area 10
# [1, 4]
# [1, 4, 5]
# height 3 * width 1 = 3, max_area 10
# height 2 * width 4 = 8, max_area 10
# height 1 * width 6 = 6, max_area 10
# [6]