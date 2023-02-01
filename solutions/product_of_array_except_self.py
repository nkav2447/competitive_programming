class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        left_running_product, right_running_product, products = [0] * length, [0] * length, [0] * length
        left_running_product[0] = 1
        for i in range(1, length):
            left_running_product[i] = nums[i - 1] * left_running_product[i - 1]
        right_running_product[length - 1] = 1
        for i in range(length - 2, -1, -1):
            right_running_product[i] = nums[i + 1] * right_running_product[i + 1]
        for i in range(length):
            products[i] = left_running_product[i] * right_running_product[i]
        return products
