class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        li = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        rem = num
        result = ""
        for i in range(13):
            quo, rem = divmod(rem, li[i])
            result += quo * dic[i]
        return result

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Input: 3
# Output: "III"
# Input: 4
# Output: "IV"
# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.