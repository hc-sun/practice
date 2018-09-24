class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        if n == 0:
            return 0
        binary = bin(n)[2:]
        binary = '0'*(32-len(binary)) + binary
        return int(binary[::-1].lstrip('0'), 2)
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
#              return 964176192 represented in binary as 00111001011110000010100101000000.