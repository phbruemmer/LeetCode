class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        counter = 0
        for i in nums:
            if i == target:
                return counter
            elif i > target:
                return counter
            counter += 1
        return counter




solution_instance = Solution()
nums_array = [1,3,5,6]
target_var = 7
sol = solution_instance.searchInsert(nums_array, target_var)
print(sol)
