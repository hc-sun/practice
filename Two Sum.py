import sys
import argparse

class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

def main(argv):
    parser = argparse.ArgumentParser(description='Two Sum')
    parser.add_argument('-n', '--nums', default=[2, 7, 11, 15], help='List of numbers')
    parser.add_argument('-t', '--target', required=True, type=int, help='Target number')
    args = parser.parse_args()
    nums = args.nums
    target = args.target
    result = Solution().twoSum(nums, target)
    print(result)

if __name__ == '__main__':
    main(sys.argv[1:])