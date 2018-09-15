class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        if n == 1:
            return s
        for i in range(1, n):
            val = self.next_str(s)
            s = val
            print(val)
        return s
            
    def next_str(self, s):
        num = s[0]
        next_s = ""
        count = 1
        for j in range(len(s)):
            if j == len(s) - 1: # add count for last nums
                return next_s + str(count) + num
            elif s[j+1] != num:
                next_s += str(count) + num
                num = s[j+1]
                count = 1
            else:
                count += 1
        return next_s

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.