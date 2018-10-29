# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) == 0:
            return 0
        result = 0
        for i in range(len(points)):
            curr_max = 0
            same_count = 0
            vertical = 0
            dic = {}# use slope as key, count the appearances of slope
            for j in range(i+1, len(points)):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same_count += 1
                elif points[i].x == points[j].x:
                    vertical += 1
                else:
                    a = points[j].x - points[i].x
                    b = points[j].y - points[i].y
                    gcd = self.gcd_helper(a, b)
                    a //= gcd
                    b //= gcd
                    slope = str([a, b])
                    try:
                        dic[slope] += 1
                    except:
                        dic[slope] = 1
                    curr_max = max(curr_max, dic[slope])
                curr_max = max(curr_max, vertical)
            result = max(result, curr_max+same_count+1)
        return result
    #The Euclidean algorithm calculates the greatest common divisor (GCD) of two natural numbers a and b. 
    #The greatest common divisor g is the largest natural number that divides both a and b without leaving a remainder.
    def gcd_helper(self, a, b):
        while b:
            a, b = b, a % b
        return a

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4

# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6