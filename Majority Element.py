class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return [num for num in set(nums) if nums.count(num) > len(nums)//2][0]
        # use hash table
# Input: [3,2,3]
# Output: 3