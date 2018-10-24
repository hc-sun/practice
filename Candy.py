class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):#make sure right person gets more candies than left
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1]+1
        for i in range(len(ratings)-2, -1, -1): #make sure left person also gets more
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:#if left higer than left and in candies left gets less
                candies[i] = candies[i+1] + 1 #then change left candies
        return sum(candies)    

# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.