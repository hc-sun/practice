class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        num = 0
        for i in bin(n)[2:].strip('0'):
            if i == '1':
                num += 1
        return num
# Input: 11
# Output: 3
# Explanation: Integer 11 has binary representation 00000000000000000000000000001011