class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        return self.searchStr(nums, target, start, end)
   
    def searchStr(self, nums, target, start, end):
        mid = start + (end - start) // 2
        if target == nums[mid]:
            return mid
        elif end - start < 2:
            if target < nums[mid]:
                return mid
            else:
                return mid + 1
        elif target < nums[mid]:
            end = mid
        elif target > nums[mid]:
            start = mid
        return self.searchStr(nums, target, start, end)