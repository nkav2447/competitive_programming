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
