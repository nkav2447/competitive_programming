class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        running_sum = res = 0
        prefix_sum = {0:1}
        for num in nums:
            running_sum += num
            rem = running_sum % k
            if rem in prefix_sum:
                res += prefix_sum[rem]
                prefix_sum[rem] += 1
            else:
                prefix_sum[rem] = 1
        return res
