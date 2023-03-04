#added another solution
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
#added another solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1
