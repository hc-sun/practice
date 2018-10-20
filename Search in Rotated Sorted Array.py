class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]: #make sure the target can be directly compared if it's in left part
                if nums[l] <= target < nums[mid]: #target is in left part
                    r = mid - 1
                else: #target is in right part
                    l = mid + 1
            else: #there is a rotation in left part, the target can be directly compared in right part
                if nums[mid] < target <= nums[r]: #target is in right part
                    l = mid + 1
                else:#target is in left part
                    r = mid - 1
        return -1
                    
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.
# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4