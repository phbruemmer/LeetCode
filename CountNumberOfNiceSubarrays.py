class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = 1
        even_nums = []

        for i in nums:
            if i % 2:
                even_nums.append(counter)
                counter = 1
            else:
                counter += 1
        even_nums.append(counter)

        total_subarrays = 0
        for i in range(k, len(even_nums)):
            total_subarrays += even_nums[i - k] * even_nums[i]
        return total_subarrays

si = Solution()
nums_arr = [91473,45388,24720,35841,29648,77363,86290,58032,53752,87188,34428,85343,19801,73201]
k_ = 4
sol = si.numberOfSubarrays(nums_arr, k_)
print(sol) # Output must be 6

solution = Solution()
print(solution.numberOfSubarrays([1, 1, 2, 1, 1], 3))  # Output: 2
print(solution.numberOfSubarrays([2, 4, 6], 1))        # Output: 0
print(solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))  # Output: 16


"""

   def helper_function(self, num_arr, start, max_k, max_length, counter):
        cur_odds = 0
        cur_subarray = []
        for i in range(start, max_length):
            if i == max_length:
                break
            evenNum = num_arr[i] % 2 == 0
            if evenNum:
                cur_subarray.append(num_arr[i])
                if i >= max_length - 1 and cur_odds == max_k:
                    counter += self.helper_function(num_arr, start + 1, max_k, max_length, counter)
                elif i >= max_length - 1:
                    counter += self.helper_function(num_arr, start, max_k, max_length, counter)
            else:
                cur_odds += 1
                if cur_odds < max_k or cur_odds == max_k:
                    cur_subarray.append(num_arr[i])
                if cur_odds > max_k:
                    counter += self.helper_function(num_arr, start + 1, max_k, max_length, counter)
                elif cur_odds == max_k:
                    counter += 1
        return counter

"""



"""
    def helper_function(self, num_arr, start, max_k, max_length, counter):
        cur_odds = 0
        cur_subarray = []
        for i in range(start, max_length):
            if i == max_length:
                break
            evenNum = num_arr[i] % 2 == 0
            if evenNum:
                cur_subarray.append(num_arr[i])
                if cur_odds == max_k:
                    # print(cur_subarray)
                    counter += 1
                if i >= max_length - 1 and cur_odds == max_k:
                    counter = self.helper_function(num_arr, start + 1, max_k, max_length, counter)
                    break
                elif i >= max_length - 1:
                    # counter += self.helper_function(num_arr, start, max_k, max_length, counter)
                    break
            else:
                cur_odds += 1
                if cur_odds < max_k or cur_odds == max_k:
                    cur_subarray.append(num_arr[i])
                if cur_odds > max_k:
                    counter = self.helper_function(num_arr, start + 1, max_k, max_length, counter)
                    break
                elif cur_odds == max_k:
                    # print(cur_subarray)
                    counter += 1
        return counter
"""
