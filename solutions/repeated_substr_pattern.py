class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n - 1):
            sub_str = s[0 : i + 1]
            if sub_str * (n // len(sub_str)) == s:
                return True
        return False
