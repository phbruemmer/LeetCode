class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        int_to_bin = bin(n)
        counter = 0
        for i in int_to_bin:
            if i == '1':
                counter += 1
        return counter



si = Solution()
sol = si.hammingWeight(128)
print(sol)
