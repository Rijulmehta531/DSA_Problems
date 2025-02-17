from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t=="+":
                stack.append(stack.pop()+stack.pop())
            elif t=="-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a-b)
            elif t=="*":
                stack.append(stack.pop()*stack.pop())
            elif t=="/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a)/b))
            else:
                stack.append(int(t))
        return stack[-1]