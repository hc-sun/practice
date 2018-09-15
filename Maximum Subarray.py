class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            if nums[i] > 0: #dynamic programming, change nums to a list of large sumresults, if num[i]>0 then substr(next) must add it()
                nums[i+1] += nums[i]
        return max(nums)
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.