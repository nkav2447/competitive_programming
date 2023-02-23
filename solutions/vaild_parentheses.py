#added another solution
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "]": "[", "}": "{"}
        opened = "({["
        closed = ")}]"
        stack = []
        for c in s:
            if c in opened:
                stack.append(c)
            elif c in closed:
                if stack and stack[-1] == brackets[c]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
#added another solution
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        opening = set('([{')
        closing = set(')]}')
        pair = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i in opening:
                stack.append(i)
            if i in closing:
                if not stack:
                    return False
                elif stack.pop() != pair[i]:
                    return False
                else:
                    continue
        if not stack:
            return True
        else:
            return False
