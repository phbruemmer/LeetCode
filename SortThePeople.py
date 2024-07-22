class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        person = {}
        sorted_list = []

        for i in range(len(names)):
            person[heights[i]] = names[i]
        heights = sorted(heights)
        for i in reversed(heights):
            sorted_list.append(person[i])
        return sorted_list


si = Solution()
sol = si.sortPeople(["Mary", "John", "Emma"], [180, 165, 170])
print(sol)
