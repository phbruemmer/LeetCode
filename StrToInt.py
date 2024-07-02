class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        final = ""
        valid_digits = {"0": 0,
                        "1": 1,
                        "2": 2,
                        "3": 3,
                        "4": 4,
                        "5": 5,
                        "6": 6,
                        "7": 7,
                        "8": 8,
                        "9": 9}
        nums = []

        for i in s:
            if i in valid_digits:
                final += i
            else:
                nums.append(final)
                final = ""
        nums.append(final)
        print(nums)
        return max(nums)


solution_instance = Solution()
sol = solution_instance.myAtoi("1337c0d3")
print(sol)
