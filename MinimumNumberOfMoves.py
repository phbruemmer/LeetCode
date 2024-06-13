class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        result = 0
        counter = 0
        while counter < len(seats):
            result += abs(students[counter] - seats[counter])
            counter += 1
        return result


si = Solution()
seats_ = [12,14,19,19,12]
students_ = [19,2,17,20,7]
sol = si.minMovesToSeat(seats_, students_)
print(sol)
