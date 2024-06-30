class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def calculate(num):
            return sum(int(digit) ** 2 for digit in str(num))

        repeated_character = set()

        while n != 1 and n not in repeated_character:
            repeated_character.add(n)
            n = calculate(n)
        return n == 1



si = Solution()
sol = si.isHappy(2)
print(sol)