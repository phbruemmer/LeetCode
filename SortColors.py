class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        counter = 0
        last_zero_index = 0

        for i in range(0, len(nums)):
            cur_num = nums[counter]

            if cur_num == 2:
                nums.append(2)
            elif cur_num == 1:
                nums.insert(last_zero_index, 1)
                counter += 1
            else:
                nums.insert(0, 0)
                counter += 1
                last_zero_index += 1
            nums.pop(counter)
        print(nums)





solution_instance = Solution()
solution_instance.sortColors([2,0,2,1,1,0])


"""
c1 = 0
        c2 = 1

        while len(nums) > max(c1, c2):
            cur_c1 = nums[c1]
            cur_c2 = nums[c2]
            print(cur_c1)
            print(cur_c2)

            if cur_c1 > cur_c2:
                nums[c1], nums[c2] = nums[c2], nums[c1]
                c1 += 1
                c2 += 1
            elif cur_c1 < cur_c2:
                nums[c1], nums[c2] = nums[c2], nums[c1]
                c1 += 1
                c2 += 1
            elif cur_c1 == cur_c2:
                c1 += 1
                c2 += 1
        print(nums)
"""
