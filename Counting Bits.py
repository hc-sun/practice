class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #return [bin(i).count('1') for i in range(num+1)]
        
        #if number&1 == 1 then its most right bit is 1, right shift>>
        result = [0]
        for i in range(1, num+1):         
            #result.append(result[i>>1]+(i&1))
            result.append(result[i&(i-1)]+1) #(number-1)&number will change the number's most right 1 to 0
        return result

# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Input: 2
# Output: [0,1,1]

# Input: 5
# Output: [0,1,1,2,1,2]
# Follow up:
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.