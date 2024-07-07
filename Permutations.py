class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def calculate_numbers():
            for i in range(0, len(nums)):
                print(i)
        calculate_numbers()
        return True




si = Solution()
sol = si.permute([1,2,3])
print(sol)
