#another solution
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first, next = 0, n
        res = []
        while first < n:
            res.append(nums[first])
            first += 1
            if next < len(nums):
                res.append(nums[next])
                next += 1
        return res
#another solution
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
 #another solution
 class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        left = nums[:n]
        right = nums[n:]
        for i in range(len(left)):
            res.append(left[i])
            res.append(right[i])
        return res
