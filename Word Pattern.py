class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strs = str.split(' ')
        if len(pattern) != len(strs):
            return False
        if len(set(pattern)) != len(set(strs)): #"abba" "dog dog dog dog"
            return False
        dic = {}
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                dic[pattern[i]] = strs[i] #{'a':'dog', 'b':'cat'}
            else:
                if dic[pattern[i]] != strs[i]:
                    return False
        return True
# Given a pattern and a string str, find if str follows the same pattern.
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false