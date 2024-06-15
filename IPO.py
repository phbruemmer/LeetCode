class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        """
        :type k: int
        :type w: int
        :type profits: List[int]
        :type capital: List[int]
        :rtype: int
        """
        counter = 0

        capital.append(0)

        for i in range(0, len(profits)):
            cur_profit = profits[i]
            cur_capital = capital[i]
            next_capital = capital[i + 1]
            if w == cur_capital and not w == next_capital:
                w += cur_profit
                counter += 1
            elif w > cur_capital:
                w += cur_profit
                counter += 1
        return w


si = Solution()
k_ = 2
w_ = 0
profits_ = [1, 2, 3]
capital_ = [0, 1, 1]
sol = si.findMaximizedCapital(k_, w_, profits_, capital_)
print(sol)
