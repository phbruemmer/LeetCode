class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        digit_list = []
        counter = 0

        while not x < 0:
            end_digit = x // 10 ** counter
            if not end_digit < 1:
                digit = end_digit % 10
                digit_list.append(digit)
            else:
                reversed_list = digit_list[::-1]
                if reversed_list == digit_list:
                    return True
                else:
                    return False
            counter += 1


solution_instance = Solution()
sol = solution_instance.isPalindrome(101)
print(sol)

"""

    def isPalindrome(self, x):
        :type x: int
        :rtype: bool
        if x < 0:
            return False

        cur_mod_value = 10
        digit_list = []
        isPalindrome = False

        while not x % cur_mod_value == x:
            new_val = x % cur_mod_value
            if new_val > cur_mod_value // 10:
                new_val = new_val // (cur_mod_value // 10)
            digit_list.append(new_val)
            cur_mod_value = cur_mod_value * 10
        new_val = x % cur_mod_value
        if new_val > cur_mod_value // 10:
            new_val = new_val // (cur_mod_value // 10)
        digit_list.append(new_val)
        reversed_list = digit_list[::-1]
        print(digit_list)
        print(reversed_list)

        if reversed_list == digit_list:
            isPalindrome = True
        return isPalindrome

"""
