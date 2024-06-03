class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_dict:
                return [num_dict[diff], i]
            num_dict[num] = i
        return []


solution_instance = Solution()
result = solution_instance.twoSum([2, 22, 7, 15, 32, 52, 11], 9)

print(result)

"""
        for i in range(len(nums)):
            current_num = nums[i]
            print(i)
            for y in range(len(nums)):
                temp_num = nums[y]
                if current_num + temp_num == target and not y == i:
                    return [i, y]
"""


"""
        # Saves the values of the List as key and their index as value [key : index]
        num_dict = {}

        for i, num in enumerate(nums):
            # Calculates difference between target and the current num
            diff = target - num
            # if the current difference is already in the 'num_dict' - dictionary, then...
            if diff in num_dict:
                # return a list with the value (saved index) of the 'num_dict' - dictionary and the current index
                return [num_dict[diff], i]
            # Current number is key and value is current index
            num_dict[num] = i
        return []
"""