from collections import Counter
class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ct = Counter(nums)
        res = 0
        for n in ct:
            tmp = k - n
            if n == tmp:
                res += ct[n] // 2
                continue    
            if n < tmp:
                res += min(ct[n], ct[tmp])
        return res
