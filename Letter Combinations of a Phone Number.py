class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        result = [""]
        for digit in digits:
            temp = []
            for comb in result:#loop previous letters
                for ch in dic[digit]:#loop current letters
                    temp.append(comb+ch)
            result = temp
        return result

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
# Although the above answer is in lexicographical order, your answer could be in any order you want.