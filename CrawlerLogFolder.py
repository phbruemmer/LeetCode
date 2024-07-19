class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        result = 0

        for i in logs:
            if i == "../":
                if not result == 0:
                    result -= 1
            elif i == "./":
                pass
            else:
                result += 1

        return result


si = Solution()
sol = si.minOperations(["./","../","./"])
print(sol)
