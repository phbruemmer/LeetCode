class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        parenthesis = {
            '(': 0,
            ')': 0
        }

        for i in s:
            parenthesis[i] += 1
        return max(parenthesis['('], parenthesis[')']) - min(parenthesis['('], parenthesis[')'])


si = Solution()
sol = si.minAddToMakeValid("())")
print(sol)
