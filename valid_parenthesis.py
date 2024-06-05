class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(0, len(s)):
            print(s[i])


solution_instance = Solution()
parenthesisStr = "()[]{}"
sol = solution_instance.isValid(parenthesisStr)
print(sol)
