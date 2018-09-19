class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        nums = [[1], [1,1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(nums[i-1][j-1]+nums[i-1][j])
            temp.append(1)
            nums.append(temp)
        return nums
# Input: 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]