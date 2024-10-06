class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.split(' ')
        counter = 0
        new_sentence = ""

        for word in s:
            counter += 1
            new_sentence += word
            if counter == k:
                break
            else:
                new_sentence += " "
        return new_sentence


si = Solution()
sol = si.truncateSentence("What is the solution to this problem", 4)
print(sol)
