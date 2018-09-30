class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return bin(n).count('1') == 1 #bitwise
# Given an integer, write a function to determine if it is a power of two.
# Input: 16
# Output: true
# Explanation: 24 = 16