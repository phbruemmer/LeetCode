class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negatives = 0
        positives = 0

        for num in nums:
            if num < 0:
                negatives += 1
            elif num == 0:
                continue
            else:
                positives += 1
        return negatives if positives < negatives else positives


solution_instance = Solution()
sol = solution_instance.maximumCount([-3,-2,-1,0,0,1,2])
print(sol)
