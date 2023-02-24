class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ctr = 0
        for s in stones:
            if s in jewels:
                ctr += 1
        return ctr
