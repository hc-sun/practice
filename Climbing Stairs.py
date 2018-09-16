class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #dynamic programming, list of sums, n[i]=n[i-1]+n[i-2]
        nums = [1, 2]
        for i in range(2, n):
            nums.append(nums[i-1] + nums[i-2])
        return nums[n-1]
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step