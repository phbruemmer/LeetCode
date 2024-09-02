class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        chalk_sum = 0

        for i in range(0, len(chalk)):
            chalk_sum += chalk[i]
        k -= (chalk_sum * (k // chalk_sum))

        for i in range(0, len(chalk)):
            k -= chalk[i]
            if k < 0:
                return i


si = Solution()
sol = si.chalkReplacer([32,89,30,66,25,25,80,54,21,61,96,76,74,9,9,24,31,79,45,18,8,14,30,28,85,76,69,98,80,24,23,41,47,99,4,5,88,9,17,41,52,61,2,54,68,40,29,33,90,63,83,88,68,57,2,93,77,40,86,11,58,85,59,100,72,98,44,1,70,83,58,43,63,74,42,8,32,80,14,90,92,15,6], 904272687)
print(sol)
