class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        new = [True]*len(l)
        for i in range(len(l)):
            sub_arr = nums[l[i]:r[i]+1]
            sub_arr.sort()
            d = []
            for j in range(len(sub_arr) - 1):
                d.append(sub_arr[j+1] - sub_arr[j])
            d = list(set(d))
            if len(d) != 1:
                new[i] = False
        return new
