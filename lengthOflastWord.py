class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(' ')
        counter = 0
        while not counter == len(s):
            if s[counter] == '':
                s.pop(counter)
            else:
                counter += 1
        return len(s[-1])


solution_instance = Solution()
sol = solution_instance.lengthOfLastWord("   fly me   to   the moon  ")
print(sol)
