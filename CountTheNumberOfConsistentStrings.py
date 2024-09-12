class Solution(object):
    def countConsistentStrings(self, allowed, words):
        for word in words:
            if not set(word).issubset(set(allowed)):
                words.remove(word)
        return len(words) - 1


si = Solution()
sol = si.countConsistentStrings("fstqyienx", ["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"])
print(sol)
