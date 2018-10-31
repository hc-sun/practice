class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        #sliding window
        from collections import Counter
        result = []
        length = len(p)
        idx = 0
        pcounter = Counter(p)
        scounter = Counter(s[:length-1]) #counts of p's length-1 in s
        while idx <= len(s) - length:
            scounter[s[idx+length-1]] += 1 #start match from the first length of p in s
            if scounter == pcounter:
                result.append(idx)
            scounter[s[idx]] -= 1 #slide -> remove from most left char
            if scounter[s[idx]] == 0: #0 means this char doesn't exist, it should be removed to avoid wrong comparistion
                del scounter[s[idx]]
            idx += 1
        return result

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
# The order of output does not matter.

# Input:
# s: "cbaebabacd" p: "abc"
# Output:
# [0, 6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# Input:
# s: "abab" p: "ab"
# Output:
# [0, 1, 2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".