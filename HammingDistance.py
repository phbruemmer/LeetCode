class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:]
        y = bin(y)[2:]
        max_len = max(len(x), len(y))
        x = x.zfill(max_len)
        y = y.zfill(max_len)

        counter = 0

        for i in range(0, max_len):
            if not x[i] == y[i]:
                counter += 1

        return counter


si = Solution()
sol = si.hammingDistance(3, 1)
print(sol)
