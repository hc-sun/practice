class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            key = tuple(sorted(s))
            dic[key] = dic.get(key, []) + [s]
        return dic.values()

# Given an array of strings, group anagrams together.
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
# All inputs will be in lowercase.
# The order of your output does not matter.