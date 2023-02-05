#another solution
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num**2 for num in nums])
    
 #another solution   
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                ans.append(nums[left]**2)
                left += 1
            else:
                ans.append(nums[right]**2)
                right -= 1
        return ans[::-1]
