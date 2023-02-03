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
