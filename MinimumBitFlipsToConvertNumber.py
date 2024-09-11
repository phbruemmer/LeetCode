class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        return bin(start ^ goal).count("1")


si = Solution()
sol = si.minBitFlips(10, 7)
print(sol)
