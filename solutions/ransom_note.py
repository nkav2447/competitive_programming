class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineCtr = {}
        for c in magazine:
            magazineCtr[c] = magazineCtr.get(c, 0) + 1
        for c in ransomNote:
            if c not in magazineCtr or magazineCtr[c] == 0:
                return False
            else:
                magazineCtr[c] -= 1
        return True
