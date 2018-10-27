# def max_array_size(nums, k): #O(n) Time
#     max_size = 0
#     for i in range(len(nums)):
#         for j in range(i, len(nums)):
#             if sum(nums[i:j]) == k:
#                 max_size = max(max_size, j-i)
#     return max_size

def max_array_size(nums, k): #O(n)
    if not nums:
        return 0
    max_size = 0
    dic = {0:-1} # use a dictionary store sum:idx, initialize 0:-1 since we need to calculate the len later which starts from 0
    curr_sum = 0
    for idx in range(len(nums)):
        curr_sum += nums[idx]
        if curr_sum not in dic:
            dic[curr_sum] = idx
        temp = curr_sum - k # temp is the difference
        if temp in dic: # if we have got the diff before, then we can get the size by idx-prev_idx
            prev_idx = dic.get(temp)
            max_size = max(max_size, idx-prev_idx)
    return max_size

# Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
# Note:
# The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.
# Input: nums = [1, -1, 5, -2, 3], k = 3
# Output: 4 
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
# Input: nums = [-2, -1, 2, 1], k = 1
# Output: 2 
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.