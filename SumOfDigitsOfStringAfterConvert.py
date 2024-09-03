class Solution(object):
    alphabet = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}

    def getLucky(self, s, k):
        result = ''

        for i in s:
            result += str(self.alphabet[i])

        final = 0
        for i in range(0, k):
            final = 0
            for y in result:
                final += int(y)
            result = str(final)
        return final


si = Solution()
sol = si.getLucky("zbax", 2)
print(sol)
