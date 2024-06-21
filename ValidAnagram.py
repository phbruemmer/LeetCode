class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        let_counter = {}

        for i in s:
            let_counter.setdefault(i, 0)
            let_counter[i] += 1
        for i in t:
            if i not in let_counter:
                return False
            else:
                let_counter[i] -= 1
                if let_counter[i] < 0:
                    return False
        return True

si = Solution()
sol = si.isAnagram('aacc', 'ccac')
print(sol)
