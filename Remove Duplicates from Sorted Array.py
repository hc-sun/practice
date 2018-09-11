# spcace complexity O(1), input sorted array
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = 0
        while temp < len(nums)-1:
            if nums[temp+1] != nums[temp]:
                temp += 1
            else:
                nums.pop(temp+1)
        return len(nums)