class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l, r, ans = 0, 0, 0
        for c in s:
            if c == "L":
                l += 1
            else:
                r += 1
            if l == r:
                ans += 1
        return ans
