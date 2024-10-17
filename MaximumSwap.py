class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        biggest_num = num
        temp_num = list(str(num))
        for i in range(len(temp_num)):
            biggest_num_index = i
            for y in range(i, len(temp_num)):
                if temp_num[y] >= temp_num[biggest_num_index]:
                    biggest_num_index = y

            if temp_num[biggest_num_index] > temp_num[i]:
                temp_num[biggest_num_index], temp_num[i] = temp_num[i], temp_num[biggest_num_index]
                swapped_num = int(''.join(temp_num))
                if swapped_num > biggest_num:
                    biggest_num = swapped_num
                temp_num = list(str(num))
        return biggest_num


si = Solution()
sol = si.maximumSwap(98368)
print(sol)
