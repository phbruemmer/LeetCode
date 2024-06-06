class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        anchor = strs[0]

        for i in range(1, len(strs)):
            temp_anchor = ""
            for y in range(0, min(len(strs[i]), len(anchor))):
                char = strs[i][y]
                if anchor[y] == char:
                    temp_anchor += char
                else:
                    break
            anchor = temp_anchor
        return anchor




solution_instance = Solution()
prefix_list = ["cir","car"]
sol = solution_instance.longestCommonPrefix(prefix_list)
print(sol)
