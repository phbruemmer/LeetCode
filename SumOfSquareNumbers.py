from math import sqrt


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0

        while True:
            if (pow(int(sqrt(c - pow(a, 2))), 2)) == (c - pow(a, 2)):
                return True
            a += 1
            if pow(a, 2) + pow(a, 2) > c:
                break
        return False


si = Solution()
sol = si.judgeSquareSum(999999999)
print(sol)
