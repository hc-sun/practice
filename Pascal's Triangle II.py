class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        nums = [1]
        for i in range(rowIndex):
            nums = [1] + [nums[j] + nums[j+1] for j in range(len(nums)-1)] + [1]
        return nums