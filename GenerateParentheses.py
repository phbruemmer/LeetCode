class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def insert(string_, index_, char):
            return string_[:index_] + char + string_[index_:]

        def remove(string_, index_):
            return string_[:index_] + string_[index_ + 1:]

        result = ""
        final = []

        for i in range(0, n):
            result += '()'
        final.append(result)
        if n > 1:
            final.append(''.join('(' if y < n else ')' for y in range(0, n * 2)))

            index = 1

            for i in range(0, len(result) // 2):
                result = insert(result, index + 2, ")")
                result = remove(result, index)
                if result in final:
                    break
                index += 2
                final.append(result)

            for i in final:
                item = ''.join('(' if char == ')' else ')' for char in reversed(i))
                if not item in final:
                    final.append(item)
        return final


si = Solution()
sol = si.generateParenthesis(4)
print(sol)

"""

["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]...

['()()()()', '(((())))', '(())()()', '(()())()', '(()()())', '()()(())', '()(()())']

"""