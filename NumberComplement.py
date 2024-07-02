class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = ""
        for i in bin(num)[2:]:
            if i == "1":
                result += "0"
            else:
                result += "1"
        return int(result, 2)


si = Solution()
sol = si.findComplement(5)
print(sol)
