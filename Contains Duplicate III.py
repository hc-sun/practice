class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        #O(n*k)
        # if t == 0 and len(nums) == len(set(nums)): 
        #     return False
        # for i in range(len(nums)):
        #     for j in range(i+1, i+k+1):
        #         if j >= len(nums):
        #             break
        #         if abs(nums[i]-nums[j]) <= t:
        #             return True
        # return False

        #O(n)
        if t < 0:
            return False
        dic = {}
        for i in range(len(nums)):
            if i-k > 0: #buckets: key:num[i]//(t+1) value:nums[i], abs(nums[i]-nums[j])<=t abs(nums[i]/t-nums[j]/t)<=1, nums[j] belongs to nums[i]/t or nums[i]/t-1 or nums[i]/t+1
                #buckets are 0,t t+1,2t+1, 2t+2,3t+2
                del dic[nums[i-k-1]//(t+1)]
            key = nums[i]//(t+1)
            if key in dic:
                return True
            if key-1 in dic and abs(nums[i] - dic[key-1]) <= t:
                return True
            if key+1 in dic and abs(nums[i] - dic[key+1]) <= t:
                return True
            dic[key] = nums[i]           
        return False
        
# Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false