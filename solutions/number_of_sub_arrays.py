class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        sub_array_sum = 0
        sub_array_count = 0
        window = 0
        for i in range(len(arr)):
            sub_array_sum += arr[i]
            if i - window + 1 ==k:
                if sub_array_sum/k >= threshold:
                    sub_array_count += 1
                sub_array_sum -= arr[window]
                window += 1
        return sub_array_count
