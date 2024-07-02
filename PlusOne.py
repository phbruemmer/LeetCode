class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        counter = 0
        digits.reverse()
        carry = 0

        digits[counter] += 1

        while counter < len(digits):
            digits[counter] += carry
            carry = 0
            current_digit = digits[counter]
            if current_digit >= 10:
                digits[counter] = current_digit % 10
                carry += 1
                if len(digits) <= (counter + 1):
                    digits.append(0)
            counter += 1

        digits.reverse()
        return digits


solution_instance = Solution()
sol = solution_instance.plusOne([9])
print(sol)
