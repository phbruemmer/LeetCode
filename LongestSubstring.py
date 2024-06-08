class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        container = {}

        for i in s:
            container.setdefault(i, 0)
            container[i] += 1
            print(i)
        print(container)


solution_instance = Solution()
start_str = "pwwkew"
sol = solution_instance.lengthOfLongestSubstring(start_str)
print(sol)
