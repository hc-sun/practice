class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > max_profit:
        #             max_profit = prices[j] - prices[i]
        min_price = float('inf')
        for i in range(len(prices)):
            min_price = min(min_price,  prices[i]) # restarts from the lowest val
            max_profit = max(max_profit, prices[i]-min_price) # profit only keep the largest profit
        return max_profit
        return max_profit
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.       