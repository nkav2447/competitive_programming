class Solution(object):
    def longestOnes(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        zeros, res = [-1] + [i for i, c in enumerate(arr) if not c] + [len(arr)], 0
        for j in range(k + 1, len(zeros)):
            res = max(res, zeros[j] - zeros[j - k - 1] - 1)
        return res or k and len(arr)
