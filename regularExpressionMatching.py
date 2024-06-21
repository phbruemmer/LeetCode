class Solution(object):
    def isMatchRecursive(self, s, p):
        # two exit condition of recursive
        # both are empty string
        if not s and not p:
            return True
        # s is not empty but p is empty
        if s and not p:
            return False
        # check if current characters are match
        cur_char_match = (s and s[0] == p[0]) or p[0] == '.'
        # split according to cur_char_match
        if cur_char_match:  # two are match
            if p[1:] and p[1] == '*':  # next character is '*'
                # repeat zero count
                zero_match = self.isMatchRecursive(s, p[2:])
                if zero_match:
                    return zero_match
                # repeat at least one time
                if s:  # if s is not empty
                    return self.isMatchRecursive(s[1:], p)
            else:  # next character is not '*'
                if s:
                    return self.isMatchRecursive(s[1:], p[1:])
        # two are not match
        if p[1:] and p[1] == '*':  # next character is '*'
            return self.isMatchRecursive(s, p[2:])

        # other condition all set to False
        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.isMatchRecursive(s, p)


si = Solution()
s = ''
p = ''
sol = si.isMatch(s, p)
print(sol)
