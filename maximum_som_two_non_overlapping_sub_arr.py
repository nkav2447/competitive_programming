class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        n = len(nums)
        l = [0] * n
        r = [0] * n
        sm = 0 
        for i in range(secondLen - 1):
            sm += nums[i]
        for j in range(n - secondLen + 1):
            sm += nums[j + secondLen - 1]
            for i in range(j + 1):
                r[i] = max(r[i], sm)
            sm -= nums[j]
        
        sm = 0
        for i in range(n - 1, n - secondLen, -1):
            sm += nums[i]
        for i in range(n - 1, secondLen - 2, -1):
            sm += nums[i - secondLen + 1]
            for j in range(i + 1, n):
                l[j] = max(l[j], sm)
            sm -= nums[i]
        sm = 0
        for i in range(firstLen - 1):
            sm += nums[i]
        res = 0
        for j in range(n - firstLen + 1):
            sm += nums[j + firstLen - 1]
            if j >= secondLen:
                res = max(res, sm + l[j - 1])
            if j + firstLen < n:
                res = max(res, sm + r[j + firstLen])
            sm -= nums[j]
        return res
