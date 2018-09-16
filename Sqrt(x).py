class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # return int(x**(1/2)) #one line solution
        #Newton's method:  sqrt(x) -> x^2 - a = 0, assume the difference is less than Epsilon, slope 2pre=(pre**2-x)/distance
        EPSILON = 0.0001
        pre = x
        while abs(pre**2-x) > EPSILON:
            pre = pre - abs(pre**2-x)/(2*pre)
        return int(pre)