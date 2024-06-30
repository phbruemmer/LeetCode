class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        brackets = [-1]
        result = 0
        for i in range(0, len(s)):
            if s[i] == '(':
                brackets.append(i)
            else:
                brackets.pop()
                if len(brackets) == 0:
                    brackets.append(i)
                result = max(result, i - brackets[-1])
        return result





    """longest_valid_parenthesis = ""
        temp = ""

        for i in s:
            if i == ')' and opening_brackets[i] == opening_brackets['(']:
                temp = ""
            else:
                print(i)
                temp += i
                opening_brackets[i] += 1
            if len(temp) > len(longest_valid_parenthesis):
                longest_valid_parenthesis = temp
        return len(longest_valid_parenthesis)"""




    """min_brackets = min(opening_brackets['('], opening_brackets[')'])
        max_brackets = max(opening_brackets['('], opening_brackets[')'])
        res = max_brackets - min_brackets"""



    """ max_val = max(opening_brackets['('], opening_brackets[')'])
        min_val = min(opening_brackets['('], opening_brackets[')'])
        result = (max_val - min_val) * 2

        if min_val == 0 and not max_val == 0:
            result = 0
        elif min_val == max_val:
            result = min_val * 2"""


si = Solution()
sol = si.longestValidParentheses("(()))")
print(sol)
