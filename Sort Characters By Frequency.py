class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {} #dic = collections.Counter(s)
        for ch in s:
            if ch in dic:
                dic[ch] += 1
            else:
                dic[ch] = 1
        #dic = collections.OrderedDict(sorted(dic.items(), key=lambda x: x[1], reverse=True)) #x[1] -> key
        li = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return ''.join([i[0]*i[1] for i in li]) # dic.values() -> get values   dic.keys() -> get keys

# Given a string, sort it in decreasing order based on the frequency of characters.

# Input:
# "tree"
# Output:
# "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Input:
# "cccaaa"
# Output:
# "cccaaa"
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:

# Input:
# "Aabb"
# Output:
# "bbAa"
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.