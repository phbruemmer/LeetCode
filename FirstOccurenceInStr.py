class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


solution_instance = Solution()
haystack = "leetcode"
needle = "leeto"
sol = solution_instance.strStr(haystack, needle)
print(sol)
