# cannot add adjacent nums
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dynamic programming
        # keep saving the total robbed amount
        
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)      
        nums[1] = max(nums[0], nums[1]) #[2,1,1,2]
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1], nums[i]+nums[i-2])           
        return nums[-1]
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.