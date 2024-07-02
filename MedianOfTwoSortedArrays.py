class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1_counter = 0
        n2_counter = 0

        merged_list = []

        while nums1 or nums2:
            n1_length = len(nums1)
            n2_length = len(nums2)
            if n1_length - 1 < n1_counter:
                merged_list.extend(nums2)
                break
            elif n2_length - 1 < n2_counter:
                merged_list.extend(nums1)
                break

            cur_n1 = nums1[n1_counter]
            cur_n2 = nums2[n2_counter]

            if cur_n1 < cur_n2:
                merged_list.append(cur_n1)
                nums1.pop(n1_counter)
            elif cur_n1 > cur_n2:
                merged_list.append(cur_n2)
                nums2.pop(n2_counter)
            elif cur_n1 == cur_n2:
                merged_list.append(cur_n1)
                merged_list.append(cur_n2)
                nums1.pop(n1_counter)
                nums2.pop(n2_counter)
        merged_list_len = len(merged_list) - 1
        center_1 = float(merged_list[int(merged_list_len / 2)])
        center_2 = float(merged_list[int(merged_list_len / 2) + (merged_list_len % 2 > 0)])
        return float((center_1 + center_2) / 2)


solution_instance = Solution()

n1 = [1, 2]
n2 = [3, 4]

sol = solution_instance.findMedianSortedArrays(n1, n2)
print(sol)
