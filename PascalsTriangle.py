class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output_list = [[1]]

        for i in range(1, numRows):
            output_list.append([1])
            for y in range(1, i):
                output_list[i].append(output_list[i - 1][y - 1] + output_list[i - 1][y])
            output_list[i].append(1)
        return output_list


si = Solution()
sol = si.generate(20)
print(sol)