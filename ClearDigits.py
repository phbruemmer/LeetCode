class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_chars = []
        last_pos = []

        for i in range(0, len(s)):
            if s[i].isdigit():
                if not last_chars:
                    for y in range(i, len(s)):
                        if not s[y].isdigit():
                            print(s[y])
                else:
                    last_char_pos = last_pos[-1]
                    s = s[:last_char_pos] + s[last_char_pos + 1:]
                    last_chars.pop(-1)
                    last_pos.pop(-1)
                s = s[:i] + s[i + 1:]
            else:
                last_chars.append(s[i])
                last_pos.append(i)
        return s


si = Solution()
sol = si.clearDigits("cb34")
print(sol)
