class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        return numBottles + (numBottles - 1) // (numExchange - 1)


si = Solution()
sol = si.numWaterBottles(15, 4)
print(sol)
