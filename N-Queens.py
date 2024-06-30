class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def solve(row, columns, diagonal1, diagonal2):
            pass



"""

temp_board = ""
        blocked_x_coordinates = []
        blocked_y_coordinates = []
        queen_in_row = False

        for i in range(0, n):
            for y in range(0, n):
                if not queen_in_row and i not in blocked_y_coordinates and y not in blocked_y_coordinates:
                    temp_board += 'Q'
                    blocked_x_coordinates.append(i)
                    blocked_y_coordinates.append(y)
                    queen_in_row = True
                else:
                    temp_board += '.'
            temp_board += '\n'
            queen_in_row = False

"""

si = Solution()
sol = si.totalNQueens(4)
print(sol)
