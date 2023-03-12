#added another solution
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rep = ""
        n = len(s)
        for i in range(n // 2):
            rep += s[i]
            if n % len(rep) == 0:
                if rep * (n // len(rep)) == s:
                    return True
        return False
#added another solution
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n - 1):
            sub_str = s[0 : i + 1]
            if sub_str * (n // len(sub_str)) == s:
                return True
        return False
