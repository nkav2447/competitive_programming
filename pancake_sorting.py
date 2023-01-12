class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = []
        for n in range(len(arr), 1, -1):
            i = arr.index(n)
            res.extend([i + 1, n])
            arr = arr[:i:-1] + arr[:i]
        return res  
       
