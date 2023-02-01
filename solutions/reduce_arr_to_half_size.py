class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        from collections import Counter
        ctr = Counter(arr)
        ud_arr = [y for x, y in ctr.items()]
        ud_arr.sort(reverse=True)
        m = 0
        res = 0
        for i in ud_arr:
            res += 1
            m += i
            if m * 2 >= len(arr):
                return res
