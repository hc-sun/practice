# haystack.index(needle)
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle or haystack == needle:
            return 0
        i = 0
        j = 0
        while i < len(haystack) - len(needle) + 1:
            if haystack[i] == needle[0]:
                while True:
                    j += 1
                    if j == len(needle):
                        return i
                    elif haystack[i+j] != needle[j]:
                        j = 0
                        break                 
            i += 1
        return -1

# Input: haystack = "hello", needle = "ll"
# Output: 2