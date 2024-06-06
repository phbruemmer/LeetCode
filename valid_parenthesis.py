class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opposite = {')': '(', '}': '{', ']': '['}
        valid = True
        last_opening_brackets = []

        for i in range(0, len(s)):
            current_bracket = s[i]
            if current_bracket == '(' or current_bracket == '{' or current_bracket == '[':
                last_opening_brackets.append(current_bracket)
            elif current_bracket in opposite:
                if last_opening_brackets and opposite[current_bracket] == last_opening_brackets[-1]:
                    last_opening_brackets.pop(-1)
                else:
                    valid = False
        if not len(last_opening_brackets) == 0:
            valid = False
        return valid


solution_instance = Solution()
parenthesis = "(("
sol = solution_instance.isValid(parenthesis)
print(sol)
