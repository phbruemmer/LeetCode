class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        counter = 0
        digits.reverse()
        last_num = 0

        while counter < len(digits) -1:
            new_digit = digits[counter] + 1
            if new_digit >= 10 and digits[counter + 1] < 9:
                last_num = new_digit
                digits[counter] = new_digit % 10
                if len(digits) <= (counter + 1):
                    digits.append(0)
            else:
                if counter == 0:
                    digits[0] += 1
                elif last_num >= 10:
                    digits[counter] = new_digit
            counter += 1
        digits.reverse()
        return digits



solution_instance = Solution()
sol = solution_instance.plusOne([8,9,9,9])
print(sol)
