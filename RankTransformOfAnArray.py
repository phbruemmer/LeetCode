class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        n_arr = sorted(set(arr))
        hm = {}
        final = []

        for i in range(0, len(n_arr)):
            hm[n_arr[i]] = i

        for i in arr:
            final.append(hm[i] + 1)
        return final



arr = [100, 100, 100]
si = Solution()
sol = si.arrayRankTransform(arr)
print(sol)
