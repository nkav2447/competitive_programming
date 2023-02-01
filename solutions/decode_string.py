class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, n, dec_string = [], 0, ""
        for c in s:
            if c == "[":
                stack += dec_string,
                stack += n,
                n, dec_string = 0, ""
            elif c == "]":
                pre_num, bef_dec_string = stack.pop(), stack.pop()
                dec_string = bef_dec_string + pre_num * dec_string
            elif c.isdigit():
                 n = n * 10 + int(c)
            else: 
                dec_string += c
        return dec_string
