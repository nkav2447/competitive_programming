#another solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums)==0: return 0
        i = j = 0
        curr = float("inf")
        r_sum = nums[0]
        while i < len(nums):
            while r_sum < target:
                j+=1
                if j >= len(nums):
                    return curr if curr != float("inf") else 0
                else:
                    r_sum += nums[j]
            curr = min(curr, j - i + 1)
            r_sum -= nums[i]
            i+=1
        return curr
#another solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        window_sum, window_start = 0, 0
        for window_end in range(len(nums)):
            window_sum += nums[window_end] 
            while window_sum >= target:
                min_length = min(min_length, window_end-window_start+1)
                window_sum -= nums[window_start]
                window_start += 1
        if min_length == float('inf'):
            return 0
        return min_length
#another solution
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, ans, curr = 0, len(nums) + 1, 0
        for idx, num in enumerate(nums):
            curr += num
            while curr >= target: ans, left, curr = min(ans, idx - left + 1), left + 1, curr - nums[left]
        return ans < len(nums) + 1 and ans or 0
