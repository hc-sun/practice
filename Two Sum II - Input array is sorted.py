class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for idx, key in enumerate(numbers):
            if target - key in dict:
                return dict[target-key], idx+1 # stored index and current index
            else:
                dict[key] = idx+1
        
        #method2: two pointers: 0, len(numbers)-1
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]