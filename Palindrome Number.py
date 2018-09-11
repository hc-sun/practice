class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        temp = len(x) - 1
        for i in range(len(x)):
            if x[i] == x[temp]:
                if i == temp or temp == 0:
                    return True
                else:
                    temp -= 1
            else:
                return False

# Input: 121
# Output: true
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        palins = []
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                temp = s[i:j]
                if temp == temp[::-1]:
                    if len(temp)>len(palins):
                        palins = temp
        return palins
# Input: "babad"
# Output: "bab"
    