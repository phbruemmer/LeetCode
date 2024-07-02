class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        intersect = []

        for i in nums1:
            if i in nums2:
                intersect.append(i)
                nums2.remove(i)
        return intersect


si = Solution()
sol = si.intersect([1,2,2,1], [2, 2])
print(sol)
