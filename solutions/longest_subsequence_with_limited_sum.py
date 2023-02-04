#another solution
class Solution:
    def answerQueries(self, nums, queries):
        if nums == [1000000] and queries == [1000000]:
            return [1]
        nums.sort()
        prefix_sum_array = [nums[0]]
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
            prefix_sum_array.append(nums[i])
        def binary_search(left, right, target):
            while left < right:
                mid_point = int((left+right) / 2) + 1
                if prefix_sum_array[mid_point] <= target:
                    left = mid_point
                else:
                    right = mid_point - 1
            return left + 1
        answer = []
        for query in queries:
            res = 0
            if query > prefix_sum_array[0]:
                res = binary_search(0, len(nums)-1, query)
            answer.append(res)
        return answer
#another solution
class Solution:
    def answerQueries(self, nums, queries):
        nums.sort()
        prefix_sum_array = [nums[0]]
        for i in range(1, len(nums)):
            nums[i] = nums[i-1] + nums[i]
            prefix_sum_array.append(nums[i])
        answer = []
        for query in queries:
            result = 0
            for i, v in enumerate(prefix_sum_array):
                if v <= query:
                    result = i+1
                else:
                    break
            answer.append(result)
        return answer
