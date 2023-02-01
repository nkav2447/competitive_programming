class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        min_deque, max_deque = deque(), deque()
        left = right = 0
        res = 0
        while right < len(nums):
            while min_deque and nums[right] <= nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[right] >= nums[max_deque[-1]]:
                max_deque.pop()
            min_deque.append(right)
            max_deque.append(right)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if left > min_deque[0]:
                    min_deque.popleft()
                if left > max_deque[0]:
                    max_deque.popleft()
            res = max(res, right - left + 1)
            right += 1   
        return res
