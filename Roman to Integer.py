class Solution:
    def romanToInt(self, s):
        symbles = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        pre_num = 1000
        for i in range(len(s)):
            current_num = symbles.get(s[i])
            if pre_num < current_num:
                num += current_num - pre_num*2
                pre_num = current_num
            else:
                num += current_num
                pre_num = current_num
        return num

# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.