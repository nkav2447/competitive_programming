class Solution(object):
    def longestMountain(self, arr,):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = 0
        for n in range(1, len(arr) - 1):
            if arr[n + 1] < arr[n] > arr[n - 1]:
                left = right = n
                while left and arr[left] > arr[left - 1]: left -= 1
                while right + 1 < len(arr) and arr[right] > arr[right + 1]: right += 1
                if right - left + 1 > ans: ans = right - left + 1
        return ans
