class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        while not len(nums) <= counter:
            if nums[counter] == val:
                nums.pop(counter)
                counter -= 1
            counter += 1
        return len(nums)


solution_instance = Solution()
sol = solution_instance.removeElement([3,2,2,3], 3)
print(sol)