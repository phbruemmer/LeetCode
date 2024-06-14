class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp_num = x
        digit = 0
        result = 0

        digits = []

        while temp_num >= 1:
            cur_digit = x // 10 ** digit % 10
            digits.append(cur_digit)
            digit += 1
            temp_num //= 10
        print(result)


si = Solution()
sol = si.reverse(123)
print(sol)
