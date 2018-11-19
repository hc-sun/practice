class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # nums.sort()
        # result = set()
        # for i in range(len(nums)-3):
        #     for j in range(i+1, len(nums)-2):
        #         l = j + 1
        #         r = len(nums) - 1
        #         while l < r:
        #             comb = (nums[i], nums[j], nums[l], nums[r])
        #             if sum(comb) == target:
        #                 result.add(comb)
        #                 l += 1
        #                 r -= 1
        #             elif sum(comb) > target:
        #                 r -= 1
        #             else:
        #                 l += 1
        # return list(result)


        nums.sort()
        return [list(i) for i in self.nSum(nums, 4, target)]
    def nSum(self, nums, n, target):
        result = set()
        if n == 2: #2sum
            l, r = 0, len(nums)-1
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    result.add((nums[l], nums[r]))
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    l += 1
        else: #reduce n
            for i in range(len(nums) - n + 1):
                if i == 0 or nums[i - 1] != nums[i]:
                    result |= set((nums[i],) + m for m in self.nSum(nums[i+1 :], n-1, target - nums[i]))
        return result

# Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
# The solution set must not contain duplicate quadruplets.

# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]