class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        # num=ord('letter')    letter=chr(number)
        result = ''
        while n != 0:
            n -= 1 # 26%26=0
            result = chr(n%26 + 65) + result #65 'A', 97 'a'
            n /= 26
        return result
            
# Input: 1
# Output: "A"
# Input: 28
# Output: "AB"