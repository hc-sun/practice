class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        temp = []
        return self.happyHelper(n, temp)
    
    def happyHelper(self, n, nums):
        if n == 1:
            return True
        elif n in nums:
            return False
        else:
            nums.append(n)
            result = 0
            for i in str(n):
                result += int(i) ** 2
            return self.happyHelper(result, nums)
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1