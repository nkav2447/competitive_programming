#added another solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for idx, num in enumerate(nums):
            target = -nums[idx]
            i, n = idx + 1, len(nums) - 1
            while i < n:
                two_sum = nums[i] + nums[n]
                if two_sum < target:
                    i += 1
                elif two_sum > target:
                    n -= 1
                else:
                    res.add((num, nums[i], nums[n]))
                    i += 1
                    n -= 1
        return res
#added another solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx-1]:
                continue
            left, right = idx + 1, len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum == 0:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif three_sum < 0:
                    left += 1
                else:
                    right -= 1
        return ans

