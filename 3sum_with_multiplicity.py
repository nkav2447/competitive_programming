class Solution(object):
    def threeSumMulti(self, arr, target):
        from collections import Counter
        from itertools import combinations_with_replacement
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        c = Counter(arr)
        ans = 0
        for i, j in combinations_with_replacement(c, 2):
            k = target - i - j
            if i == j == k: 
                ans += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            elif i == j != k: 
                ans += c[i] * (c[i] - 1) // 2 * c[k]
            elif k > i and k > j: 
                ans += c[i] * c[j] * c[k]
        return ans % (10**9 + 7)
