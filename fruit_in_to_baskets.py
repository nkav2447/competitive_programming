class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        from collections import defaultdict
        ans = i = 0
        last = defaultdict(int)
        for idx, value in enumerate(fruits):
            if len(last) == 2 and value not in last:
                pre = min(last.values())
                i = pre + 1
                last.pop(fruits[pre])
            last[value] = idx
            ans = max(ans, idx - i + 1)
        return ans
