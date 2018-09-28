class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return len(nums) != len(set(nums)) # one line solution
        temp = set()
        for n in nums:
            if n in temp:
                return True
            temp.add(n)
        return False
# Input: [1,2,3,1]
# Output: true
# Input: [1,2,3,4]
# Output: false