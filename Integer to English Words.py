# Given input is guaranteed to be less than 231 - 1.
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        result = ""
        nineteen = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tys = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["","Thousand","Million","Billion"]
        def helper(num): #get english words, less than a thousand prefix
            if num == 0: return "" #when the num is less than 1000, it's already calculated so skip
            elif num < 20:
                return nineteen[num] + " "
            elif num < 100:
                return tys[num//10] + " " + helper(num%10)
            else:#greater than 100
                return nineteen[num//100] + " Hundred " + helper(num%100)
        for i in range(4): #2**31 is 2147483648(2billion) which needs to divide 1000 for 4 times to get a num less than 1000
            if num % 1000 != 0:
                result = helper(num%1000) + thousands[i] + " " + result #keep adding to result from lowest 000 to higiest
            num //= 1000
        return result.strip()
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
