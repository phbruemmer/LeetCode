import string


class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        odds = 0
        valid = False

        for i in range(0, len(arr)):
            cur_item = arr[i]
            if cur_item % 2 == 0:
                odds = 0
            else:
                odds += 1
            if odds >= 3:
                valid = True
                break
        return valid


si = Solution()
sol = si.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12])
print(sol)
