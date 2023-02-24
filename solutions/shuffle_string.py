class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        hash_map = {}
        for i, idx in enumerate(indices):
            if idx not in hash_map:
                hash_map[idx] = s[i]
        shuffled = ""
        for c in dict(sorted(hash_map.items())).values():
            shuffled += c
        return shuffled
