class Solution:
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     if len(s) < 2:
    #         return s
    #     palins = []
    #     for i in range(len(s)):
    #         for j in range(i,len(s)+1):
    #             temp = s[i:j]
    #             if temp == temp[::-1]:
    #                 if len(temp)>len(palins):
    #                     palins = temp
    #     return palins

    def longestPalindrome(self, s): #O(n^2) solution
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for i in range(len(s)): # from s[i] use parlin_helper adding left and right
            temp = self.palin_helper(s, i, i) # start is one char 'a' to 'bab'
            if len(temp) > len(result):
                result = temp
            temp = self.palin_helper(s, i, i+1) # starting from 'aa' to 'baab'
            if len(temp) > len(result):
                result = temp
        return result

    def palin_helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]: #keep adding if left==right
            l -= 1
            r += 1
        return s[l-1:r] # previous index
# Input: "babad"
# Output: "bab"