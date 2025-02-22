# Generate Parentheses
# You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

# Example 1:

# Input: n = 1

# Output: ["()"]
# Example 2:

# Input: n = 3

# Output: ["((()))","(()())","(())()","()(())","()()()"]
# You may return the answer in any order.



from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN and openN == n:
                res.append(''.join(stack))
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN+1)
                stack.pop()
        backtrack (0,0)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(1))
    print(sol.generateParenthesis(3))