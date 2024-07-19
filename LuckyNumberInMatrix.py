class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        num_columns = len(matrix[0])
        max_values = [0] * num_columns
        min_values = []

        for row in matrix:
            min_values.append(min(row))
            for col in range(0, num_columns):
                if row[col] > max_values[col]:
                    max_values[col] = row[col]
        return list(map(lambda x: x, set(max_values) & set(min_values)))


si = Solution()
sol = si.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]])
print(sol)
