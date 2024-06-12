class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        items = {}
        forbidden_nums = {}

        for i in nums:
            if i not in forbidden_nums:
                items.setdefault(i, 0)
                items[i] += 1
            if items[i] >= 2:
                items.pop(i)
                forbidden_nums.setdefault(i, 0)
        return list(items.keys())[0]



si = Solution()
sol = si.singleNumber([4,1,2,1,2])
print(sol)