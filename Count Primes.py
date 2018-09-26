class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        nums = [True] * n
        nums[0] = False
        nums[1] = False
        for i in range(2, n):
            if nums[i] == True:
                for j in range(2, (n-1) // i+1):
                    nums[i*j] = False
        return sum(nums)
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.