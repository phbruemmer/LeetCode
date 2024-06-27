class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        values = {}
        for i in edges:
            values.setdefault(i[0], 0)
            values[i[0]] += 1
            values.setdefault(i[1], 0)
            values[i[1]] += 1
        return max(values.items(), key=lambda item: item[1])[0]





si = Solution()
sol = si.findCenter([[1,2],[5,1],[1,3],[1,4]])
print(sol)
