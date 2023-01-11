class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = ['']
        for chr in s:
            if chr == '(':
                stack.append('')
            elif chr == ')':
                add = stack.pop()[::-1]
                stack[-1] += add
            else:
                stack[-1] += chr
        return stack.pop()
