class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pares = {'(':')', '[':']', '{':'}'}
        #'([]{})'
        # )]
        stack = []
        for p in s:
            if p in pares:
                stack.append(pares[p]) # store corr right parentheses
            elif not stack or p != stack.pop(): # if stack is empty(not found left) or right does not match
                return False
        return not stack #if not empty return false '['