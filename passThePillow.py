class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        rest = time // (n - 1)
        return (time % (n - 1) + 1) if rest % 2 == 0 else (n - time % (n - 1))


si = Solution()
sol = si.passThePillow(18, 38)
print(sol)
