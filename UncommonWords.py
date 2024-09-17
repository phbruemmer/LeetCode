class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        s3 = {}

        for i in s1.split(' '):
            s3[i] = s3.setdefault(i, 0) + 1

        for i in s2.split(' '):
            s3[i] = s3.setdefault(i, 0) + 1
        return [uncommon_word for uncommon_word in s3 if s3[uncommon_word] == 1]


si = Solution()
sol = si.uncommonFromSentences("this apple is sweet", "this apple is sour")
print(sol)
