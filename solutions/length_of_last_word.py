#another solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, n = 0, len(s) - 1
        while s[n] == " ":
            n -= 1
        for i in range(n, -1, -1):
            if s[i] == " ":
                return length
            else:
                length += 1
        return length
#another solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
