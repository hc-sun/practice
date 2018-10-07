class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return nums[-1] + 1 # len(nums)==1
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
# Input: [3,0,1]
# Output: 2