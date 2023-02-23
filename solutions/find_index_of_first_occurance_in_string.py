#another solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == 0:
            return -1
        if haystack == needle:
            return 0
        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1
 #another solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
