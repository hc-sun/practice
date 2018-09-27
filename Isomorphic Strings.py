class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # if len(s) <= 1:
        #     return True
        # for i in range(len(s)):
        #     if [x for x, val in enumerate(s) if val == s[i]] != [y for y, val in enumerate(t) if val == t[i]]:
        #         return False
        # return True
        dic = {}
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] != t[i]:
                return False
            if s[i] not in dic and t[i] in dic.values():
                return False
            dic[s[i]] = t[i]
        return True