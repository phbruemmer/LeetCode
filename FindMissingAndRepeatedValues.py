class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        solution_arr = [0, 0]

        grid_size = len(grid) ** 2

        mappy_map = {}

        for num in range(1, grid_size + 1):
            mappy_map[num] = 0

        for y in grid:
            for x in y:
                mappy_map[x] += 1

        for key, value in mappy_map.items():
            if value == 0:
                solution_arr[1] = key
            elif value == 2:
                solution_arr[0] = key

        return solution_arr


grid_ = [[1,3],[2,2]]
instance = Solution()
sol = instance.findMissingAndRepeatedValues(grid_)
print(sol)
