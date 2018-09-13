# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) < 1:
#             return 0
#         length = 1
#         temp = []
#         for i in range(len(s)):
#             for j in range(i+1, len(s)-2):

#                 if s[i] not in s[i+1:j]:
#                     if j-i > length:
#                         length = j-i
#                 else:
#                     break
#         return length

##sliding window
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = []
        length = 0
        for ch in s:
            if ch in temp:
                temp = temp[temp.index(ch)+1:]
            temp.append(ch)
            if length < len(temp):
                length = len(temp)
        return length

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.