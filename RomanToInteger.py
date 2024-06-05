class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_types = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0

        for i in range(0, len(s)):
            current = roman_types[s[i]]
            if not i + 1 >= len(s) and roman_types[s[i + 1]] > current:
                current = current * -1
            result += current
        return result

solution_instance = Solution()
romanStr = "MCMXCIV"
sol = solution_instance.romanToInt(romanStr)
print(sol)
