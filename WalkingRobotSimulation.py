class Robot(object):
    def __init__(self, current_position, obstacles, furthest_euclidean_distance, degrees):
        self.current_position = current_position
        self.obstacles = obstacles
        self.furthest_euclidean_distance = furthest_euclidean_distance
        self.degrees = degrees

    def move(self, k):
        new_value = self.current_position[:]
        origin = self.current_position[:]

        # print(self.current_position)
        if self.degrees == 0:       # North
            new_value[1] += k
        elif self.degrees == 1:     # East
            new_value[0] += k
        elif self.degrees == 2:     # South
            new_value[1] -= k
        elif self.degrees == 3:     # West
            new_value[0] -= k

        print(new_value)

        self.current_position = self.check_path_for_obstacles(origin, new_value)
        print(self.current_position)
        self.check_furthest_distance()

    def check_path_for_obstacles(self, origin, new_position):
        start_x, start_y = origin
        end_x, end_y = new_position
        final_position = new_position

        if start_x == end_x:
            for i in self.obstacles:
                if start_y < i[1] < end_y:
                    final_position = i
                    if start_y < end_y:
                        final_position[1] -= 1
                    elif start_y > end_y:
                        final_position[1] += 1
        elif start_y == end_y:
            for i in self.obstacles:
                if start_x < i[0] < end_x:
                    final_position = i
                    if start_x < end_x:
                        final_position[0] -= 1
                    elif start_x > end_x:
                        final_position[0] += 1
        return final_position

    def euclidean_distance(self):
        return self.current_position[0] ** 2 + self.current_position[1] ** 2

    def check_furthest_distance(self):
        distance = self.euclidean_distance()
        if distance > self.furthest_euclidean_distance:
            self.furthest_euclidean_distance = distance

    def turn_check(self):
        if self.degrees == 4:
            self.degrees = 0
        elif self.degrees == -1:
            self.degrees = 3

    def turn_left(self):
        self.degrees -= 1
        self.turn_check()

    def turn_right(self):
        self.degrees += 1
        self.turn_check()


class Solution(object):
    def robotSim(self, commands, obstacles):
        bob = Robot([0, 0], obstacles, 0, 0)
        for i in commands:
            if i == -1:
                bob.turn_right()
            elif i == -2:
                bob.turn_left()
            else:
                bob.move(i)
        distance = bob.furthest_euclidean_distance
        return distance
        


si = Solution()
sol = si.robotSim([-2,-1,8,9,6], [[-1,3],[0,1],[-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]])
print(sol)
