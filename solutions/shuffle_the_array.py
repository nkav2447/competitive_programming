class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        lst = zip(nums[:n], nums[n:len(nums)])
        shuffled = []
        for i in lst:
            shuffled.append(i[0])
            shuffled.append(i[1])
        return shuffled
