class Robot(object):
    def __init__(self, current_position, furthest_euclidean_distance, degrees):
        self.current_position = current_position
        self.furthest_euclidean_distance = furthest_euclidean_distance
        self.degrees = degrees

    def move(self, k):
        if self.degrees == 0: # North
            self.current_position[1] += k
        elif self.degrees == 1: # East
            self.current_position[0] += k
        elif self.degrees == 2: # South
            self.current_position[1] -= k
        elif self.degrees == 3: # West
            self.current_position[0] -= k
        self.check_furthest_distance()
    
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
        bob = Robot([0,0], 0, 0)
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
sol = si.robotSim([4,-1,3], [])
print(sol)
sol = si.robotSim([4,-1,4,-2,4], [[2, 4]])
print(sol)
sol = si.robotSim([6,-1,-1,6], [])
print(sol)

