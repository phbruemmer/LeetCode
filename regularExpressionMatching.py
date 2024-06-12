class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        any_chars = False

        last_char = ''
        continue_last_chars = False

        for i in range(0, len(p)):
            if p[i] == '.':
                any_chars = True
            elif p[i] == '*':
                last_char = p[i - 1]
                continue_last_chars = True

        if not any_chars and not continue_last_chars:
            if s == p:
                return True
            else:
                return False

        for i in range(0, len(s)):
            if not any_chars and continue_last_chars:
                if not s[i] == last_char:
                    return False

        return True



"""

Work on this problem later

"""


solution_instance = Solution()
sol = solution_instance.isMatch("aab", "c*a*b")
print(sol)
