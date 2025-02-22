# We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

# Example 1:

# Input: asteroids = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

# Input: asteroids = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

# Input: asteroids = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def signOpp(a, b):
            return (a < 0 and b > 0)
        stack = []
        for a in asteroids:
            incoming = a
            while stack and signOpp(incoming, stack[-1]) and incoming != 0:
                prevAst = stack.pop()
                if abs(incoming) < abs(prevAst):
                    incoming = prevAst
                elif abs(prevAst) == abs(incoming):
                    incoming = 0
            if incoming != 0 :
                stack.append(incoming)
        return stack

if __name__ == '__main__':
    sol = Solution()
    print(sol.asteroidCollision([5,10,-5]))
    print(sol.asteroidCollision([8,-8]))
    print(sol.asteroidCollision([10,2,-5]))