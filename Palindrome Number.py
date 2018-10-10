class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        temp = len(x) - 1
        for i in range(len(x)):
            if x[i] == x[temp]:
                if i == temp or temp == 0:
                    return True
                else:
                    temp -= 1
            else:
                return False

# Input: 121
# Output: true