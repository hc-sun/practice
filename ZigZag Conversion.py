class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = [''] * numRows
        idx = 0
        temp = 1
        for ch in s:
            result[idx] += ch
            if idx == 0:
                temp = 1
            if idx == numRows-1:
                temp = -1
            idx += temp
        return ''.join(result)
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# P   A   H   N
# A P L S I I G
# Y   I   R
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# P     I    N
# A   L S  I G
# Y A   H R
# P     I