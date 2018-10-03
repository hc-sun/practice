class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        for ch in set(s):
            if s.count(ch) != t.count(ch):
                return False
        return True
# Given two strings s and t , write a function to determine if t is an anagram of s.
# Input: s = "anagram", t = "nagaram"
# Output: true
# Input: s = "rat", t = "car"
# Output: false