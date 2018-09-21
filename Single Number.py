class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # temp = {}
        # for i in nums:
        #     if i in temp:
        #         temp.pop(i)
        #     else:
        #         temp[i] = 1
        # return list(temp.keys())[0]
        
        # a XOR a =0    a XOR b XOR a=b
        a = 0
        for i in nums:
            a ^= i
        return a
# Input: [2,2,1]
# Output: 1