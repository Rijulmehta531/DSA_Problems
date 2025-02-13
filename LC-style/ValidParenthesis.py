# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:

# Input: s = "[]"

# Output: true
# Example 2:

# Input: s = "([{}])"

# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(',']':'[','}':'{'}
        stack = []

        for c in s:
            if c not in mapping:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1] == mapping[c]:
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("([])"))
    print(sol.isValid("[(])"))