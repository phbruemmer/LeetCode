class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = ""
        final = []

        for i in range(0, n):
            result += '()'
        final.append(result)
        index = 1

        for i in range(0, len(result), 2):
            print(result)

        return final

si = Solution()
sol = si.generateParenthesis(3)
print(sol)
