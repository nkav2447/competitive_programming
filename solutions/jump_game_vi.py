class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = deque([(nums[0], 0)])
        for i in range(1, len(nums)):
            while dp and dp[0][1] + k < i:
                dp.popleft()
            move = nums[i] + dp[0][0]
            while dp and move >= dp[-1][0]:
                dp.pop()
            dp.append((move, i))
        return dp[-1][0]
