class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for ch in s:  
            num = num*26 + (ord(ch)-64) # ord('A') -> 65
        return num
# Input: "A"
# Output: 1
# Input: "AB"
# Output: 28