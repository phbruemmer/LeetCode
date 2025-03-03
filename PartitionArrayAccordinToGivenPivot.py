class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        first_arr = []
        middle_arr = []
        second_arr = []

        for i in nums:
            if i < pivot:
                first_arr.append(i)
            elif i > pivot:
                second_arr.append(i)
            elif i == pivot:
                middle_arr.append(i)

        nums = first_arr + middle_arr + second_arr
        return nums



sol = Solution()
bratwurscht = sol.pivotArray([9, 12, 5, 10, 14, 3, 10], 10)

print(bratwurscht)

# [9,5,3,10,10,12,14]
