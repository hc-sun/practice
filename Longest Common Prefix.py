class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) is not 0:
            current_str = strs[0]
            longest = strs[0] # ["a"]
        else:
            return ""
        for i in range(1, len(strs)):
            longest = ""
            for j in range(len(current_str) if len(current_str)<len(strs[i]) else len(strs[i])):
                if current_str[j] is strs[i][j]:
                    longest += current_str[j]
                else:
                    break
            current_str = longest            
        return longest

# Input: ["flower","flow","flight"]
# Output: "fl"