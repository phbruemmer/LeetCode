class Solution(object):
    def maximumImportance(self, n, roads):
        values = {}
        for road in roads:
            values[road[0]] = values.get(road[0], 0) + 1
            values[road[1]] = values.get(road[1], 0) + 1

        sorted_map = sorted(values.items(), key=lambda item: item[1], reverse=True)
        total_importance = 0

        for val in sorted_map:
            val = val[1]
            total_importance += val * n
            n -= 1

        return total_importance


si = Solution()
sol = si.maximumImportance(5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]])
print(sol)
