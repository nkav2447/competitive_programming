class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left_char = right_char = zeros = 0

        while right_char < len(nums):
            if nums[right_char] == 0:
                zeros += 1
            if zeros > 1:
                if nums[left_char] == 0:
                    zeros -= 1
                left_char += 1
            right_char += 1
         
        return right_char - left_char - 1
