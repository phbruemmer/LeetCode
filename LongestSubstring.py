class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        container = {}
        temp_str = ""
        test_str = ""

        for i in range(0, len(s)):
            start_point = s[i]
            temp_str += start_point
            container.setdefault(start_point, 0)
            container[start_point] += 1
            print(start_point)
            for y in range(i + 1, len(s)):
                if s[y] == start_point or s[y] in container:
                    break
                container.setdefault(s[y], 0)
                container[s[y]] += 1
                temp_str += s[y]
            container.clear()
            if len(test_str) < len(temp_str):
                test_str = temp_str
            temp_str = ""
        return len(test_str)


solution_instance = Solution()
start_str = "dvdf"
sol = solution_instance.lengthOfLongestSubstring(start_str)
print(sol)


"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        :type s: str
        :rtype: int
        - Gehe durch die Liste...
        - A ... A

        container = {}
        temp_str = ""
        test_str = ""

        for i in s:
            if i in container:
                temp_str = ""
                temp_str += i
                container.clear()
            else:
                temp_str += i

            if len(temp_str) > len(test_str):
                test_str = temp_str
            container.setdefault(i, 0)
            container[i] += 1

        print(s.find(test_str))
        print(test_str)
        return len(test_str)
"""
