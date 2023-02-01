class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, mst = 0, len(height) - 1, 0
        while left < right:
            mst = max(mst, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]: 
                left += 1
            else: 
                right -= 1
        return mst
