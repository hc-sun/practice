class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Trailing Zeros, 0 can only get from 2*5
        # 10 -> 2(2*5 plus 10) which is 10/5=2
        zeros = 0
        while n > 0:
            n /= 5
            zeros += n
        return zeros
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.