class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for i in range(len(nums)):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
            else:
                idx += 1
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]