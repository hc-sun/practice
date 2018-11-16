import heapq
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # return sorted(nums)[-k]


        # nums = [-num for num in nums] #min heap to max heap
        # heapq.heapify(nums)
        # result = float('inf')
        # for i in range(k):
        #     result = heapq.heappop(nums)    
        # return -result


        heapq.heapify(nums)
        for i in range(len(nums)-k):
            heapq.heappop(nums)
        return nums[0]

# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.