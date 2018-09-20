class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = ''.join(ch for ch in s if ch.isalnum()).lower()
        return temp == temp[::-1]
# Input: "A man, a plan, a canal: Panama"
# Output: true