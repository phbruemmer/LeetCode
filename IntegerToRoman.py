class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num >= 1 or not num <= 3999:
            return -1

        romans = {
            0: '',
            1: 'I',
            4: 'VI',
            5: 'V',
            9: 'XI',
            10: 'X',
            40: 'LX',
            50: 'L',
            90: 'CX',
            100: 'C',
            400: 'DC',
            500: 'D',
            900: 'MC',
            1000: 'M',
            5000: ''}

        if num in romans:
            return romans[num][::-1]

        digit_position = 0
        final = ""

        while num:
            digit = ((num // 10 ** digit_position) % 10) * 10 ** digit_position

            if digit in romans:
                final += romans[digit]
            elif digit not in romans and not digit_position == 0:
                multiplier = digit // 10 ** digit_position
                romanToLookFor = digit // multiplier
                divs, rest = divmod(multiplier, 5)
                final += (romans[romanToLookFor * 5] * divs + romans[romanToLookFor] * rest)[::-1]
            elif digit not in romans and digit_position == 0:
                divs, rest = divmod(digit, 5)
                final += (romans[5] * divs + romans[1] * rest)[::-1]
            digit_position += 1
            num -= digit
        return final[::-1]


solution_instance = Solution()
sol = solution_instance.intToRoman(101)
print(sol)
if sol == "MMMDCCXLIX":
    print("fdklsjfklasdj")