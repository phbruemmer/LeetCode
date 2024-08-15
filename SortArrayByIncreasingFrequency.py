class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_counter = {}

        for i in nums:
            print(i)
            num_counter.setdefault(i, 0)
            num_counter[i] += 1

        nums = sorted(nums, key=lambda x: (num_counter[x], -x))
        return nums


si = Solution()
sol = si.frequencySort([2, 3, 1, 3, 2])
print(sol)
