class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # arr = sorted(nums1 + nums2)
        # l = len(arr)
        # if l%2 == 0:
        #     return (arr[l/2-1]+arr[l/2])/2.0
        # else:
        #     return arr[l/2]
        
        l = len(nums1) + len(nums2)
        return self.kth_small(nums1, nums2, l//2) if l%2==1 else (self.kth_small(nums1, nums2, l//2-1) + self.kth_small(nums1, nums2, l//2))/2.0   
    def kth_small(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        mid1 = len(nums1)//2
        mid2 = len(nums2)//2
        if mid1+mid2 < k:
            if nums1[mid1] > nums2[mid2]:
                return self.kth_small(nums1, nums2[mid2+1:], k-mid2-1)
            else:
                return self.kth_small(nums1[mid1+1:], nums2, k-mid1-1)
        else:
            if nums1[mid1] > nums2[mid2]:
                return self.kth_small(nums1[:mid1], nums2, k)
            else:
                return self.kth_small(nums1, nums2[:mid2], k)


# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.

# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5