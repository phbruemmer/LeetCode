class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = ""
        if x < 0:
            result += "-"
        elif x == 0:
            return 0
        x = abs(x)
        temp_num = x
        digit = 0

        while temp_num >= 1:
            cur_digit = x // 10 ** digit % 10
            result += str(cur_digit)
            digit += 1
            temp_num //= 10
        result = int(result)
        if result >= 2**31 or result <= -2**31:
            return 0
        return result


si = Solution()
sol = si.reverse(75438975)
print(sol)
