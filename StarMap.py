class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        common = ""

        for i in range(0, len(edges)):
            for y in i:
                print(edges[i])
                print(edges[i + 1])
                print(y)

si = Solution()
sol = si.findCenter([[1,2],[2,3],[4,2]])
print(sol)