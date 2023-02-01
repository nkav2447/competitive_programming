class Solution(object):
    def sortColors(self, nums):
        num1, num2, num3 = 0, 0, len(nums)-1
        while(num2 <= num3):
            if nums[num2] == 0:
                nums[num2], nums[num1] = nums[num1], 0
                num1, num2 = num1+1, num2+1
            elif nums[num2] == 2:
                nums[num2], nums[num3] = nums[num3], 2
                num3 -= 1
            else:
                num2 += 1
