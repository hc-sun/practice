class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left <= right:
            mid = (left + right)//2
            if mid*mid > num:
                right = mid - 1
            elif mid*mid < num:
                left = mid + 1
            else:
                return True
        return False

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Input: 16
# Output: true

# Input: 14
# Output: false