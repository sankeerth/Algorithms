"""
1041. Robot Bounded In Circle

On an infinite plane, a robot initially stands at (0, 0) and faces north. 
The robot can receive one of three instructions:
"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.

Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

Constraints:
1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        current, direction = (0, 0), 'N'
        directionsToLeft = {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}
        directionsToRight = {'E': 'S', 'N': 'E', 'W': 'N', 'S': 'W'}

        def move(direction, point):
            x, y = point
            if direction == 'N':
                point = x, y+1
            elif direction == 'E':
                point = x+1, y
            elif direction == 'S':
                point = x, y-1
            else:
                point = x-1, y
            return point

        for instruction in instructions:
            if instruction == 'G':
                current = move(direction, current)
            elif instruction == 'L':
                direction = directionsToLeft[direction]
            else:
                direction = directionsToRight[direction]

        if direction == 'N' and current != (0, 0):
            return False

        return True


sol = Solution()
print(sol.isRobotBounded("GGLLGG"))
print(sol.isRobotBounded("GL"))
print(sol.isRobotBounded("GG"))
print(sol.isRobotBounded("GLGLGLGL"))
print(sol.isRobotBounded("GRGRGRGR"))
print(sol.isRobotBounded("GLGLGGLGL"))
