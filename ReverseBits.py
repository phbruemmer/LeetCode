class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(bin(n)[2:].zfill(32)[::-1], 2)


si = Solution()
sol = si.reverseBits(int('00000010100101000001111010011100', 2))
print(sol)
