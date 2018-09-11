class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums) and len(nums) > 0:
            if nums[i] == val:
                nums.pop(i)
                continue
            i += 1
        return len(nums)
# in: nums = [3,2,2,3], val = 3
# out: 2