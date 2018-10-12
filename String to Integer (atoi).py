import re
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        reg = re.match(r"[\s]*[\+\-]?[\d]+", str) #re.mathch no new line, re.search searche entire string
        if not reg:
            return 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        return max(min(int(reg.group(0)), INT_MAX), INT_MIN)
        # .group(0) entire match, .group(i) i_th parenthesized subgroup

# Input: "42"
# Output: 42
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.