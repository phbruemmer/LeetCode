class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniques = []
        counter = 0

        while not len(nums) <= counter:
            if nums[counter] in uniques:
                nums.pop(counter)
                counter -= 1
            else:
                uniques.append(nums[counter])
            counter += 1
        return len(nums)


solution_instance = Solution()
int_list = [0,0,1,1,1,2,2,3,3,4]
sol = solution_instance.removeDuplicates(int_list)
print(sol)
